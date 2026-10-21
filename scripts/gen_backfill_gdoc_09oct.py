"""Genera el SDK-TS del workflow backfill GDoc 09/10 (3 reuniones PPI -> Google Docs).

Lee los 3 .md de raw/reuniones + el jsCode del nodo Build del Core,
y emite el codigo SDK listo para validate/create via MCP n8n.
Uso: comfyenv python.exe scripts/gen_backfill_gdoc_09oct.py
Sale: Temp/opencode/backfill-gdoc-09oct.ts
"""
import json
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
RAW = VAULT / "raw" / "reuniones"
TMP = Path(r"C:\Users\Solch16\AppData\Local\Temp\opencode")
CORE = json.loads((TMP / "n8n-fathom-core.json").read_text(encoding="utf-8-sig"))
CORE = json.loads(CORE["result"]["content"][0]["text"])["workflow"]
BUILD_JS = next(n for n in CORE["nodes"] if n["name"] == "Build Google Docs Requests")["parameters"]["jsCode"]

FILES = [
    "2026-10-09_emilia-proyectopi_191472132.md",
    "2026-10-09_emilia-proyectopi_191509492.md",
    "2026-10-09_emilia-proyectopi_191524949.md",
]
FOLDER = "1n5mkPNdHhgFEsYfLmx3LYD4sIUiHDtcQ"  # Reuniones-Internas

docs = [{"fileName": f, "folderId": FOLDER, "document": (RAW / f).read_text(encoding="utf-8")} for f in FILES]

BACKFILL_JS = (
    "const ITEMS = " + json.dumps(docs, ensure_ascii=False) + ";\n"
    "const out = [];\n"
    "for (const d of ITEMS) {\n"
    "  const cut = d.document.indexOf('## Transcripcion');\n"
    "  const summary = cut > 0 ? d.document.slice(0, cut) : d.document;\n"
    "  out.push({ json: { fileName: d.fileName, folderId: d.folderId,"
    " summaryDocument: summary, document: d.document } });\n"
    "}\n"
    "return out;"
)

TS = """import { workflow, node, trigger, expr, newCredential } from '@n8n/workflow-sdk';

const manual = trigger({
  type: 'n8n-nodes-base.manualTrigger',
  version: 1,
  config: { name: 'Manual Trigger', position: [240, 300] }
});

const backfill = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: { name: 'Backfill Items', parameters: { jsCode: ___BACKFILL___ }, position: [460, 300] }
});

const buildReq = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: { name: 'Build Doc Requests', parameters: { jsCode: ___BUILD___ }, position: [680, 300] }
});

const createDoc = node({
  type: 'n8n-nodes-base.googleDocs',
  version: 2,
  config: {
    name: 'Create Google Doc',
    parameters: {
      folderId: expr("{{ $('Backfill Items').item.json.folderId }}"),
      title: expr("{{ $('Backfill Items').item.json.fileName.replace(/\\.md$/, '') }}")
    },
    credentials: { googleDocsOAuth2Api: newCredential('Google Docs account') },
    position: [900, 300]
  }
});

const moveDoc = node({
  type: 'n8n-nodes-base.googleDrive',
  version: 3,
  config: {
    name: 'Move Google Doc to Folder',
    parameters: {
      operation: 'move',
      fileId: expr("{{ { __rl: true, mode: 'id', value: $json.id, cachedResultName: 'Google Doc' } }}"),
      driveId: expr("{{ { __rl: true, mode: 'id', value: 'My Drive', cachedResultName: 'My Drive' } }}"),
      folderId: expr("{{ { __rl: true, mode: 'id', value: $('Backfill Items').item.json.folderId, cachedResultName: 'Reuniones-Internas' } }}")
    },
    credentials: { googleDriveOAuth2Api: newCredential('ppi-EmiliaOS_Google Drive account') },
    position: [1120, 300]
  }
});

const applyFmt = node({
  type: 'n8n-nodes-base.httpRequest',
  version: 4.5,
  config: {
    name: 'Apply Google Docs Formatting',
    parameters: {
      method: 'POST',
      url: '=https://docs.googleapis.com/v1/documents/{{ $json.id }}:batchUpdate',
      authentication: 'predefinedCredentialType',
      nodeCredentialType: 'googleDocsOAuth2Api',
      sendBody: true,
      specifyBody: 'json',
      jsonBody: expr("{{ JSON.stringify($('Backfill Items').item.json.batchUpdate) }}"),
      options: {}
    },
    credentials: { googleDocsOAuth2Api: newCredential('Google Docs account') },
    position: [1340, 300]
  }
});

export default workflow('backfill-gdoc-09-10', 'OS-Emilia - GDoc Backfill 09-10')
  .add(manual)
  .to(backfill)
  .to(buildReq)
  .to(createDoc)
  .to(moveDoc)
  .to(applyFmt);
"""

TS = TS.replace("___BACKFILL___", json.dumps(BACKFILL_JS)).replace("___BUILD___", json.dumps(BUILD_JS))
out = TMP / "backfill-gdoc-09oct.ts"
out.write_text(TS, encoding="utf-8")
print("TS chars:", len(TS))
