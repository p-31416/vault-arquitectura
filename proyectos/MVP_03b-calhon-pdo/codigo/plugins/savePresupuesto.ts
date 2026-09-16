import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { resolve } from 'node:path'
import type { Connect, Plugin } from 'vite'

type BodyPresupuesto = {
  nombre?: unknown
  contenidoBase64?: unknown
}

function nombreUnico(dir: string, base: string): Promise<string> {
  const stem = base.replace(/\.pdf$/i, '')
  return (async () => {
    for (let i = 1; ; i++) {
      const candidato = i === 1 ? `${stem}.pdf` : `${stem}_${i}.pdf`
      try {
        await readFile(resolve(dir, candidato))
      } catch {
        return resolve(dir, candidato)
      }
    }
  })()
}

/**
 * ADR 0006 — Guarda los presupuestos generados en una carpeta del repo.
 * El navegador no puede escribir en el disco, así que el dev server recibe
 * el PDF (base64) por POST y lo escribe en `outDir`.
 */
export function savePresupuesto(outDir: string): Plugin {
  return {
    name: 'save-presupuesto',
    configureServer(server) {
      server.middlewares.use(
        '/api/presupuesto',
        (req: Connect.IncomingMessage, res) => {
          if (req.method !== 'POST') {
            res.statusCode = 405
            res.end('Method not allowed')
            return
          }

          const chunks: Uint8Array[] = []
          req.on('data', (chunk) => chunks.push(chunk as Uint8Array))
          req.on('end', () => {
            void (async () => {
              try {
                const raw = Buffer.concat(chunks).toString('utf8')
                const body = JSON.parse(raw) as BodyPresupuesto
                const nombre = String(body?.nombre ?? 'presupuesto')
                const base64 = String(body?.contenidoBase64 ?? '')
                if (!base64) throw new Error('Falta contenidoBase64')
                const buffer = Buffer.from(base64, 'base64')
                await mkdir(outDir, { recursive: true })
                const ruta = await nombreUnico(outDir, nombre)
                await writeFile(ruta, buffer)
                res.setHeader('Content-Type', 'application/json; charset=utf-8')
                res.end(JSON.stringify({ ok: true, archivo: ruta }))
              } catch (err) {
                res.statusCode = 500
                res.setHeader('Content-Type', 'application/json; charset=utf-8')
                res.end(
                  JSON.stringify({
                    ok: false,
                    error: String((err as Error)?.message ?? err),
                  }),
                )
              }
            })()
          })
        },
      )
    },
  }
}
