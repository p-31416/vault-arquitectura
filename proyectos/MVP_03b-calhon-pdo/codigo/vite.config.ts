import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { savePresupuesto } from './plugins/savePresupuesto.js'

const presupuestosDir = fileURLToPath(new URL('../presupuestos/', import.meta.url))

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), savePresupuesto(presupuestosDir)],
})
