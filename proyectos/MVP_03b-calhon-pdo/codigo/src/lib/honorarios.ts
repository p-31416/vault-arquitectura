import {
  ETAPAS,
  GRUPOS,
  K,
  REMODELACION_PCT,
  rangoMonto,
  type GrupoObra,
  type RangoMonto,
} from '../data/cpau'

export type ResultadoHonorario = {
  M: number
  K: number
  grupo: GrupoObra
  rango: RangoMonto
  honorarioBase: number
  remodelacion: boolean
  pctRemodelacion: number
  adicionalRemodelacion: number
  honorarioTotal: number
  expresion: string
  etapas: {
    id: string
    indice: number
    nombre: string
    articulo: string
    definicion: string
    definicionCliente?: string
    parcialPct: number
    acumuladoPct: number
    parcial: number
    acumulado: number
  }[]
}

export function calcularHonorario(params: {
  M: number
  grupo: GrupoObra
  remodelacion: boolean
  k?: number
}): ResultadoHonorario {
  const k = params.k ?? K
  const M = Math.max(0, params.M)
  const rango = rangoMonto(M, k)
  const { coefM, coefK } = GRUPOS[params.grupo].coefs[rango]
  const honorarioBase = coefM * M + coefK * k

  // +40% solo sobre honorarios (el $/m² de reciclaje ya contempla la obra)
  const pctRemodelacion = params.remodelacion ? REMODELACION_PCT : 0
  const adicionalRemodelacion = honorarioBase * pctRemodelacion
  const honorarioTotal = honorarioBase + adicionalRemodelacion

  const expresion =
    coefK === 0
      ? `${coefM} × M`
      : `${coefM} × M + ${coefK} × K`

  const etapas = ETAPAS.map((e, i) => ({
    id: e.id,
    indice: i + 1,
    nombre: e.nombre,
    articulo: e.articulo,
    definicion: e.definicion,
    definicionCliente: e.definicionCliente,
    parcialPct: e.parcial,
    acumuladoPct: e.acumulado,
    parcial: honorarioTotal * e.parcial,
    acumulado: honorarioTotal * e.acumulado,
  }))

  return {
    M,
    K: k,
    grupo: params.grupo,
    rango,
    honorarioBase,
    remodelacion: params.remodelacion,
    pctRemodelacion,
    adicionalRemodelacion,
    honorarioTotal,
    expresion,
    etapas,
  }
}

export function estimarMonto(precioM2: number, superficie: number): number {
  return Math.max(0, precioM2) * Math.max(0, superficie)
}
