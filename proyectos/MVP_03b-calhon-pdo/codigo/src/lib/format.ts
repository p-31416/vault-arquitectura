const arCurrency = new Intl.NumberFormat('es-AR', {
  style: 'currency',
  currency: 'ARS',
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
})

const arNumber = new Intl.NumberFormat('es-AR', {
  minimumFractionDigits: 0,
  maximumFractionDigits: 2,
})

const arPercent = new Intl.NumberFormat('es-AR', {
  style: 'percent',
  minimumFractionDigits: 0,
  maximumFractionDigits: 0,
})

export function formatPesos(value: number): string {
  return arCurrency.format(value)
}

export function formatNumero(value: number): string {
  return arNumber.format(value)
}

export function formatPorcentaje(fraction: number): string {
  return arPercent.format(fraction)
}

const arPercentDetalle = new Intl.NumberFormat('es-AR', {
  style: 'percent',
  minimumFractionDigits: 1,
  maximumFractionDigits: 1,
})

export function formatPorcentajeDetalle(fraction: number): string {
  return arPercentDetalle.format(fraction)
}

/** Parsea string con puntos de miles / coma decimal (es-AR) o número crudo */
export function parseNumeroAR(raw: string): number | null {
  const cleaned = raw.trim().replace(/\s/g, '')
  if (!cleaned) return null
  // Si tiene coma, tratar como es-AR: quitar puntos de miles, coma → punto
  if (cleaned.includes(',')) {
    const n = Number(cleaned.replace(/\./g, '').replace(',', '.'))
    return Number.isFinite(n) ? n : null
  }
  const n = Number(cleaned.replace(/\./g, ''))
  return Number.isFinite(n) ? n : null
}
