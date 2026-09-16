/** Índice CPAU — ICC junio 2026 */
export const K = 640_069_857.62

export const ICC_LABEL = 'ICC junio 2026'

export type RangoMonto = 'A' | 'B' | 'C' | 'D'

export type GrupoObra = 1 | 2 | 3

/** Coeficientes Cuadro 5: honorario = coefM * M + coefK * K (coefK=0 en rango A) */
export type CoefRango = { coefM: number; coefK: number }

export const GRUPOS: Record<
  GrupoObra,
  { label: string; descripcion: string; coefs: Record<RangoMonto, CoefRango> }
> = {
  1: {
    label: 'Grupo 1',
    descripcion: 'Edificios en general',
    coefs: {
      A: { coefM: 0.14, coefK: 0 },
      B: { coefM: 0.08, coefK: 0.03 },
      C: { coefM: 0.06, coefK: 0.13 },
      D: { coefM: 0.04, coefK: 0.63 },
    },
  },
  2: {
    label: 'Grupo 2',
    descripcion: 'Arquitectura efímera, monumentos y funeraria',
    coefs: {
      A: { coefM: 0.17, coefK: 0 },
      B: { coefM: 0.1, coefK: 0.035 },
      C: { coefM: 0.04, coefK: 0.335 },
      D: { coefM: 0.04, coefK: 0.335 },
    },
  },
  3: {
    label: 'Grupo 3',
    descripcion: 'Planificación del paisaje y diseño de interiores',
    coefs: {
      A: { coefM: 0.2, coefK: 0 },
      B: { coefM: 0.1, coefK: 0.05 },
      C: { coefM: 0.03, coefK: 0.4 },
      D: { coefM: 0.03, coefK: 0.4 },
    },
  },
}

/** Adicional Art. 3.18 — obras de refacción / remodelación (sobre honorarios) */
export const REMODELACION_PCT = 0.4

export type Etapa = {
  id: string
  nombre: string
  parcial: number
  acumulado: number
  /** Artículo del arancel CPAU que define la etapa */
  articulo: string
  /** Definición CPAU para aclaración al comitente */
  definicion: string
  /** Versión resumida para el presupuesto al cliente */
  definicionCliente?: string
}

/** Art. 3.14 — subdivisión de honorarios (Cuadro 6) con definiciones del arancel */
export const ETAPAS: Etapa[] = [
  {
    id: 'croquis-preliminares',
    nombre: 'Croquis preliminares',
    parcial: 0.07,
    acumulado: 0.07,
    articulo: 'Art. 3.8',
    definicion:
      'Conjunto de planos y escritos que el profesional confecciona como preliminar interpretación del programa convenido con el comitente: esquemas de plantas, cortes o volúmenes, planos esquemáticos básicos de la estructura, perspectiva esquemática y memoria descriptiva con estimación de superficies y monto tentativo de la obra.',
    definicionCliente:
      'Conjunto de planos esquemáticos de arquitectura como preliminar interpretación del programa convenido.',
  },
  {
    id: 'croquis-avanzados',
    nombre: 'Croquis avanzados',
    parcial: 0.08,
    acumulado: 0.15,
    articulo: 'Art. 3.8',
    definicion:
      'Segunda fase de los croquis preliminares, previo acuerdo de las partes, que se ajusta a las mismas condiciones e incorpora planos esquemáticos completos de la estructura y de las instalaciones, que comprenden la idea general de sus proyectos.',
    definicionCliente:
      'Planos de arquitectura con equipamiento, planos esquemáticos completos de instalaciones (sanit./elect.), estructura, volumetrías (3D) esquemáticas y memoria descriptiva (detalles/notas), siempre bajo el cumplimiento de los reglamentos vigentes.',
  },
  {
    id: 'anteproyecto',
    nombre: 'Anteproyecto',
    parcial: 0.05,
    acumulado: 0.2,
    articulo: 'Art. 3.9',
    definicion:
      'Conjunto de planos y escritos necesarios para dar una idea general de la obra en estudio: plano de implantación, todas las plantas, elevaciones y cortes acotados, planos esquemáticos de estructura e instalaciones, cómputo de superficies y presupuesto global estimativo, memoria descriptiva y perspectiva.',
  },
  {
    id: 'anteproyecto-avanzado',
    nombre: 'Anteproyecto avanzado',
    parcial: 0.2,
    acumulado: 0.4,
    articulo: 'Art. 3.9',
    definicion:
      'Profundización del anteproyecto: exhibe el partido adoptado, los lineamientos de los sistemas constructivos y describe las terminaciones interiores y exteriores, preparando la documentación de proyecto.',
  },
  {
    id: 'documentacion',
    nombre: 'Documentación de proyecto',
    parcial: 0.2,
    acumulado: 0.6,
    articulo: 'Art. 3.10',
    definicion:
      'Conjunto de elementos gráficos y escritos que definen con precisión el carácter y finalidad de la obra y permiten su construcción bajo la dirección de un profesional: planos generales y de replanteo, documentación de estructura e instalaciones, planilla de carpinterías, detalles constructivos, pliego de especificaciones técnicas, presupuesto desagregado por rubros, bases de licitación y memoria de proyecto.',
  },
  {
    id: 'direccion',
    nombre: 'Dirección de obra',
    parcial: 0.4,
    acumulado: 1,
    articulo: 'Art. 3.11',
    definicion:
      'Función del profesional durante la construcción de la obra: preparar el llamado a licitación, estudiar las propuestas, revisar y aprobar los planos de ejecución del constructor, controlar la fiel interpretación del proyecto, revisar liquidaciones y extender certificados, y asesorar al comitente sobre aspectos técnicos de la obra.',
  },
]

export function rangoMonto(M: number, k: number = K): RangoMonto {
  if (M <= 0.5 * k) return 'A'
  if (M <= 5 * k) return 'B'
  if (M <= 25 * k) return 'C'
  return 'D'
}

export function limitesRango(k: number = K) {
  return {
    A: { hasta: 0.5 * k },
    B: { desde: 0.5 * k, hasta: 5 * k },
    C: { desde: 5 * k, hasta: 25 * k },
    D: { desde: 25 * k },
  }
}
