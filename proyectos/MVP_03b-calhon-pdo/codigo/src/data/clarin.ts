export type RubroClarin = {
  id: string
  nombre: string
  monto: number
}

export type RubroConPct = RubroClarin & {
  /** Participación sobre el total del ejemplo Clarín */
  pct: number
}

export type TipologiaClarin = {
  id: string
  modelo: number
  nombre: string
  /** obra nueva vs reciclaje/remodelación */
  tipo: 'obra-nueva' | 'reciclaje'
  precioM2: number
  superficieRef: number
  fuente: string
  rubros?: RubroClarin[]
  totalObra?: number
  nota?: string
}

/** Tipologías Clarín ARQ — resumen junio 2026 + Modelo 11 del PDF local */
export const TIPOLOGIAS: TipologiaClarin[] = [
  {
    id: 'modelo-2-country',
    modelo: 2,
    nombre: 'Vivienda Country',
    tipo: 'obra-nueva',
    precioM2: 2_876_571,
    superficieRef: 182.8,
    fuente: 'Clarín ARQ · resumen junio 2026',
  },
  {
    id: 'modelo-5-ph',
    modelo: 5,
    nombre: 'PH Moderno',
    tipo: 'obra-nueva',
    precioM2: 2_264_375,
    superficieRef: 943,
    fuente: 'Clarín ARQ · resumen junio 2026',
  },
  {
    id: 'modelo-6-altura',
    modelo: 6,
    nombre: 'Vivienda en Altura',
    tipo: 'obra-nueva',
    precioM2: 2_651_210,
    superficieRef: 1_503.78,
    fuente: 'Clarín ARQ · resumen junio 2026',
  },
  {
    id: 'modelo-11-reciclaje',
    modelo: 11,
    nombre: 'Reciclaje casa chorizo',
    tipo: 'reciclaje',
    precioM2: 2_831_639,
    superficieRef: 220,
    fuente: 'Clarín ARQ · PDF kiosco (Modelo 11)',
    totalObra: 649_602_458,
    nota: 'Demolición parcial y reforma; baño y cocina reubicados; segundo piso en etapa posterior.',
    rubros: [
      { id: 'demoliciones', nombre: 'Demoliciones', monto: 232_114_389 },
      { id: 'mamposteria', nombre: 'Mampostería', monto: 23_014_398 },
      { id: 'carpinterias', nombre: 'Carpinterías', monto: 5_848_808 },
      { id: 'estructuras', nombre: 'Estructuras', monto: 51_978_385 },
      { id: 'revoques', nombre: 'Revoques', monto: 42_881_022 },
      { id: 'carp-contrap', nombre: 'Carp. y contrap.', monto: 3_627_785 },
      { id: 'pisos', nombre: 'Pisos y zócalos', monto: 64_835_070 },
      { id: 'revestimientos', nombre: 'Revestimientos', monto: 6_781_114 },
      { id: 'cielorrasos', nombre: 'Cielorrasos', monto: 9_648_124 },
      { id: 'cubierta', nombre: 'Cubierta', monto: 30_274_931 },
      { id: 'sanitaria', nombre: 'Instal. sanitaria', monto: 25_512_648 },
      { id: 'gas', nombre: 'Inst. de gas', monto: 3_110_522 },
      { id: 'electrica', nombre: 'Inst. eléctrica', monto: 26_975_650 },
      { id: 'pinturas', nombre: 'Pinturas', monto: 27_049_468 },
      { id: 'mesadas', nombre: 'Mesadas y mueb.', monto: 4_924_089 },
      { id: 'limpieza', nombre: 'Limpieza de obra', monto: 14_973_660 },
      { id: 'gastos', nombre: 'Gastos de obra', monto: 9_418_420 },
      { id: 'beneficio', nombre: 'Beneficio', monto: 66_633_976 },
    ],
  },
]

export const TIPOLOGIA_OBRA_NUEVA_DEFAULT = 'modelo-5-ph'
export const TIPOLOGIA_RECICLAJE_DEFAULT = 'modelo-11-reciclaje'

export function getTipologia(id: string): TipologiaClarin {
  const t = TIPOLOGIAS.find((x) => x.id === id)
  if (!t) throw new Error(`Tipología desconocida: ${id}`)
  return t
}

export function totalRubros(tipologia: TipologiaClarin): number {
  if (tipologia.totalObra != null) return tipologia.totalObra
  return (tipologia.rubros ?? []).reduce((a, r) => a + r.monto, 0)
}

/** Rubros del ejemplo Clarín con % sobre el total de referencia */
export function rubrosConPorcentaje(tipologia: TipologiaClarin): RubroConPct[] {
  const rubros = tipologia.rubros
  if (!rubros?.length) return []
  const total = totalRubros(tipologia)
  if (total <= 0) return rubros.map((r) => ({ ...r, pct: 0 }))
  return rubros.map((r) => ({ ...r, pct: r.monto / total }))
}

/** Escala un rubro al monto de obra considerado (precio/m² × superficie) */
export function escalarRubro(pct: number, montoBase: number): number {
  return pct * Math.max(0, montoBase)
}
