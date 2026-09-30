# Notas — pegar firma escaneada en el PDF

## ¿Se puede pegar la firma escaneada en el PDF? Sí.

- **Técnicamente:** sí. El script `insertar_firma_contrato.py` pega tu PNG transparente encima del bloque "Firma Prestadora" en la última página (A4, ~18mm margen izq, 42mm desde abajo, 48mm ancho).
- **Legalmente:** tu contrato ya habilita `Firma escaneada simple válida` (`wiki/legal/contrato-servicios-studio-os.md:44`). Pegar la firma rinde como **firma electrónica simple** (Ley 25.506 art.5). No es **firma digital con certificado** (art.2 con token), pero para este programa I+D entre dos partes alcanza — sobre todo si queda trail por mail.

### Qué hacer para que quede blindada

1. **Escanear bien:** firma con birome negra en hoja blanca lisa, foto/scan 300 dpi, recortar a `activos/firmas/sol_firma.png` con fondo transparente (usar remove.bg o Photoshop → PNG).
2. **Pegar solo la tuya:** generás `contrato-studio-os-emilia_firmado-sol.pdf` y se lo mandás a Emilia. Ella imprime/firma o pega la suya y devuelve `..._firmado-ambas.pdf`. Queda evidencia de ida y vuelta por mail (QUINTA: mails válidos).
3. **Enviar por mail con texto:** "Adjunto contrato firmado por mí el 24/09 — queda a tu firma y devolución por este mismo mail" — eso + PDF con imagen ya es prueba de conformidad + fecha.

### Si Emilia quiere más traza

Subir ese mismo PDF a **DocuSeal** (`docusealco/docuseal` — `docker run -p 3000:3000 docuseal/docuseal`) que guarda audit log + hash + IP. No hace falta para firmar hoy.

### Comandos

```bash
# 1) Guardá tu firma en activos/firmas/sol_firma.png (PNG transparente)

# 2) Generá PDF con tu firma pegada
P:\Anaconda\envs\comfyenv\python.exe scripts/insertar_firma_contrato.py --firma activos/firmas/sol_firma.png

# 3) Resultado
# proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia_firmado-sol.pdf
# Ese se lo mandás a Emilia para su firma.
```

### Dependencias

```bash
pip install pypdf reportlab pillow
```

Si el PDF no carga en algún visor, avisar — ajustamos x/y/w en `crear_overlay()`.
