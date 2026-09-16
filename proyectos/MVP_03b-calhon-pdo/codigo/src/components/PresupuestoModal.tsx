import { useState, type FormEvent } from 'react'

export type DatosPresupuesto = {
  nombre: string
  direccion: string
  cliente: string
}

export function PresupuestoModal(props: {
  onCancel: () => void
  onGenerar: (datos: DatosPresupuesto) => void
}) {
  const [nombre, setNombre] = useState('')
  const [direccion, setDireccion] = useState('')
  const [cliente, setCliente] = useState('')

  function onSubmit(e: FormEvent) {
    e.preventDefault()
    props.onGenerar({
      nombre: nombre.trim(),
      direccion: direccion.trim(),
      cliente: cliente.trim(),
    })
  }

  return (
    <div className="modal-backdrop" onClick={props.onCancel}>
      <form
        className="modal"
        onSubmit={onSubmit}
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="modal-title">Generar presupuesto</h2>
        <p className="modal-sub">
          Datos para identificar la obra y el cliente en el PDF.
        </p>
        <label className="modal-field">
          <span>Nombre de la obra</span>
          <input
            autoFocus
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            placeholder="Ej. Casa en Pilar"
          />
        </label>
        <label className="modal-field">
          <span>Dirección</span>
          <input
            value={direccion}
            onChange={(e) => setDireccion(e.target.value)}
            placeholder="Ej. Av. del Libertador 1234"
          />
        </label>
        <label className="modal-field">
          <span>Apellido del cliente</span>
          <input
            value={cliente}
            onChange={(e) => setCliente(e.target.value)}
            placeholder="Ej. García"
          />
        </label>
        <div className="modal-actions">
          <button type="button" className="linkish" onClick={props.onCancel}>
            Cancelar
          </button>
          <button type="submit" className="modal-submit">
            Generar PDF
          </button>
        </div>
      </form>
    </div>
  )
}
