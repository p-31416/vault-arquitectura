import { jsPDF } from 'jspdf'
import { ICC_LABEL, K, type RangoMonto } from '../data/cpau'

export type DatosObra = {
  nombre: string
  direccion: string
  cliente: string
}

export type EtapaPresupuesto = {
  indice: number
  nombre: string
  articulo: string
  definicion: string
  definicionCliente?: string
  parcialPct: number
  acumuladoPct: number
  parcial: number
  acumulado: number
}

export type LogoPDF = { url: string; formato: 'PNG' | 'JPEG' } | null

export type VersionPresupuesto = 'estudio' | 'cliente'

export type Params = {
  datos: DatosObra
  fecha: Date
  logo: LogoPDF
  version: VersionPresupuesto
  M: number
  rango: RangoMonto
  grupoLabel: string
  expresion: string
  honorarioTotal: number
  etapas: EtapaPresupuesto[]
  montoEtapas: number
  pctEtapas: number
  remodelacion: boolean
  pctRemodelacion: number
  adicionalRemodelacion: number
}

export const ESTUDIO = 'Estudio Pi'
export const ESTUDIO_SUB = 'Presupuesto de honorarios · CPAU 31416'
export const CLIENTE_NOTA =
  'INCLUYE honorarios profesionales únicamente por las tareas antes detalladas. NO INCLUYE Ejecución, dirección de obra, tasas, IVA, sellados u otras tramitaciones municipales/provinciales.'

export const VALIDEZ_NOTA = 'Presupuesto válido por 15 días corridos.'

type RGB = readonly [number, number, number]

const COLOR: Record<string, RGB> = {
  ink: [26, 36, 33],
  muted: [94, 107, 102],
  faint: [135, 145, 140],
  accent: [15, 110, 86],
  accentDeep: [10, 79, 61],
  soft: [238, 243, 240],
  line: [201, 192, 174],
}

function money(n: number): string {
  return '$' + Math.round(n).toLocaleString('es-AR')
}

function pct(f: number): string {
  return (Math.round(f * 1000) / 10).toLocaleString('es-AR') + '%'
}

function fechaStr(d: Date): string {
  return d.toLocaleDateString('es-AR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  })
}

function listarEtapas(nombres: string[]): string {
  if (nombres.length === 0) return 'Etapa completa'
  if (nombres.length === 1) return nombres[0]
  if (nombres.length === 2) return `${nombres[0]} y ${nombres[1]}`
  return `${nombres.slice(0, -1).join(', ')} y ${nombres[nombres.length - 1]}`
}

function acronimoObra(nombre: string): string {
  const limpio = nombre
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-zA-Z0-9]/g, '')
    .toUpperCase()
  return limpio.slice(0, 3) || 'OBRA'
}

export function nombreArchivoPresupuesto(
  fecha: Date,
  datos: DatosObra,
  etapas: EtapaPresupuesto[],
  version: VersionPresupuesto = 'estudio',
): string {
  const pad = (n: number) => String(n).padStart(2, '0')
  const fechaCompacta = `${fecha.getFullYear()}${pad(fecha.getMonth() + 1)}${pad(fecha.getDate())}`
  const nEtapas = etapas.length
    ? etapas.map((e) => e.indice).join('_')
    : '0'
  const base = `${acronimoObra(datos.nombre)}-${nEtapas}-PRES_HON-${fechaCompacta}`
  if (version !== 'cliente') return `${base}-INTERNO.pdf`
  const cliente = acronimoObra(datos.cliente)
  return cliente === 'OBRA' ? `${base}.pdf` : `${base}-${cliente}.pdf`
}

