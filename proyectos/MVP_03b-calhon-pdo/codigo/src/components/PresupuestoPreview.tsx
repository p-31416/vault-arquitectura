import type { VersionPresupuesto } from '../lib/presupuesto'

export type EstadoDescarga = { tipo: 'ok' | 'error'; texto: string } | null

export type PreviewItem = {
  url: string
  base64: string
  nombre: string
  version: VersionPresupuesto
}

const ETIQUETAS: Record<VersionPresupuesto, string> = {
  estudio: 'Estudio (detallado)',
  cliente: 'Para el cliente',
}

export function PresupuestoPreview(props: {
  items: PreviewItem[]
  activo: number
  onActivo: (i: number) => void
  descargando: boolean
  mensaje: EstadoDescarga
  onDescargar: () => void
  onCerrar: () => void
}) {
  const item = props.items[props.activo]
  return (
    <div className="modal-backdrop" onClick={props.onCerrar}>
      <div className="modal modal-preview" onClick={(e) => e.stopPropagation()}>
        <h2 className="modal-title">Vista previa del presupuesto</h2>
        <p className="modal-sub">
          {item.nombre} — verificá el contenido antes de guardarlo en la carpeta.
        </p>
        <div className="preview-tabs" role="tablist">
          {props.items.map((it, i) => (
            <button
              key={it.version}
              type="button"
              role="tab"
              aria-selected={i === props.activo}
              className={`preview-tab ${i === props.activo ? 'on' : ''}`}
              onClick={() => props.onActivo(i)}
            >
              {ETIQUETAS[it.version]}
            </button>
          ))}
        </div>
        <div className="pdf-preview">
          <iframe
            key={item.version}
            title="Vista previa del presupuesto"
            src={item.url}
          />
        </div>
        {props.mensaje ? (
          <p className={`preview-mensaje ${props.mensaje.tipo}`} role="status">
            {props.mensaje.tipo === 'ok' ? 'Guardado: ' : 'Error: '}
            {props.mensaje.texto}
          </p>
        ) : null}
        <div className="modal-actions">
          <button
            type="button"
            className="linkish"
            onClick={props.onCerrar}
            disabled={props.descargando}
          >
            Cerrar
          </button>
          <button
            type="button"
            className="btn-principal"
            onClick={props.onDescargar}
            disabled={props.descargando}
          >
            {props.descargando
              ? 'Guardando…'
              : `Guardar en carpeta (${ETIQUETAS[item.version].toLowerCase()})`}
          </button>
        </div>
      </div>
    </div>
  )
}
