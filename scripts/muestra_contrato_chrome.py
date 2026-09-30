# NOTA ES: Muestra A — HTML+CSS -> Chrome headless PDF
# Qué hace: toma temp/muestras-pdf/contrato-muestra.html y genera contrato-muestra-chrome.pdf via chrome --headless --print-to-pdf
# Por qué: WeasyPrint falló por falta de GTK libgobject-2.0-0 en Windows; Chrome hace el mismo trabajo HTML->PDF sin dependencias extra
# Uso: P:\Anaconda\envs\comfyenv\python.exe scripts/muestra_contrato_chrome.py
import subprocess, pathlib
html = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\temp\muestras-pdf\contrato-muestra.html")
pdf = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\temp\muestras-pdf\contrato-muestra-chrome.pdf")
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# NOTA ES: --no-pdf-header-footer evita fecha/URL automáticos; --run-all-compositor-stages-before-draw espera CSS
cmd = [chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw", f"--print-to-pdf={pdf}", str(html)]
print("CMD:", " ".join(cmd))
r = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", r.stdout[:500])
print("STDERR:", r.stderr[:1000])
print("PDF existe:", pdf.exists(), "bytes:", pdf.stat().st_size if pdf.exists() else 0)
