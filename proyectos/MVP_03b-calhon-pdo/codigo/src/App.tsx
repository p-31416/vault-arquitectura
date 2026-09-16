import { useEffect, useId, useMemo, useState } from 'react'
import {
  escalarRubro,
  getTipologia,
  rubrosConPorcentaje,
  TIPOLOGIA_OBRA_NUEVA_DEFAULT,
  TIPOLOGIAS,
  type TipologiaClarin,
} from './data/clarin'
import { GRUPOS, ICC_LABEL, K, REMODELACION_PCT, type GrupoObra } from './data/cpau'
import {
  formatNumero,
  formatPesos,
  formatPorcentaje,
  formatPorcentajeDetalle,
} from './lib/format'
import { calcularHonorario, estimarMonto } from './lib/honorarios'
import {
  buildPresupuestoPDF,
  nombreArchivoPresupuesto,
  type LogoPDF,
  type VersionPresupuesto,
} from './lib/presupuesto'
import { PresupuestoModal, type DatosPresupuesto } from './components/PresupuestoModal'
import {
  PresupuestoPreview,
  type EstadoDescarga,
  type PreviewItem,
} from './components/PresupuestoPreview'
import './App.css'

function App() {
  const ids = {
    tipologia: useId(),
    superficie: useId(),
    precio: useId(),
    monto: useId(),
    grupo: useId(),
  }

  const tipologiaInicial = useMemo<TipologiaClarin>(() => {
    const guardada = localStorage.getItem('calhon:tipologia')
    if (guardada && TIPOLOGIAS.some((t) => t.id === guardada)) {
      return getTipologia(guardada)
    }
    return getTipologia(TIPOLOGIA_OBRA_NUEVA_DEFAULT)
  }, [])

  const [tipologiaId, setTipologiaId] = useState(tipologiaInicial.id)
  const [remodelacion, setRemodelacion] = useState(
    tipologiaInicial.tipo === 'reciclaje',
  )
  const [grupo, setGrupo] = useState<GrupoObra>(1)
  const [superficie, setSuperficie] = useState(tipologiaInicial.superficieRef)
  const [precioM2, setPrecioM2] = useState(tipologiaInicial.precioM2)
  const [montoManual, setMontoManual] = useState(false)
  const [monto, setMonto] = useState(() =>
    estimarMonto(tipologiaInicial.precioM2, tipologiaInicial.superficieRef),
  )
  const [rubrosAbiertos, setRubrosAbiertos] = useState(
    Boolean(tipologiaInicial.rubros?.length),
  )
  const [rubrosActivos, setRubrosActivos] = useState<Set<string>>(
    () => new Set((tipologiaInicial.rubros ?? []).map((r) => r.id)),
  )
  const [etapasSeleccionadas, setEtapasSeleccionadas] = useState<Set<string>>(
    () => new Set(),
  )
  const [presupuestoAbierto, setPresupuestoAbierto] = useState(false)
  const [preview, setPreview] = useState<PreviewItem[] | null>(null)
  const [previewIdx, setPreviewIdx] = useState(0)
  const [descargando, setDescargando] = useState(false)
  const [mensajeDescarga, setMensajeDescarga] = useState<EstadoDescarga>(null)
  const [logo, setLogo] = useState<LogoPDF>(null)

  const tipologia = getTipologia(tipologiaId)
  const rubros = useMemo(() => rubrosConPorcentaje(tipologia), [tipologia])
  const estimadoCompleto = estimarMonto(precioM2, superficie)

  const factorRubros = useMemo(() => {
    if (!rubrosAbiertos || rubros.length === 0) return 1
    return rubros.reduce(
      (acc, r) => (rubrosActivos.has(r.id) ? acc + r.pct : acc),
      0,
    )
  }, [rubros, rubrosAbiertos, rubrosActivos])

  const montoObra = montoManual ? monto : estimadoCompleto
  const M = montoObra * factorRubros
  const resultado = calcularHonorario({ M, grupo, remodelacion })

  const etapasSeleccionadasInfo = resultado.etapas.filter((e) =>
    etapasSeleccionadas.has(e.id),
  )
  const montoEtapas = etapasSeleccionadasInfo.reduce((a, e) => a + e.parcial, 0)
  const pctEtapas = etapasSeleccionadasInfo.reduce(
    (a, e) => a + e.parcialPct,
    0,
  )

  useEffect(() => {
    if (!montoManual) setMonto(estimadoCompleto)
  }, [estimadoCompleto, montoManual])

  useEffect(() => {
    let activo = true
    fetch('/logo.png')
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`)
        return r.blob()
      })
      .then((blob) => {
        if (!activo) return
        if (!blob.type.startsWith('image/')) {
          throw new Error(`tipo inesperado: ${blob.type}`)
        }
        const objetoUrl = URL.createObjectURL(blob)
        const img = new Image()
        img.onload = () => {
          if (!activo) {
            URL.revokeObjectURL(objetoUrl)
            return
          }
          const max = 180
          const escala = Math.min(
            1,
            max / Math.max(img.naturalWidth, img.naturalHeight),
          )
          const ancho = Math.max(1, Math.round(img.naturalWidth * escala))
          const alto = Math.max(1, Math.round(img.naturalHeight * escala))
          const canvas = document.createElement('canvas')
          canvas.width = ancho
          canvas.height = alto
          const ctx = canvas.getContext('2d')
          if (ctx) ctx.drawImage(img, 0, 0, ancho, alto)
          URL.revokeObjectURL(objetoUrl)
          setLogo({ url: canvas.toDataURL('image/png'), formato: 'PNG' })
        }
        img.onerror = () => {
          if (activo) console.warn('No se pudo cargar la imagen del logo')
          URL.revokeObjectURL(objetoUrl)
        }
        img.src = objetoUrl
      })
      .catch((err) => {
        if (activo) console.warn('No se pudo cargar /logo.png:', err)
      })
    return () => {
      activo = false
    }
  }, [])

  function sincronizarRubros(id: string, abrir?: boolean) {
    const t = getTipologia(id)
    const idsRubros = (t.rubros ?? []).map((r) => r.id)
    setRubrosActivos(new Set(idsRubros))
    if (abrir !== undefined) setRubrosAbiertos(abrir)
    else setRubrosAbiertos(Boolean(idsRubros.length) && rubrosAbiertos)
  }

  function aplicarTipologia(id: string) {
    const t = getTipologia(id)
    localStorage.setItem('calhon:tipologia', id)
    setTipologiaId(id)
    setSuperficie(t.superficieRef)
    setPrecioM2(t.precioM2)
    setMontoManual(false)
    setMonto(t.totalObra ?? estimarMonto(t.precioM2, t.superficieRef))
    setRemodelacion(t.tipo === 'reciclaje')
    sincronizarRubros(id, Boolean(t.rubros?.length))
  }

  function onChangeTipologia(id: string) {
    aplicarTipologia(id)
  }

  function toggleRubro(id: string) {
    setRubrosActivos((prev) => {
      const next = new Set(prev)
      if (next.has(id)) next.delete(id)
      else next.add(id)
      return next
    })
  }

  function toggleTodosRubros(activar: boolean) {
    setRubrosActivos(
      activar ? new Set(rubros.map((r) => r.id)) : new Set(),
    )
  }

  function toggleEtapa(id: string) {
    setEtapasSeleccionadas((prev) => {
      const next = new Set(prev)
      if (next.has(id)) next.delete(id)
      else next.add(id)
      return next
    })
  }

  function generarPresupuesto(datos: DatosPresupuesto) {
    const fecha = new Date()
    const base = {
      datos,
      fecha,
      logo,
      M,
      rango: resultado.rango,
      grupoLabel: `${GRUPOS[grupo].label} — ${GRUPOS[grupo].descripcion}`,
      expresion: resultado.expresion,
      honorarioTotal: resultado.honorarioTotal,
      etapas: etapasSeleccionadasInfo,
      montoEtapas,
      pctEtapas,
      remodelacion: resultado.remodelacion,
      pctRemodelacion: resultado.pctRemodelacion,
      adicionalRemodelacion: resultado.adicionalRemodelacion,
    }
    function crear(version: VersionPresupuesto): PreviewItem {
      const doc = buildPresupuestoPDF({ ...base, version })
      const dataUrl = doc.output('datauristring')
      const base64 = dataUrl.slice(dataUrl.indexOf(',') + 1)
      return { url: dataUrl, base64, nombre: nombreArchivoPresupuesto(fecha, datos, etapasSeleccionadasInfo, version), version }
    }
    setPreview([crear('estudio'), crear('cliente')])
    setPreviewIdx(0)
    setMensajeDescarga(null)
    setPresupuestoAbierto(false)
  }

  async function descargarPresupuesto() {
    if (!preview) return
    const item = preview[previewIdx]
    if (!item) return
    setDescargando(true)
    setMensajeDescarga(null)
    try {
      const res = await fetch('/api/presupuesto', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nombre: item.nombre,
          contenidoBase64: item.base64,
        }),
      })
      const data = (await res.json()) as { ok: boolean; archivo?: string; error?: string }
      if (!res.ok || !data.ok) throw new Error(data.error ?? `HTTP ${res.status}`)
      setMensajeDescarga({
        tipo: 'ok',
        texto: `${data.archivo ?? item.nombre}`,
      })
    } catch (err) {
      setMensajeDescarga({
        tipo: 'error',
        texto: `no se pudo guardar: ${(err as Error).message}`,
      })
    } finally {
      setDescargando(false)
    }
  }

  function cerrarPreview() {
    setPreview(null)
    setMensajeDescarga(null)
  }

  return (
    <div className="app">
      <header className="header">
        <p className="brand">CalHon</p>
        <h1 className="title">Proyecto y dirección</h1>
        <p className="meta">
          Honorarios sugeridos CPAU · {ICC_LABEL} · K = {formatPesos(K)}
        </p>
      </header>

      <main className="main">
        <section className="inputs" aria-label="Datos de la obra">
          <div className="field">
            <label htmlFor={ids.tipologia}>Tipología Clarín ARQ</label>
            <select
              id={ids.tipologia}
              value={tipologiaId}
              onChange={(e) => onChangeTipologia(e.target.value)}
            >
              {TIPOLOGIAS.map((t) => (
                <option key={t.id} value={t.id}>
                  Modelo {t.modelo} — {t.nombre}
                  {t.tipo === 'reciclaje' ? ' (reciclaje)' : ''}
                </option>
              ))}
            </select>
            <p className="hint">{tipologia.fuente}</p>
          </div>

          <div className="row">
            <div className="field">
              <label htmlFor={ids.superficie}>Superficie (m²)</label>
              <input
                id={ids.superficie}
                type="number"
                min={0}
                step={0.01}
                value={superficie}
                onChange={(e) => {
                  setSuperficie(Number(e.target.value) || 0)
                  setMontoManual(false)
                }}
              />
            </div>
            <div className="field">
              <label htmlFor={ids.precio}>Precio / m²</label>
              <input
                id={ids.precio}
                type="number"
                min={0}
                step={1}
                value={precioM2}
                onChange={(e) => {
                  setPrecioM2(Number(e.target.value) || 0)
                  setMontoManual(false)
                }}
              />
            </div>
          </div>

          <div className="field">
            <div className="label-row">
              <label htmlFor={ids.monto}>Monto de obra M</label>
              <button
                type="button"
                className="linkish"
                onClick={() => {
                  setMontoManual(false)
                  setPrecioM2(tipologia.precioM2)
                  setMonto(estimarMonto(tipologia.precioM2, superficie))
                }}
              >
                Usar estimado · costo por m²{' '}
                {formatPesos(tipologia.precioM2)}
              </button>
            </div>
            <input
              id={ids.monto}
              type="number"
              min={0}
              step={1}
              value={Math.round(montoObra)}
              onChange={(e) => {
                setMontoManual(true)
                setMonto(Number(e.target.value) || 0)
              }}
            />
            {rubrosAbiertos && factorRubros < 1 - 1e-9 ? (
              <p className="hint">
                M considerado: {formatPesos(M)} (
                {formatPorcentaje(factorRubros)} de {formatPesos(montoObra)})
              </p>
            ) : null}
            <p className="hint">
              No incluyen IVA, honorarios profesionales, tasas ni sellados
              municipales y provinciales.
            </p>
          </div>

          <div className="field">
            <label htmlFor={ids.grupo}>Grupo de obra (Art. 3.13)</label>
            <select
              id={ids.grupo}
              value={grupo}
              onChange={(e) => setGrupo(Number(e.target.value) as GrupoObra)}
            >
              {([1, 2, 3] as GrupoObra[]).map((g) => (
                <option key={g} value={g}>
                  {GRUPOS[g].label} — {GRUPOS[g].descripcion}
                </option>
              ))}
            </select>
          </div>

          <button
            type="button"
            className={`remodelacion ${remodelacion ? 'on' : ''}`}
            onClick={() => setRemodelacion((v) => !v)}
            aria-pressed={remodelacion}
          >
            <span className="remodelacion-check" aria-hidden="true">
              {remodelacion ? '✓' : ''}
            </span>
            <span>
              <strong>Remodelación</strong>
              <span className="remodelacion-sub">
                Adicional Art. 3.18 sobre honorarios
                {remodelacion
                  ? ` · +${formatPorcentaje(REMODELACION_PCT)}`
                  : ` · +${formatPorcentaje(REMODELACION_PCT)} si se activa`}
              </span>
            </span>
          </button>
        </section>

        <section className="resultado" aria-live="polite">
          <p className="resultado-label">Honorario sugerido</p>
          <p className="resultado-monto">{formatPesos(resultado.honorarioTotal)}</p>
          <p className="resultado-detalle">
            Rango {resultado.rango} · {resultado.expresion}
            {resultado.remodelacion
              ? ` · base ${formatPesos(resultado.honorarioBase)} + ${formatPorcentaje(resultado.pctRemodelacion)} ${formatPesos(resultado.adicionalRemodelacion)}`
              : null}
          </p>

          <table className="etapas">
            <caption>Subdivisión por etapas (Art. 3.14)</caption>
            <thead>
              <tr>
                <th>Etapa</th>
                <th>Parcial</th>
                <th>Acumulado</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {resultado.etapas.map((e) => {
                const activa = etapasSeleccionadas.has(e.id)
                return (
                  <tr key={e.id} className={activa ? 'on' : ''}>
                    <td>
                      {e.nombre}
                      <span className="pct">
                        {' '}
                        ({formatPorcentaje(e.parcialPct)})
                      </span>
                    </td>
                    <td>{formatPesos(e.parcial)}</td>
                    <td>{formatPesos(e.acumulado)}</td>
                    <td className="etapa-accion">
                      <button
                        type="button"
                        className="linkish"
                        aria-pressed={activa}
                        onClick={() => toggleEtapa(e.id)}
                      >
                        {activa ? 'Quitar' : 'Usar'}
                      </button>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>

          {etapasSeleccionadasInfo.length > 0 ? (
            <div className="etapa-resumen">
              <p className="etapa-resumen-titulo">Presupuesto de la etapa</p>
              <p className="etapa-resumen-monto">
                {formatPesos(montoEtapas)}
                <span className="pct">
                  {' '}
                  ({formatPorcentaje(pctEtapas)} del honorario)
                </span>
              </p>
              <ul>
                {etapasSeleccionadasInfo.map((e) => (
                  <li key={e.id}>
                    <strong>
                      {e.nombre} ({formatPorcentaje(e.parcialPct)})
                    </strong>{' '}
                    · parcial {formatPesos(e.parcial)} · acumulado{' '}
                    {formatPesos(e.acumulado)}
                  </li>
                ))}
              </ul>
              <div className="etapa-definiciones">
                {etapasSeleccionadasInfo.map((e) => (
                  <details key={e.id}>
                    <summary>
                      {e.articulo} — {e.nombre}
                    </summary>
                    <p>{e.definicion}</p>
                  </details>
                ))}
              </div>
              <div className="etapa-acciones">
                <button
                  type="button"
                  className="btn-principal"
                  onClick={() => setPresupuestoAbierto(true)}
                >
                  Generar presupuesto
                </button>
              </div>
            </div>
          ) : null}
        </section>
      </main>

      {presupuestoAbierto ? (
        <PresupuestoModal
          onCancel={() => setPresupuestoAbierto(false)}
          onGenerar={generarPresupuesto}
        />
      ) : null}

      {preview ? (
        <PresupuestoPreview
          items={preview}
          activo={previewIdx}
          onActivo={setPreviewIdx}
          descargando={descargando}
          mensaje={mensajeDescarga}
          onDescargar={() => {
            void descargarPresupuesto()
          }}
          onCerrar={cerrarPreview}
        />
      ) : null}

      {rubros.length > 0 ? (
        <section className="rubros">
          <button
            type="button"
            className="rubros-toggle"
            onClick={() => {
              const next = !rubrosAbiertos
              setRubrosAbiertos(next)
              if (next && rubrosActivos.size === 0) {
                setRubrosActivos(new Set(rubros.map((r) => r.id)))
              }
            }}
            aria-expanded={rubrosAbiertos}
          >
            Presupuesto Clarín discriminado
            <span>{rubrosAbiertos ? '−' : '+'}</span>
          </button>
          {rubrosAbiertos ? (
            <div className="rubros-body">
              {tipologia.nota ? <p className="hint">{tipologia.nota}</p> : null}
              <p className="hint">
                Porcentajes del ejemplo Clarín aplicados al monto de obra{' '}
                {formatPesos(montoObra)}. Destildá ítems que no apliquen (p. ej.
                demoliciones ≈{' '}
                {formatPorcentajeDetalle(
                  rubros.find((r) => r.id === 'demoliciones')?.pct ?? 0,
                )}
                ).
              </p>
              <div className="rubros-actions">
                <button
                  type="button"
                  className="linkish"
                  onClick={() => toggleTodosRubros(true)}
                >
                  Marcar todos
                </button>
                <button
                  type="button"
                  className="linkish"
                  onClick={() => toggleTodosRubros(false)}
                >
                  Desmarcar todos
                </button>
              </div>
              <ul>
                {rubros.map((r) => {
                  const activo = rubrosActivos.has(r.id)
                  const escalado = escalarRubro(r.pct, montoObra)
                  return (
                    <li key={r.id} className={activo ? '' : 'off'}>
                      <label className="rubro-check">
                        <input
                          type="checkbox"
                          checked={activo}
                          onChange={() => toggleRubro(r.id)}
                        />
                        <span className="rubro-nombre">
                          {r.nombre}
                          <span className="rubro-pct">
                            {' '}
                            ({formatPorcentajeDetalle(r.pct)})
                          </span>
                        </span>
                      </label>
                      <span className="rubro-monto">
                        {activo ? formatPesos(escalado) : formatPesos(0)}
                      </span>
                    </li>
                  )
                })}
                <li className="total">
                  <span>Total considerado</span>
                  <span>{formatPesos(M)}</span>
                </li>
              </ul>
              <p className="hint">
                Referencia ejemplo: {formatNumero(tipologia.superficieRef)} m² ·
                total {formatPesos(tipologia.totalObra ?? 0)}
              </p>
            </div>
          ) : null}
        </section>
      ) : null}

      <footer className="footer">
        Valores indicativos según cuadros CPAU y modelos ARQ Clarín. El adicional
        de remodelación se aplica solo sobre honorarios. No incluyen IVA ni
        impuestos locales.
      </footer>
    </div>
  )
}

export default App