export function buildPresupuestoPDF(params: Params): jsPDF {
  const { datos, etapas } = params
  const esCliente = params.version === 'cliente'
  const doc = new jsPDF({ unit: 'mm', format: 'a4' })
  const w = doc.internal.pageSize.getWidth()
  const h = doc.internal.pageSize.getHeight()
  const margin = 16
  const maxW = w - margin * 2
  let y = 0

  const fill = (c: RGB) => doc.setFillColor(c[0], c[1], c[2])
  const stroke = (c: RGB) => doc.setDrawColor(c[0], c[1], c[2])
  const textColor = (c: RGB) => doc.setTextColor(c[0], c[1], c[2])

  function ensure(space = 0): number {
    if (y + space > h - 24) {
      doc.addPage()
      return 20
    }
    return y
  }

  function dibujarBox(yy: number, titulo: string, sub: string): number {
    fill(COLOR.accentDeep)
    doc.rect(margin, yy, maxW, 24, 'F')
    doc.setTextColor(255, 255, 255)
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(8)
    doc.text(titulo, margin + 4, yy + 7)
    doc.setFontSize(16)
    doc.text(money(params.montoEtapas), margin + 4, yy + 16)
    doc.setFont('helvetica', 'normal')
    doc.setFontSize(9)
    doc.setTextColor(210, 232, 224)
    doc.text(sub, w - margin - 4, yy + 16, { align: 'right' })
    return yy + 24 + 8
  }

type PagoPresupuesto = { desc: string; pct: number }

function planPagos(etapas: EtapaPresupuesto[]): PagoPresupuesto[] {
  const n = etapas.length
  if (n <= 1) {
    return [
      { desc: '60% adelanto', pct: 0.6 },
      { desc: '40% contraentrega de la documentación', pct: 0.4 },
    ]
  }
  if (n === 2) {
    return [
      { desc: '40% encargo (antes de los croquis preliminares)', pct: 0.4 },
      {
        desc: '30% en la reunión intermedia (luego del análisis de las variantes)',
        pct: 0.3,
      },
      { desc: '30% contra entrega de la documentación', pct: 0.3 },
    ]
  }
  const total = n + 1
  const pct = 1 / total
  const pagos: PagoPresupuesto[] = [
    { desc: `Encargo (antes de ${etapas[0].nombre})`, pct },
  ]
  for (let i = 1; i < n; i++) {
    pagos.push({ desc: `Antes de ${etapas[i].nombre}`, pct })
  }
  pagos.push({ desc: 'Contra entrega de la documentación', pct })
  return pagos
}

function cronogramaPagos(
  etapas: EtapaPresupuesto[],
): { titulo: string; sub: string; pct: number }[] {
  const n = etapas.length
  if (n === 2) {
    return [
      { titulo: 'ENCARGO', sub: `de ${etapas[0].nombre}`, pct: 0.4 },
      { titulo: 'REUNIÓN INTERMEDIA', sub: 'análisis de variantes', pct: 0.3 },
      {
        titulo: 'CONTRA ENTREGA',
        sub: 'entrega de la documentación',
        pct: 0.3,
      },
    ]
  }
  if (n <= 1) {
    return [
      { titulo: 'ADELANTO', sub: 'señal de encargo', pct: 0.6 },
      {
        titulo: 'CONTRA ENTREGA',
        sub: 'entrega de la documentación',
        pct: 0.4,
      },
    ]
  }
  const pctEq = 1 / (n + 1)
  const items: { titulo: string; sub: string; pct: number }[] = [
    { titulo: 'ENCARGO', sub: `de ${etapas[0].nombre}`, pct: pctEq },
  ]
  for (let i = 1; i < n; i++) {
    items.push({ titulo: `PAGO ${i + 1}`, sub: `antes de ${etapas[i].nombre}`, pct: pctEq })
  }
  items.push({
    titulo: 'CONTRA ENTREGA',
    sub: 'entrega de la documentación',
    pct: pctEq,
  })
  return items
}

  function dibujarPago(yy: number): number {
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(11)
    textColor(COLOR.ink)
    doc.text('Modalidad de pago', margin, yy)
    yy += 6.5
    doc.setFont('helvetica', 'normal')
    doc.setFontSize(9.5)
    textColor(COLOR.ink)
    stroke(COLOR.line)
    doc.setLineWidth(0.3)
    for (const p of planPagos(params.etapas)) {
      if (yy > h - 26) {
        doc.addPage()
        yy = 20
      }
      doc.text(p.desc, margin, yy)
      doc.text(money(params.montoEtapas * p.pct), w - margin, yy, {
        align: 'right',
      })
      doc.line(margin, yy + 2.2, w - margin, yy + 2.2)
      yy += 6.5
    }
    return yy + 7
  }

  function dibujarTimeline(yy: number): number {
    const n = etapas.length
    if (n === 0) return yy

    const DURACIONES: Record<string, number> = {
      'Croquis preliminares': 1,
      'Croquis avanzados': 2,
      'Anteproyecto': 2,
      'Anteproyecto avanzado': 2,
      'Documentación de proyecto': 3,
      'Dirección de obra': 8,
    }
    const DETALLE: Record<string, string> = {
      'Croquis preliminares': '5 días hábiles · planos y memoria descriptiva.',
      'Croquis avanzados':
        '10 días hábiles · planos, renders 3D, esquemáticos de instalaciones (eléctricas y sanitarias) y diagrama estructural.',
    }

    const weeks = etapas.map((e) => DURACIONES[e.nombre] ?? 1)
    let cursor = 0
    for (let i = 0; i < n; i++) {
      cursor += weeks[i]
      if (i < n - 1) cursor += 1
    }
    const totalWeeks = cursor
    const scale = 1 / totalWeeks

    const amber: RGB = [231, 165, 28]
    const amberDark: RGB = [181, 125, 0]
    const softGreen: RGB = [87, 165, 140]
    const gray: RGB = [154, 165, 160]

    const stageStartFrac: number[] = []
    const blocks: { label: string; frac: number; color: RGB }[] = []
    const mileFracs: number[] = []
    cursor = 0
    for (let i = 0; i < n; i++) {
      stageStartFrac.push(cursor * scale)
      blocks.push({
        label: etapas[i].nombre.toUpperCase(),
        frac: weeks[i] * scale,
        color: i % 2 === 0 ? softGreen : COLOR.accent,
      })
      cursor += weeks[i]
      if (i < n - 1) {
        blocks.push({ label: 'REUNIÓN', frac: 1 * scale, color: gray })
        mileFracs.push((cursor + 0.5) * scale)
        cursor += 1
      } else {
        mileFracs.push(1)
      }
    }
    const posX = [0, ...mileFracs]

    const items = cronogramaPagos(etapas)
    const nItems = items.length

    const pad = 4
    const innerLeft = margin + pad
    const innerRight = margin + maxW - pad
    const innerW = maxW - pad * 2

    const descTexts = etapas.map((e, i) => {
      const det = DETALLE[e.nombre]
      if (det) return det
      return weeks[i] === 1 ? '1 semana estimada' : `${weeks[i]} semanas estimadas`
    })
    const cols = descTexts.map((t, i) =>
      doc.splitTextToSize(t, Math.max(18, weeks[i] * scale * innerW - 4)),
    )
    const colH = Math.max(...cols.map((c) => c.length * 3.2), 3.2)

    const axisH = 16
    const barH = 8
    const totalH = 4 + 5 + axisH + barH + 3.2 + 6.2 + 9.7 + 3 + colH + 5

    if (yy + totalH > h - 24) {
      doc.addPage()
      yy = 20
    }

    fill(COLOR.soft)
    doc.roundedRect(margin, yy, maxW, totalH, 2.5, 2.5, 'F')
    stroke(COLOR.line)
    doc.setLineWidth(0.4)
    doc.roundedRect(margin, yy, maxW, totalH, 2.5, 2.5, 'S')

    doc.setFont('helvetica', 'bold')
    doc.setFontSize(8)
    textColor(COLOR.accent)
    doc.text('CRONOGRAMA DE PAGOS', innerLeft, yy + 4.5)

    const axisTop = yy + 8
    const barTop = axisTop + axisH
    const barMidY = barTop + barH / 2

    function rombo(cx: number, cy: number, r: number, c: RGB): void {
      fill(c)
      doc.triangle(cx, cy - r, cx - r, cy, cx, cy + r, 'F')
      doc.triangle(cx, cy - r, cx + r, cy, cx, cy + r, 'F')
    }

    doc.setLineWidth(0.3)
    doc.setLineDashPattern([0.8, 0.8], 0)
    for (const fx of posX) {
      const x = innerLeft + fx * innerW
      doc.setDrawColor(amber[0], amber[1], amber[2])
      doc.line(x, axisTop + 4, x, barMidY)
    }
    doc.setLineDashPattern([], 0)

    items.forEach((it, i) => {
      const x = innerLeft + posX[i] * innerW
      const dotY = axisTop + 3
      rombo(x, dotY, 2.3, [255, 255, 255])
      rombo(x, dotY, 1.7, amber)

      const align: 'left' | 'center' | 'right' =
        nItems === 1
          ? 'center'
          : i === 0
            ? 'left'
            : i === nItems - 1
              ? 'right'
              : 'center'
      const tx = x + (align === 'left' ? 2.5 : align === 'right' ? -2.5 : 0)

      doc.setFont('helvetica', 'bold')
      doc.setFontSize(6.5)
      textColor(COLOR.ink)
      doc.text(`${it.titulo} · ${pct(it.pct)}`, tx, axisTop + 8, { align })
      doc.setFontSize(7)
      textColor(amberDark)
      doc.text(money(params.montoEtapas * it.pct), tx, axisTop + 11.2, {
        align,
      })
      doc.setFont('helvetica', 'italic')
      doc.setFontSize(5.5)
      textColor(COLOR.muted)
      doc.text(it.sub, tx, axisTop + 14, { align })
    })

    let bx = innerLeft
    blocks.forEach((b, i) => {
      const bw = b.frac * innerW
      fill(b.color)
      if (i === 0 && blocks.length > 1) {
        doc.roundedRect(bx, barTop, bw, barH, 1.5, 1.5, 'F')
        doc.rect(bx + bw - 1.5, barTop, 1.5, barH, 'F')
      } else if (i === blocks.length - 1 && blocks.length > 1) {
        doc.roundedRect(bx, barTop, bw, barH, 1.5, 1.5, 'F')
        doc.rect(bx, barTop, 1.5, barH, 'F')
      } else if (blocks.length === 1) {
        doc.roundedRect(bx, barTop, bw, barH, 1.5, 1.5, 'F')
      } else {
        doc.rect(bx, barTop, bw, barH, 'F')
      }
      bx += bw
    })

    posX.forEach((fx) => {
      rombo(innerLeft + fx * innerW, barMidY, 2.3, [255, 255, 255])
      rombo(innerLeft + fx * innerW, barMidY, 1.7, amber)
    })

    doc.setFont('helvetica', 'bold')
    doc.setFontSize(6)
    textColor(COLOR.ink)
    bx = innerLeft
    blocks.forEach((b) => {
      const bw = b.frac * innerW
      doc.text(b.label, bx + bw / 2, barTop + barH + 3.2, { align: 'center' })
      bx += bw
    })

    stroke(COLOR.faint)
    doc.setLineWidth(0.3)
    for (let k = 1; k < totalWeeks; k++) {
      const tx = innerLeft + (k / totalWeeks) * innerW
      doc.line(tx, barTop + barH + 1, tx, barTop + barH + 4.5)
    }
    doc.setFont('helvetica', 'normal')
    doc.setFontSize(5.5)
    textColor(COLOR.faint)
    for (let k = 1; k <= totalWeeks; k++) {
      const cx = innerLeft + ((k - 0.5) / totalWeeks) * innerW
      doc.text(`Sem ${k}`, cx, barTop + barH + 6.2, { align: 'center' })
    }
    const meses = totalWeeks / 4
    const totalLabel =
      meses <= 1.25
        ? '1 mes'
        : meses <= 2.25
          ? 'mes y medio'
          : meses <= 3.25
            ? 'dos meses'
            : `${Math.round(meses)} meses`
    doc.setFont('helvetica', 'italic')
    doc.setFontSize(5.5)
    textColor(amberDark)
    doc.text(`~ ${totalWeeks} semanas · ${totalLabel}`, innerRight, barTop + barH + 9.7, {
      align: 'right',
    })

    const descTop = barTop + barH + 12.2
    doc.setFont('helvetica', 'italic')
    doc.setFontSize(6)
    textColor(COLOR.muted)
    cols.forEach((c, i) => {
      let ly = descTop
      const colLeft = innerLeft + stageStartFrac[i] * innerW
      for (const ln of c) {
        doc.text(ln, colLeft, ly)
        ly += 3.2
      }
    })

    return yy + totalH + 8
  }

  fill(COLOR.soft)
  doc.rect(0, 0, w, 30, 'F')
  fill(COLOR.accent)
  doc.rect(0, 30, w, 1.4, 'F')

  let logoW = 0
  if (params.logo) {
    try {
      const info = doc.getImageProperties(params.logo.url)
      const logoH = 15
      logoW = logoH * (info.width / info.height)
      doc.addImage(params.logo.url, params.logo.formato, margin, 7.5, logoW, logoH)
    } catch (err) {
      console.warn('No se pudo dibujar el logo en el PDF', err)
      logoW = 0
    }
  }
  const brandX = margin + logoW + (logoW ? 5 : 0)

  doc.setFont('helvetica', 'bold')
  doc.setFontSize(16)
  textColor(COLOR.ink)
  doc.text(ESTUDIO, brandX, 14)
  doc.setFont('helvetica', 'normal')
  doc.setFontSize(8.5)
  textColor(COLOR.muted)
  doc.text(ESTUDIO_SUB, brandX, 19.5)
  doc.text(`Fecha: ${fechaStr(params.fecha)}`, w - margin, 14, {
    align: 'right',
  })

  y = 38
  doc.setFont('helvetica', 'bold')
  doc.setFontSize(8)
  textColor(COLOR.accent)
  doc.text('OBRA', margin, y)
  y += 5.2
  doc.setFontSize(19)
  textColor(COLOR.ink)
  const obra = datos.nombre || 'Presupuesto de honorarios'
  for (const ln of doc.splitTextToSize(obra, maxW)) {
    y = ensure(8)
    doc.text(ln, margin, y)
    y += 7
  }
  doc.setFont('helvetica', 'normal')
  doc.setFontSize(9.5)
  textColor(COLOR.muted)
  if (datos.cliente) {
    y = ensure(5)
    doc.text(`Cliente: ${datos.cliente}`, margin, y)
    y += 5
  }
  if (datos.direccion) {
    y = ensure(5)
    doc.text(`Dirección: ${datos.direccion}`, margin, y)
    y += 5
  }
  y += 3
  y = ensure(1)
  stroke(COLOR.line)
  doc.setLineWidth(0.4)
  doc.line(margin, y, w - margin, y)
  y += 8

  y = ensure(6)
  doc.setFont('helvetica', 'bold')
  doc.setFontSize(9)
  textColor(COLOR.accent)
  doc.text('PRESUPUESTO DE HONORARIOS POR', margin, y)
  y += 5.5
  doc.setFontSize(13)
  textColor(COLOR.ink)
  const nombresEtapas = etapas.map((e) => e.nombre)
  const tituloEtapas = listarEtapas(nombresEtapas)
  for (const ln of doc.splitTextToSize(tituloEtapas, maxW)) {
    y = ensure(6.2)
    doc.text(ln, margin, y)
    y += 6
  }
  y += 5
  y = ensure(1)
  stroke(COLOR.line)
  doc.line(margin, y, w - margin, y)
  y += 8

  if (esCliente) {
    y = ensure(10)
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(11)
    textColor(COLOR.ink)
    doc.text('Etapas incluidas', margin, y)
    y += 6.5
    doc.setFont('helvetica', 'normal')
    doc.setFontSize(9.5)
    for (const e of etapas) {
      if (y > h - 26) {
        doc.addPage()
        y = 20
      }
      doc.setFont('helvetica', 'bold')
      doc.setFontSize(9.5)
      textColor(COLOR.ink)
      const nombreW = doc.getTextWidth(e.nombre)
      doc.text(e.nombre, margin, y)
      doc.setFont('helvetica', 'italic')
      doc.setFontSize(7.5)
      textColor(COLOR.muted)
      doc.text(e.articulo, margin + nombreW + 3, y + 0.5)
      doc.text(money(e.parcial), w - margin, y, { align: 'right' })
      stroke(COLOR.line)
      doc.setLineWidth(0.3)
      doc.line(margin, y + 2.2, w - margin, y + 2.2)
      y += 6.2
      doc.setFont('helvetica', 'italic')
      doc.setFontSize(8)
      textColor(COLOR.muted)
      for (const ln of doc.splitTextToSize(e.definicionCliente ?? e.definicion, maxW - 34)) {
        if (y > h - 26) {
          doc.addPage()
          y = 20
        }
        doc.text(ln, margin, y)
        y += 3.8
      }
      y += 2
    }

    y = ensure(34)
    y = dibujarBox(y, 'HONORARIOS PROFESIONALES', 'por etapas incluidas')

    y = ensure(24)
    y = dibujarPago(y)

    y = ensure(5)
    doc.setFont('helvetica', 'italic')
    doc.setFontSize(8)
    textColor(COLOR.muted)
    doc.text('*efectivo o transferencia - se entrega factura "C"', margin, y)
    y += 6

    y = dibujarTimeline(y)
  } else {
    y = ensure(36)
    const bandY = y
    fill(COLOR.soft)
    doc.rect(margin, bandY, maxW, 27, 'F')

    doc.setFont('helvetica', 'normal')
    doc.setFontSize(10)
    textColor(COLOR.muted)
    doc.text('Monto de obra M', margin + 4, bandY + 7)
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(12)
    textColor(COLOR.ink)
    doc.text(money(params.M), w - margin - 4, bandY + 7, { align: 'right' })

    doc.setFont('helvetica', 'normal')
    doc.setFontSize(10)
    textColor(COLOR.muted)
    doc.text('Honorario total (proyecto y dirección)', margin + 4, bandY + 14.5)
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(14)
    textColor(COLOR.accentDeep)
    doc.text(money(params.honorarioTotal), w - margin - 4, bandY + 14.5, {
      align: 'right',
    })

    doc.setFont('helvetica', 'normal')
    doc.setFontSize(8)
    textColor(COLOR.muted)
    let detalle = `Rango ${params.rango} · ${params.expresion} · ${params.grupoLabel}`
    if (params.remodelacion) {
      detalle += ` · +${pct(params.pctRemodelacion)} remodelación (${money(params.adicionalRemodelacion)})`
    }
    doc.text(detalle, margin + 4, bandY + 22.5)

    y = bandY + 27 + 8

    y = ensure(44)
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(11)
    textColor(COLOR.ink)
    doc.text('Detalle por etapas', margin, y)
    y += 6.5

    const cEtapa = 74
    const cPct = 26
    const cParcial = 44

    function cabeceraEtapas(ty: number): number {
      fill(COLOR.accentDeep)
      doc.rect(margin, ty - 4.5, maxW, 6.5, 'F')
      doc.setTextColor(255, 255, 255)
      doc.setFont('helvetica', 'bold')
      doc.setFontSize(8)
      doc.text('ETAPA', margin + 2, ty)
      doc.text('%', margin + cEtapa, ty, { align: 'right' })
      doc.text('PARCIAL', margin + cEtapa + cPct, ty, { align: 'right' })
      doc.text('ACUMULADO', margin + cEtapa + cPct + cParcial, ty, {
        align: 'right',
      })
      return ty + 6.5
    }

    y = cabeceraEtapas(y)
    doc.setFont('helvetica', 'normal')
    doc.setFontSize(9)
    textColor(COLOR.ink)
    etapas.forEach((e, i) => {
      if (y > h - 26) {
        doc.addPage()
        y = 20
        y = cabeceraEtapas(y)
        doc.setFont('helvetica', 'normal')
        doc.setFontSize(9)
        textColor(COLOR.ink)
      }
      if (i % 2 === 1) {
        fill(COLOR.soft)
        doc.rect(margin, y - 4.2, maxW, 5.6, 'F')
      }
      doc.text(e.nombre, margin + 2, y)
      doc.text(pct(e.parcialPct), margin + cEtapa, y, { align: 'right' })
      doc.text(money(e.parcial), margin + cEtapa + cPct, y, { align: 'right' })
      doc.text(money(e.acumulado), margin + cEtapa + cPct + cParcial, y, {
        align: 'right',
      })
      y += 5.6
    })
    y += 5

    y = ensure(34)
    y = dibujarBox(y, 'PRESUPUESTO DE LA ETAPA SELECCIONADA', `${pct(params.pctEtapas)} del honorario total`)

    y = ensure(24)
    y = dibujarPago(y)

    y = ensure(24)
    doc.setFont('helvetica', 'bold')
    doc.setFontSize(9)
    textColor(COLOR.ink)
    doc.text('Nota — detalle de las etapas', margin, y)
    y += 5
    doc.setFont('helvetica', 'italic')
    doc.setFontSize(8)
    textColor(COLOR.muted)
    for (const e of etapas) {
      for (const ln of doc.splitTextToSize(
        `* ${e.articulo} — ${e.nombre}: ${e.definicion}`,
        maxW,
      )) {
        y = ensure(4)
        doc.text(ln, margin, y)
        y += 3.8
      }
      y += 2
    }
  }

  const totalPages = doc.getNumberOfPages()
  for (let i = 1; i <= totalPages; i++) {
    doc.setPage(i)
    // Validez — siempre visible, por encima del pie
    doc.setFont('helvetica', 'italic')
    doc.setFontSize(6.5)
    textColor(COLOR.muted)
    doc.text(VALIDEZ_NOTA, w / 2, h - 19.5, { align: 'center' })
    stroke(COLOR.line)
    doc.setLineWidth(0.3)
    doc.line(margin, h - 16, w - margin, h - 16)
    doc.setFont('helvetica', 'normal')
    doc.setFontSize(7)
    textColor(COLOR.faint)
    if (esCliente) {
      doc.setFont('helvetica', 'bold')
      doc.setFontSize(7)
      textColor(COLOR.faint)
      doc.text('NOTAS', margin, h - 11.5)
      const notaLines = doc.splitTextToSize(CLIENTE_NOTA, maxW - 28)
      doc.setFont('helvetica', 'normal')
      doc.setFontSize(6.5)
      textColor(COLOR.faint)
      let ly = h - 7.5 - (notaLines.length - 1) * 3.2
      for (const ln of notaLines) {
        doc.text(ln, w / 2, ly, { align: 'center' })
        ly += 3.2
      }
      doc.text(`${ESTUDIO} · ${fechaStr(params.fecha)}`, w - margin, h - 11.5, {
        align: 'right',
      })
    } else {
      doc.text(`${ICC_LABEL} · K = ${money(K)}`, margin, h - 11.5)
      doc.text(
        'Valores indicativos según cuadros CPAU y modelos ARQ Clarín. No incluyen IVA ni impuestos locales.',
        margin,
        h - 7.5,
      )
      doc.text(ESTUDIO, w - margin, h - 11.5, { align: 'right' })
      doc.text(fechaStr(params.fecha), w - margin, h - 7.5, { align: 'right' })
    }
  }

  return doc
}

export function generarPresupuestoPDF(params: Params): void {
  const doc = buildPresupuestoPDF(params)
  doc.save(nombreArchivoPresupuesto(params.fecha, params.datos, params.etapas, params.version))
}
