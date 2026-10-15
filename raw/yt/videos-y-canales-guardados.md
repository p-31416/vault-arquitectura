---
tipo: raw-cola
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [yt, takeout, watch-later, playlists, canales, revision, hitl]
---

# Videos y canales guardados — YouTube + Chrome

> Documento unico de curacion generado desde Google Takeout (2026-10-08).
> **Parte A**: todos los videos que tenes guardados, agrupados por tu carpeta/listado, con link directo.
> **Parte B**: los canales que quedaron fuera del scope del estudio, para que revises si los sumar o descartar.

Regenerar con: `scripts/yt_takeout_parser.py`

## Resumen

| Metrica                                              | Cantidad |
| ---------------------------------------------------- | -------- |
| Videos en Watch Later                                | 259      |
| Videos en listas tematicas                           | 450      |
| Videos que estan en Watch Later Y en alguna tematica | 14       |
| Canales suscritos totales                            | 157      |
| Canales en scope                                     | 91       |
| Canales fuera de scope (Parte B)                     | 66       |

### Top tags en tus videos

Tags especificos (lo fino). Para lo grueso, ver Por categoria amplia abajo.

| Tag | Videos |
|---|---|
| `llm` | 208 |
| `arq` | 120 |
| `n8n` | 90 |
| `comfyui` | 80 |
| `otros` | 65 |
| `rhino` | 47 |
| `vibe-coding` | 44 |
| `agents` | 42 |
| `autocad` | 35 |
| `nanobanana` | 26 |
| `viz` | 26 |
| `charlas` | 24 |
| `twinmotion` | 21 |
| `metaverso` | 16 |
| `grasshopper` | 16 |
| `parametrico` | 15 |
| `filosofia` | 14 |
| `blender` | 14 |
| `planos` | 13 |
| `descartado` | 12 |

### Por categoria amplia

| Categoria         | Videos | Que incluye                                                                                         |
| ----------------- | ------ | --------------------------------------------------------------------------------------------------- |
| `ia-agentes-code` | 401    | `llm`, `agents`, `vibe-coding`, `opencode`, `n8n`, `whatsapp`, `repos`                              |
| `diseno-arq`      | 209    | `viz`, `dibujo`, `planos`, `interior`, `parametrico`, `sostenibilidad`, `metaverso`, `nft`          |
| `software-arq`    | 160    | `rhino`, `grasshopper`, `revit`, `autocad`, `twinmotion`, `unreal`, `blender`, `freecad`            |
| `ia-imagen`       | 133    | `comfyui`, `stable-diffusion`, `midjourney`, `nanobanana`, `flux`, `upscaling`, `magnific`, `ai-3d` |
| `(sin categoria)` | 116    |                                                                                                     |
| `gestion`         | 25     | `marketing`, `gestion`, `notebook`, `hardware`                                                      |
| `construccion`    | 19     | `3d-print`, `concreto`, `modular`, `aislamiento`, `madera`                                          |
| `ia-video-audio`  | 13     | `video-ia`, `audio-ia`, `remotion`                                                                  |

---

## Parte A — Videos guardados

Cada seccion es una de tus listas de YouTube. Los links van directo al video.
Columnas: **Tags** = tema fino (ej `comfyui`, `rhino`); **Cat** = categoria
amplia (ej `ia-imagen`, `software-arq`) para filtrar rapido; **En WL** = si
ademas esta en Watch Later.

> Titulos, canal y duracion traidos con la YouTube Data API v3
> (cache en `raw/yt/cache-titulos.json`, generado por `scripts/yt_titles.py`).

### Indice de listas

- [[#0. Watch Later]] — 259 videos
- [[#ARQ/3D-Print]] — 34 videos
- [[#ARQ/AutoCAD2D]] — 40 videos
- [[#ARQ/docs]] — 24 videos
- [[#ARQ/IA]] — 32 videos
- [[#ARQ/Rhino+Grasshopper]] — 31 videos
- [[#ARQ/Twinmotion-Unreal_Engine]] — 21 videos
- [[#IA/Metaverso-VR/AR]] — 9 videos
- [[#libros]] — 6 videos
- [[#🛒MKT📈SEM/SEO]] — 2 videos
- [[#IA/🧩Vibe_Coding]] — 18 videos
- [[#IA/🤖gen_Agents]] — 23 videos
- [[#IA/🧠gen_Txt (LLMs)]] — 30 videos
- [[#IA/⚙️Workflows(Autom.)]] — 91 videos
- [[#IA/🎨gen_Img]] — 71 videos
- [[#IA/🎬gen_Vid]] — 18 videos

---

### 0. Watch Later

Tu cola general de videos para ver. 259 videos, ordenados por fecha de agregado (mas nuevo primero).

| #   | Titulo                                                                                                | Canal                                       | Dur      | Fecha      | Tags                                   | Cat             | Link                                        |
| --- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------- | -------- | ---------- | -------------------------------------- | --------------- | ------------------------------------------- |
| 1   | DeepSeek acaba de lanzar su APP de Agente IA: Hace TODO GRATIS 🔥                                     | Alejavi Rivera                              | 24:09    | 2026-10-08 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=TCTV0ggcQCI |
| 2   | Gemini Nano Banana 2.1 in ComfyUI: 4K Output, 14 References & Multi-Turn Editing                      | ComfyUI                                     | 0:35     | 2026-10-07 | comfyui, nanobanana, llm               | ia-imagen       | https://www.youtube.com/watch?v=JWln_5jm4Ic |
| 3   | Model Jam: Latest Image & Video Model Releases                                                        | ComfyUI                                     | 55:07    | 2026-10-07 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=7V7Aazicx-s |
| 4   | Beyond the 3D Box with Rhino \| S2 E4 \| Rhino Studio Series                                          | Rhino 3D (Rhinoceros3d official)            | 20:00    | 2026-10-07 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=3DigELY2Zus |
| 5   | Generate Residential Floor Plans directly in the Browser!                                             | PlanFinder                                  | 0:39     | 2026-10-07 | planos                                 | diseno-arq      | https://www.youtube.com/watch?v=xx94B4Pw-to |
| 6   | Forget Suno. New BEST local AI music generator is here!                                               | AI Search                                   | 24:37    | 2026-10-05 | audio-ia                               | ia-video-audio  | https://www.youtube.com/watch?v=9RtywbN--QE |
| 7   | All 7 Dimensions Explained in Detail (From 0D to Infinity)                                            | Ridddle                                     | 14:13    | 2026-10-05 | otros                                  |                 | https://www.youtube.com/watch?v=-gPFxMHWV8w |
| 8   | Sharon Stone Saw the Afterlife: 5 Alien Orbs Told Her to Stay & Share Their Message                   | Dr. Mayim Bialik                            | 1:52:48  | 2026-10-03 | otros                                  |                 | https://www.youtube.com/watch?v=7hsvA4-zWAI |
| 9   | LAO TZU: El Arte de "Hacer que te Deseen" Sin Perseguir a Nadie (La Ley del Imán Inverso)             | Legado de los Maestros                      | 2:11:59  | 2026-10-01 | filosofia                              |                 | https://www.youtube.com/watch?v=b4byMoRGSk4 |
| 10  | Comfy Agent: The AI Agent That Builds ComfyUI Workflows for You                                       | ComfyUI                                     | 0:46     | 2026-10-01 | comfyui, agents                        | ia-imagen       | https://www.youtube.com/watch?v=QfvwVfKtpQ4 |
| 11  | 3D Massing Iterations with Rhino \| S2 E3 \| Rhino Studio Series                                      | Rhino 3D (Rhinoceros3d official)            | 20:55    | 2026-09-30 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=Fu1JUMR_oLY |
| 12  | Tu bot de WhatsApp cobra cada respuesta desde el 1/10: qué hacer hoy #shorts                          | Nicolas Dubois                              | 0:50     | 2026-09-29 | llm, whatsapp                          | ia-agentes-code | https://www.youtube.com/watch?v=42hysJoTTSA |
| 13  | Probé GPT-6 Astra en 3ds Max: no es lo que te están vendiendo                                         | Adán Martín                                 | 44:55    | 2026-09-29 | 3dsmax, llm                            | software-arq    | https://www.youtube.com/watch?v=WlbDZadAYmo |
| 14  | Comfy Agent: Live Art Build, VFX & Product Marketing                                                  | ComfyUI                                     | 1:12:30  | 2026-09-27 | comfyui, agents, marketing             | ia-imagen       | https://www.youtube.com/watch?v=gDRn8k3-mDA |
| 15  | Comfy Router is live                                                                                  | ComfyUI                                     | 0:47     | 2026-09-25 | comfyui, hardware                      | ia-imagen       | https://www.youtube.com/watch?v=SIkcEyl2MRw |
| 16  | Interactive door in Twinmotion 2026.2!  #twinmotionguru #twinmotionmasterclass                        | Twinmotion Guru                             | 1:10     | 2026-09-25 | twinmotion                             | software-arq    | https://www.youtube.com/watch?v=RO1_DjLj_yU |
| 17  | ComfyUI for Animation: Keyframe Exploration at Any Camera Angle (GPT Image 2)                         | ComfyUI                                     | 0:57     | 2026-09-25 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=6Jzr81R7sE4 |
| 18  | This ComfyUI workflow uses a Blender video to define the camera movement and perspective              | ComfyUI                                     | 0:09     | 2026-09-23 | blender, comfyui                       | software-arq    | https://www.youtube.com/watch?v=WFHlgwl6jno |
| 19  | Comfy Router: One API for Frontier Image & Video Models                                               | ComfyUI                                     | 0:47     | 2026-09-23 | comfyui, hardware                      | ia-imagen       | https://www.youtube.com/watch?v=d1K9xiiZ1e8 |
| 20  | I Built an Entire Architecture Project in ONE DAY with GPT Astra!                                     | ArchiTech Network                           | 35:19    | 2026-09-18 | llm, arq                               | ia-agentes-code | https://www.youtube.com/watch?v=X1WvG10zG-M |
| 21  | 5 powerful Things You Must Tell Yourself Every Morning \| Buddhist Wisdom for Calm Morning            | Glimpse Of Wisdom                           | 25:13    | 2026-09-18 | filosofia                              |                 | https://www.youtube.com/watch?v=-kqHfYc0UTA |
| 22  | ComfyUI for Animation: Concept Art to Any Angle (Tripo + GPT Image + Seedance)                        | ComfyUI                                     | 1:31     | 2026-09-18 | comfyui, ai-3d                         | ia-imagen       | https://www.youtube.com/watch?v=5O-4dqUchsE |
| 23  | Carl Jung Said that Life Really BEGINS at 40: My Midlife Advice To My Younger Self [FIXED AUDIO]      | Progress Pursuit                            | 21:01    | 2026-09-18 | filosofia                              |                 | https://www.youtube.com/watch?v=fal18RJOLQY |
| 24  | How to Think in 3D with Rhino \| S2 E1 \| Rhino Studio Series                                         | Rhino 3D (Rhinoceros3d official)            | 17:57    | 2026-09-15 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=sozaV2SFWDI |
| 25  | La Calma Hace Que Actúes Como Si Ya Tuvieras TODO Lo Que Deseas                                       | Paz en el Tao                               | 37:10    | 2026-09-15 | filosofia                              |                 | https://www.youtube.com/watch?v=4Br45kOed_s |
| 26  | Las enseñanzas de un lama para vivir mejor \| Rinchen Gyaltsen, monje budista                         | AprendemosJuntos                            | 1:17:28  | 2026-09-15 | filosofia                              |                 | https://www.youtube.com/watch?v=w5c4kRucRr0 |
| 27  | Atravesaste el infierno y algo cambió para siempre — Carl Jung                                        | Psycor                                      | 23:35    | 2026-09-15 | filosofia                              |                 | https://www.youtube.com/watch?v=F-1INVnrtvI |
| 28  | Cuando Te Calmas, Todo se Acomoda \| Sabiduría Espiritual                                             | El Camino del Buda                          | 1:22:11  | 2026-09-15 | filosofia                              |                 | https://www.youtube.com/watch?v=EMA608v7cmk |
| 29  | Cómo interactúan las personas inteligentes con los necios: la filosofía de Schopenhauer               | NOSCE TE IPSUM                              | 31:37    | 2026-09-15 | filosofia                              |                 | https://www.youtube.com/watch?v=gKpzLYW-nik |
| 30  | ¡Google acaba de reventar la creación de APPs GRATIS! 4 casos de uso brutales 🔥                      | Josema Fernández \| IA                      | 30:56    | 2026-09-15 | vibe-coding, llm                       | ia-agentes-code | https://www.youtube.com/watch?v=iHv0DTBoMy0 |
| 31  | I Finally Found an AI CAD Tool Architects Can Actually Use \| Synaps Tutorial                         | Salmaan Mohamed                             | 12:25    | 2026-09-14 | descartado                             |                 | https://www.youtube.com/watch?v=9kU6FT7ldZs |
| 32  | GPT-6 Astra Can Now Build Architectural 3D Models                                                     | Salmaan Mohamed                             | 8:12     | 2026-09-08 | llm, arq, viz                          | ia-agentes-code | https://www.youtube.com/watch?v=eKKpqMowytA |
| 33  | Estos juegos NO tenían VR… hasta AHORA 🤯                                                             | VrPatch                                     | 12:18    | 2026-09-06 | metaverso                              | diseno-arq      | https://www.youtube.com/watch?v=SnaXIT-EFm4 |
| 34  | Herramientas IA #10: Usando Spec Kit en OpenCode                                                      | Darellanodev                                | 38:24    | 2026-09-06 | llm, vibe-coding, opencode             | ia-agentes-code | https://www.youtube.com/watch?v=2kXr9PvOoPc |
| 35  | 🗺️  Import your DWG from AutoCAD and automatically adapt your building to the terrain. #AutoCAD #AI  | ARCHITEChTURES - English                    | 0:25     | 2026-09-06 | autocad                                | software-arq    | https://www.youtube.com/watch?v=TP18NCJxf2A |
| 36  | ¡META HACE CAMBIOS! 👉240 Hz en Quest 3, Half Life Alyx GRATIS con Steam Frame y Steam Link con CABLE | VrPatch                                     | 6:40     | 2026-09-05 | metaverso                              | diseno-arq      | https://www.youtube.com/watch?v=69ekfLN0fjE |
| 37  | New Autodesk Assistant (Tech Preview) \| AutoCAD 2027                                                 | AutoCAD                                     | 2:28     | 2026-09-05 | autocad                                | software-arq    | https://www.youtube.com/watch?v=wC0m_JfhfK8 |
| 38  | 🚀 ¡Hoy es el día!  📣 Taller Gratuito: Gestiona tus proyectos con Python + Power BI                  | Grid Studio                                 | 2:30:43  | 2026-09-05 | gestion                                | gestion         | https://www.youtube.com/watch?v=-wGoOstlVGM |
| 39  | The Danger of Awareness: Why You Can’t Unsee the Truth                                                | Progress Pursuit                            | 26:07    | 2026-09-05 | otros                                  |                 | https://www.youtube.com/watch?v=JH0W_Wzlmi4 |
| 40  | Transform Your Elevations with Rhino \| Rhino Studio Series #Shorts                                   | Rhino 3D (Rhinoceros3d official)            | 1:29     | 2026-09-05 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=ZQZPhtbp00s |
| 41  | parametric design for architects. #parametricdesign #architecture #parametric #architect              | David Copete Parametric                     | 0:50     | 2026-09-05 | arq, parametrico                       | diseno-arq      | https://www.youtube.com/watch?v=fHOZc2egsGU |
| 42  | Harvard enseña a programar en español (gratis)                                                        | MoureDev by Brais Moure                     | 0:39     | 2026-09-05 | vibe-coding                            | ia-agentes-code | https://www.youtube.com/watch?v=3CslWIaQWLQ |
| 43  | More control over motion. More control over the camera                                                | ComfyUI                                     | 0:16     | 2026-09-04 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=byhpMCvZNQo |
| 44  | El hábito de Leonardo da Vinci que me ha quitado el móvil de las manos  \| Commonplace book           | Maialen Lleó                                | 12:35    | 2026-09-04 | proyecto, notebook                     | gestion         | https://www.youtube.com/watch?v=A2S-lzsb3gw |
| 45  | 3 AI workflows I actually use as an Architect                                                         | Show It Better                              | 14:49    | 2026-09-04 | arq, agents                            | ia-agentes-code | https://www.youtube.com/watch?v=lEfSoR5JCaQ |
| 46  | Announcing the ComfyUI Forward Deployed Creative program                                              | ComfyUI                                     | 0:55     | 2026-09-03 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=omwi2IRRGw8 |
| 47  | ComfyUI Tutorial for Beginners: Image-to-Video, Motion Control & Upscaling (2026)                     | ComfyUI                                     | 42:00    | 2026-09-02 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=Yuw8F4E4-7Y |
| 48  | George Proud & Ismail Seleit \| AI Sucks: Why Architects need better AI tools \| Gendo                | ArchiTech Network                           | 16:04    | 2026-08-30 | charlas, arq, llm                      | ia-agentes-code | https://www.youtube.com/watch?v=4fWR8x2BtP0 |
| 49  | El fin del Vibe Coding: Crea software robusto con este método                                         | MoureDev by Brais Moure                     | 2:03:16  | 2026-08-29 | vibe-coding                            | ia-agentes-code | https://www.youtube.com/watch?v=5HaOxAAA5qI |
| 50  | I Connected Gemini to Blender… This Changes Everything (Blender MCP)                                  | MYN3D                                       | 1:50     | 2026-08-28 | blender, llm, agents                   | software-arq    | https://www.youtube.com/watch?v=vpH9HCZi1-I |
| 51  | Configura TUS AGENTES de OpenCode en 4 minutos                                                        | kiburld                                     | 4:07     | 2026-08-28 | opencode                               | ia-agentes-code | https://www.youtube.com/watch?v=EXPiDs3XXq4 |
| 52  | 👨‍🎓Tutorial Pixelart (Cap. 1) Empieza a hacer Pixelart desde cero!!                                 | Elias Lozano                                | 1:00:01  | 2026-08-28 | dibujo                                 | diseno-arq      | https://www.youtube.com/watch?v=F8jdt9Rc1Mc |
| 53  | Rhino for Architecture: Interface, Interoperability & Independence \| Rhino Studio Series             | Rhino 3D (Rhinoceros3d official)            | 3:31     | 2026-08-24 | rhino, arq                             | software-arq    | https://www.youtube.com/watch?v=g7Kq1cDrokE |
| 54  | Architecture Before Software: Think First, Then Build with Rhino \| Rhino Studio Series               | Rhino 3D (Rhinoceros3d official)            | 3:30     | 2026-08-24 | rhino, arq                             | software-arq    | https://www.youtube.com/watch?v=jP4nkpupcIc |
| 55  | Top 10 Setup Tricks with Rhino \| Rhino Studio Series                                                 | Rhino 3D (Rhinoceros3d official)            | 5:34     | 2026-08-23 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=qUhbXIF1DDw |
| 56  | Claude Code para profesionales, curso completo                                                        | HolaMundo                                   | 1:22:30  | 2026-08-23 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=zVK9CAdsc-g |
| 57  | Drafting Floor Plans with Rhino \| S1 E3 \| Rhino Studio Series                                       | Rhino 3D (Rhinoceros3d official)            | 17:40    | 2026-08-22 | rhino, planos                          | software-arq    | https://www.youtube.com/watch?v=gf1rkK-Uq1A |
| 58  | Drafting Site Plans & Context with Rhino \| S1 E2 \| Rhino Studio Series                              | Rhino 3D (Rhinoceros3d official)            | 13:32    | 2026-08-22 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=PlWRlBdxKcA |
| 59  | Build Your Drawing Standard with Rhino \| Rhino Studio Series #Shorts                                 | Rhino 3D (Rhinoceros3d official)            | 1:27     | 2026-08-22 | rhino, dibujo                          | software-arq    | https://www.youtube.com/watch?v=qsMZlvavM3k |
| 60  | How to Get Started with Rhino \| Rhino Studio Series                                                  | Rhino 3D (Rhinoceros3d official)            | 9:06     | 2026-08-21 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=RFPG6BmpyFs |
| 61  | 3 Tricks to Level Up Your Floor Plans with Rhino \| Rhino Studio Series #Shorts                       | Rhino 3D (Rhinoceros3d official)            | 1:13     | 2026-08-21 | rhino, planos                          | software-arq    | https://www.youtube.com/watch?v=jUFQQX7-cPw |
| 62  | Vida y triste final de DANIEL RABINOVICH (Les Luthiers) - Biografía de un genio - Ester Píscole       | Tukma Radio                                 | 31:06    | 2026-08-21 | otros                                  |                 | https://www.youtube.com/watch?v=YKUEPQmoeBM |
| 63  | Architecture Comes Before Software \| Rhino Studio Series #Shorts                                     | Rhino 3D (Rhinoceros3d official)            | 3:00     | 2026-08-20 | rhino, arq                             | software-arq    | https://www.youtube.com/watch?v=DnxHiyzPvVE |
| 64  | Using Comfy to Go Beyond the Models: Custom Workflows for Commercial and Film Production              | ComfyUI                                     | 1:02:05  | 2026-08-19 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=IzTI8oK_Wg4 |
| 65  | How I Fully Automated My Video Editing (Claude Code)                                                  | Brendan Jowett                              | 11:52    | 2026-08-19 | llm, vibe-coding, n8n                  | ia-agentes-code | https://www.youtube.com/watch?v=G0EH0xdy2-E |
| 66  | Stop editing videos! Use REMOTION instead, here’s how                                                 | Maciej Dziuba                               | 41:27    | 2026-08-19 | remotion                               | ia-video-audio  | https://www.youtube.com/watch?v=BmsT9V4YQWA |
| 67  | Curso completo de OpenCode desde cero: Modelos gratis, Comandos, Agentes y mucho más                  | MoureDev by Brais Moure                     | 2:31:24  | 2026-08-19 | vibe-coding, opencode                  | ia-agentes-code | https://www.youtube.com/watch?v=aDJNG_f2C3E |
| 68  | The INFJ Polymath Trap: Brilliant at Many Things, Certain About Nothing                               | Brainy Touch                                | 21:19    | 2026-08-19 | otros                                  |                 | https://www.youtube.com/watch?v=qZrRKXclf9k |
| 69  | Me creé un dashboard profesional con Claude en 5 minutos (sin Power BI)                               | Hashtag Capacitaciones \| IA                | 16:22    | 2026-08-19 | llm, gestion                           | ia-agentes-code | https://www.youtube.com/watch?v=lpvzvH4d_-c |
| 70  | ComfyUI Tutorial for Beginners: LoRAs, Style Transfer & ControlNets (2026)                            | ComfyUI                                     | 48:10    | 2026-08-19 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=-igiHGaxKek |
| 71  | ComfyUI MCP Server Now Runs Locally — Connect Claude, Cursor & Codex                                  | ComfyUI                                     | 0:21     | 2026-08-18 | comfyui, llm, agents, vibe-coding      | ia-imagen       | https://www.youtube.com/watch?v=IQep_c2R19M |
| 72  | Herramientas IA #2: Crear vídeo con Remotion y OpenCode                                               | Darellanodev                                | 9:56     | 2026-08-16 | llm, opencode, remotion                | ia-video-audio  | https://www.youtube.com/watch?v=7KMcc12K0fA |
| 73  | Curso COMPLETO de PYTHON desde CERO para PRINCIPIANTES                                                | MoureDev by Brais Moure                     | 10:07:35 | 2026-08-16 | vibe-coding                            | ia-agentes-code | https://www.youtube.com/watch?v=Kp4Mvapo5kc |
| 74  | El entrenamiento que te enseña a pensar como programador                                              | MoureDev by Brais Moure                     | 11:27:52 | 2026-08-16 | vibe-coding                            | ia-agentes-code | https://www.youtube.com/watch?v=qSup_483xO8 |
| 75  | Lo que haría hoy si tuviera que aprender a programar otra vez                                         | MoureDev by Brais Moure                     | 14:02    | 2026-08-16 | vibe-coding                            | ia-agentes-code | https://www.youtube.com/watch?v=KDxBEksTKBI |
| 76  | Claude Code + Ollama = Free Unlimited Coding AI                                                       | Eric Tech                                   | 14:10    | 2026-08-15 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=N7CQdYaeUEE |
| 77  | Las Apps Secretas de GitHub que Google No Quiere que Instales                                         | Núñez Tech                                  | 8:14     | 2026-08-15 | repos, vibe-coding                     | ia-agentes-code | https://www.youtube.com/watch?v=t7CUw_OOKbY |
| 78  | 4+6 Cosas que puedes hacer con un Router Viejo sin Internet                                           | elmondigital                                | 13:42    | 2026-08-15 | hardware                               | gestion         | https://www.youtube.com/watch?v=JnzMXLeI1AI |
| 79  | Minimax Music 3 is now on ComfyUI                                                                     | ComfyUI                                     | 1:50     | 2026-08-13 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=KXQOffw2Tmw |
| 80  | MiniMax H3: A New Open-Weight Video Model, Live in ComfyUI                                            | ComfyUI                                     | 44:17    | 2026-08-07 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=S9O3FPumX4Q |
| 81  | Flag Tag - Capture the Flag Meets Tag in Decentraland                                                 | Decentraland                                | 2:05:18  | 2026-08-06 | decentraland, nft, metaverso           | diseno-arq      | https://www.youtube.com/watch?v=oyqIEbOQEcA |
| 82  | How I use AI in our architecture office (it's Runway)                                                 | Gediminas Kirdeikis                         | 29:06    | 2026-08-06 | video-ia, arq                          | ia-video-audio  | https://www.youtube.com/watch?v=G2GBdFH1VBE |
| 83  | The Future of AI Post Production: Custom LoRAs & Motion Graphics Nodes with Ingi Erlingsson           | ComfyUI                                     | 1:05:11  | 2026-08-05 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=4xS4LOn3CTE |
| 84  | The Blueprint to Get Flexible Once, Forever                                                           | matthewismith                               | 39:01    | 2026-08-02 | otros                                  |                 | https://www.youtube.com/watch?v=3j7oSqCuTHs |
| 85  | Cómo Tu Atención Colapsa la Realidad Todos los Días — Aldous Huxley                                   | Códigos de Riqueza                          | 16:08    | 2026-08-01 | otros                                  |                 | https://www.youtube.com/watch?v=ZaC7mtoxNR0 |
| 86  | Video Model Showdown: Open-Source vs. Paid AI Video Models                                            | ComfyUI                                     | 1:03:43  | 2026-07-31 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=VeG1bveKZco |
| 87  | Reemplacé todo mi entrenamiento por estos 5 holds soviéticos (Método Pavel)                           | Tipo Gris                                   | 9:37     | 2026-07-31 | otros                                  |                 | https://www.youtube.com/watch?v=NqBFBnhUQcI |
| 88  | ComfyUI Tutorial for Beginners: Full Node Graph Basics (2026)                                         | ComfyUI                                     | 1:12:16  | 2026-07-31 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=TQhIYT1ZYGQ |
| 89  | The Brutal Shift Every INFJ Faces After 40                                                            | Brainy Touch                                | 20:29    | 2026-07-31 | otros                                  |                 | https://www.youtube.com/watch?v=m9BI_ezPtA0 |
| 90  | Juan Martín Maldacena - El significado del espacio-tiempo                                             | Planetario BA                               | 1:53:15  | 2026-07-30 | otros                                  |                 | https://www.youtube.com/watch?v=2nooU_KfIns |
| 91  | ComfyUI Moodboard Workflow: Generate On-Brand Ad Images (Recraft + GPT Image)                         | ComfyUI                                     | 1:22     | 2026-07-30 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=cTdHYiD28F4 |
| 92  | How to use ComfyUI MCP with Claude Code                                                               | ComfyUI                                     | 59:25    | 2026-07-29 | comfyui, llm, agents, vibe-coding      | ia-imagen       | https://www.youtube.com/watch?v=8RGN69h_xTU |
| 93  | ComfyUI Billboard Mockup Tutorial: Realistic Out-of-Home Ad Placements                                | ComfyUI                                     | 1:22     | 2026-07-28 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=e_rXFG6BWZE |
| 94  | With Comfy MCP, workflows can be built from anywhere                                                  | ComfyUI                                     | 1:07     | 2026-07-28 | comfyui, agents                        | ia-imagen       | https://www.youtube.com/watch?v=WePHUX46ZLc |
| 95  | You can generate split-stack videos like this in a single click                                       | ComfyUI                                     | 0:07     | 2026-07-28 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=x1w5IJKr9vE |
| 96  | Playwright + Claude Code: tu agente navega y testea webs solo                                         | Nicolas Dubois                              | 12:06    | 2026-07-27 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=9Cr-1nJE9i0 |
| 97  | Masterclass · Del copiloto al guionista: IA para audiovisual                                          | B:Side Academy                              | 1:19:10  | 2026-07-27 | charlas, llm                           | ia-agentes-code | https://www.youtube.com/watch?v=Tys9_WVEoVQ |
| 98  | Agentic Engineering: ya no se promptea, se orquesta (paper de Google)                                 | Nicolas Dubois                              | 15:13    | 2026-07-27 | llm, agents                            | ia-agentes-code | https://www.youtube.com/watch?v=nuzi3k4oX9A |
| 99  | Turn AutoCAD Floor Plans into Stunning AI Renders                                                     | Salmaan Mohamed                             | 7:52     | 2026-07-26 | autocad, viz, planos                   | software-arq    | https://www.youtube.com/watch?v=FGJ1RpAXsxA |
| 100 | Architecture Diagrams Crash Course - 6 Types of Diagrams You Should Be Using                          | Kyle Sinko                                  | 8:20     | 2026-07-26 | diagramas, arq                         | diseno-arq      | https://www.youtube.com/watch?v=Y-oqz-cTAbU |
| 101 | Architects Are Switching to Claude \| Here's Why - FULL Guide                                         | Urban Decoders                              | 18:15    | 2026-07-26 | llm, arq                               | ia-agentes-code | https://www.youtube.com/watch?v=la8Ml1fQfOg |
| 102 | Keyan Rahimzadeh: How VIA Builds the World's Most Complex Facades \| VIA \| ATN Summit 2026           | ArchiTech Network                           | 26:15    | 2026-07-26 | charlas, planos                        | diseno-arq      | https://www.youtube.com/watch?v=A4fntmDzCZY |
| 103 | The Complete AI Workflow for Architectural Visualization                                              | LandSpace Architecture                      | 9:10     | 2026-07-25 | arq, viz                               | diseno-arq      | https://www.youtube.com/watch?v=hsNtcYtgc3g |
| 104 | VES ESTO PORQUE SUPERASTE LA PRUEBA FINAL \| EL SECRETO DE CARL JUNG QUE PUEDE CAMBIAR TU VIDA        | Explorar la Mente del Universo Español      | 34:15    | 2026-07-25 | filosofia                              |                 | https://www.youtube.com/watch?v=KjLMbYY0jEQ |
| 105 | Directed, Not Prompted: Cinematic Al Filmmaking with ComfyUl                                          | ComfyUI                                     | 0:20     | 2026-07-24 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=D0zqyIN4iOs |
| 106 | Inside the BIM Masterclass with Charles Vidal (Bjarke Ingels Group: BIG) \| Revit + Claude AI         | PAACADEMY                                   | 1:11     | 2026-07-23 | revit, llm, charlas                    | software-arq    | https://www.youtube.com/watch?v=4JB4prsOlok |
| 107 | Directed, Not Prompted: Cinematic AI Filmmaking with ComfyUI                                          | ComfyUI                                     | 0:19     | 2026-07-23 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=bpH39Dd_wvA |
| 108 | Directed, Not Prompted: Cinematic AI Filmmaking with ComfyUI                                          | ComfyUI                                     | 0:20     | 2026-07-22 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=UIuQCwvwFdU |
| 109 | Open World Models in Production: LTX and ComfyUI Founders Live                                        | ComfyUI                                     | 59:29    | 2026-07-21 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=dbp5Jnto7S8 |
| 110 | New FREE Local 3D AI Generator is Here! (TripoSplat)                                                  | PixelArtistry                               | 12:41    | 2026-07-16 | ai-3d                                  | ia-imagen       | https://www.youtube.com/watch?v=Ldwd1APMw5A |
| 111 | Import ANY location on Earth to your Rhino Model                                                      | How to Rhino                                | 0:17     | 2026-07-16 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=zCUZ1SP0vkc |
| 112 | ComfyUI for Architects: Generate Renders in Minutes (Not Hours)                                       | architutors                                 | 10:22    | 2026-07-16 | comfyui, arq, viz                      | ia-imagen       | https://www.youtube.com/watch?v=RAMs89SS6cM |
| 113 | ComfyUI on Your Phone: AI Videos From Vacation \| Comfy MCP                                           | ComfyUI                                     | 0:23     | 2026-07-15 | comfyui, agents                        | ia-imagen       | https://www.youtube.com/watch?v=yG9Wi0IzOOw |
| 114 | El Secreto de la Mente: Cómo el Observador Crea la Realidad Sin Esfuerzo — Aldous Huxley              | Mente Fractal                               | 42:37    | 2026-07-14 | filosofia                              |                 | https://www.youtube.com/watch?v=XcZI-E302Bg |
| 115 | Nuevo CHATGPT para Arquitectura e Interiorismo ▶ Proyectos completos                                  | bydavidparra                                | 8:22     | 2026-07-09 | llm, arq                               | ia-agentes-code | https://www.youtube.com/watch?v=1GL4y-TaPU0 |
| 116 | He Creado un Segundo Cerebro con IA… y Es una Locura!                                                 | Javier DV - Inversión y Finanzas            | 24:21    | 2026-07-09 | llm, notebook                          | ia-agentes-code | https://www.youtube.com/watch?v=cwF8JK92pdw |
| 117 | Google lanza 8 bombas NUEVAS con Gemini GRATIS: Esto puedes hacer 💣                                  | Alejavi Rivera                              | 27:30    | 2026-07-09 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=gnGR0oVspcs |
| 118 | State of Ai at MVRDV                                                                                  | DAD Dipartimento di Architettura e Design   | 1:49:19  | 2026-07-05 | charlas, arq                           | diseno-arq      | https://www.youtube.com/watch?v=xb18odKRs3s |
| 119 | Master AI in Rhino 3D FAST (2025)                                                                     | Urban Decoders                              | 12:04    | 2026-07-05 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=aMhj-d0JiKY |
| 120 | Tips · Herramientas aplicadas a la IA en arquitectura con Carlos Muñoz                                | B:Side Academy                              | 1:12     | 2026-07-04 | charlas, arq, llm                      | ia-agentes-code | https://www.youtube.com/watch?v=Ga4H_e6TAlM |
| 121 | Domina el 90% de Hermes Agent en 39 minutos (Guía Completa)                                           | Josema Fernández \| IA                      | 39:01    | 2026-07-04 | llm, agents, vibe-coding               | ia-agentes-code | https://www.youtube.com/watch?v=Ysb-sE4VLyA |
| 122 | CAD TO AI Quickly AutoCAD YQPRIME                                                                     | CAD Concepts                                | 3:40     | 2026-07-02 | autocad                                | software-arq    | https://www.youtube.com/watch?v=leqltdKMhNQ |
| 123 | Bauhaus 100: A BBC Arts Documentary                                                                   | Dr Umer Hameed                              | 59:25    | 2026-07-01 | charlas, arq                           | diseno-arq      | https://www.youtube.com/watch?v=wwYZQjgUljA |
| 124 | The FULL 2026 Guide To Layout & Composition For Designers!                                            | Satori Graphics                             | 30:56    | 2026-07-01 | planos                                 | diseno-arq      | https://www.youtube.com/watch?v=PKfZ1gnVJ44 |
| 125 | Las skills OFICIALES de n8n en Claude Code (ya disponibles)                                           | Nicolas Dubois                              | 10:45    | 2026-06-30 | llm, vibe-coding, n8n                  | ia-agentes-code | https://www.youtube.com/watch?v=BZ0eaaO9IMY |
| 126 | Leaving Zaha Hadid Architects & AI Driven Architecture \| Tim Fu                                      | BlessedArch                                 | 45:03    | 2026-06-28 | charlas, arq                           | diseno-arq      | https://www.youtube.com/watch?v=ezbD51v4i0A |
| 127 | #67 - Winy Maas - MVRDV, Markthal, Imprint, Technology, Computational Design, Urbanism                | Parametric Architecture                     | 42:55    | 2026-06-28 | arq, parametrico                       | diseno-arq      | https://www.youtube.com/watch?v=A_HQ77AuhxQ |
| 128 | How AI is Transforming Architecture - Keir Regan-Alexander                                            | Bespoke Careers                             | 53:17    | 2026-06-27 | charlas, arq                           | diseno-arq      | https://www.youtube.com/watch?v=Te9yJ1Kthb8 |
| 129 | Tim Fu: Designing at the Speed of AI \| Studio Tim Fu \| ATN Summit 2026                              | ArchiTech Network                           | 25:58    | 2026-06-27 | charlas, arq                           | diseno-arq      | https://www.youtube.com/watch?v=uYffGLGOfzw |
| 130 | Krea X Comfy: Founders Live                                                                           | ComfyUI                                     | 59:29    | 2026-06-24 | comfyui                                | ia-imagen       | https://www.youtube.com/watch?v=31jiUhCEjJ4 |
| 131 | Experto en Poder Mental: "vamos a vivir en Silent Hill: quien domina esta habilidad triunfa"          | Zoom Out Podcast                            | 1:38:36  | 2026-06-24 | filosofia                              |                 | https://www.youtube.com/watch?v=f7aiFYdm9-c |
| 132 | Claude Code + WhatsApp: el CRM con agentes de IA que le vendes a cualquier negocio (Guía Completa)    | Josema Fernández \| IA                      | 43:04    | 2026-06-23 | llm, vibe-coding, whatsapp             | ia-agentes-code | https://www.youtube.com/watch?v=exgTjIiDS8A |
| 133 | Facturación automática con ARCA: cómo lo hice paso a paso en mi SaaS                                  | char.developer                              | 11:52    | 2026-06-23 | n8n                                    | ia-agentes-code | https://www.youtube.com/watch?v=oGwblZdlD5k |
| 134 | Le conté en vivo a 400 personas cómo pasar de 0 a 100 en Meta Ads usando IA (sin ser experto)         | Caro Dubi - Marketing de Resultados         | 14:18    | 2026-06-23 | llm, marketing                         | ia-agentes-code | https://www.youtube.com/watch?v=olg11wKMR-M |
| 135 | 🤖 Un diseñador IA GRATIS en tu estudio con el Nodo Designer en Magnific Spaces (Novedad)             | Escuela de INteriorismo EStratégico         | 5:52     | 2026-06-23 | magnific, ia-imagen, llm               | ia-imagen       | https://www.youtube.com/watch?v=qWB7p_n-jDA |
| 136 | Georgie and Mandy: The Movie (2024) \| FULL MOVIE                                                     | Abdurazaak Ufram                            | 1:31:35  | 2026-06-23 | otros                                  |                 | https://www.youtube.com/watch?v=qqwhjSzFJqY |
| 137 | Los mejores comandos de Claude Code que uso todos los días                                            | Nicolas Dubois                              | 21:06    | 2026-06-23 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=0ilUMO8Yj1U |
| 138 | ¡Claude Code + Antigravity revientan a las AGENCIAS web! El sistema entero de un negocio 🔥           | Josema Fernández \| IA                      | 36:06    | 2026-06-23 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=zgJ2f_fAynY |
| 139 | Taking 3D Characters From Comfy To Blender                                                            | ComfyUI                                     | 1:00:10  | 2026-06-23 | blender, comfyui                       | software-arq    | https://www.youtube.com/watch?v=cXXNUR_wu60 |
| 140 | De 0 a EXPERTO en Chatwoot + n8n \| Automatiza WhatsApp paso a paso                                   | Diego Vásquez \| IA builder                 | 50:14    | 2026-06-23 | llm, n8n, whatsapp                     | ia-agentes-code | https://www.youtube.com/watch?v=-6IleMvI_80 |
| 141 | Carmen Santamaría revela los perfiles ocultos de las ALTAS CAPACIDADES                                | Marc Romera                                 | 1:01:01  | 2026-06-20 | otros                                  |                 | https://www.youtube.com/watch?v=5dZkZ08x8GA |
| 142 | Si Haces Estas 7 Cosas Estando Solo, Tienes una Inteligencia Extremadamente Rara                      | Mente y Conducta                            | 10:41    | 2026-06-20 | otros                                  |                 | https://www.youtube.com/watch?v=ZzIPb_zDgXo |
| 143 | This Workflow Is Faster Than Traditional Architectural Drawing Software                               | Rayon Academy                               | 19:05    | 2026-06-19 | dibujo, arq                            | diseno-arq      | https://www.youtube.com/watch?v=qXDu__GaL7s |
| 144 | PENSAMIENTO DIVERGENTE y ARBORESCENTE (concepto y diferencias)                                        | El Rincón de Álvaro                         | 7:26     | 2026-06-18 | filosofia                              |                 | https://www.youtube.com/watch?v=PyVGu_-Px5I |
| 145 | AI Is Replacing Everyone. Here Is Why The INFJ Is Safe.                                               | Your Mind Is Your Super Power               | 24:15    | 2026-06-17 | filosofia                              |                 | https://www.youtube.com/watch?v=jPwwZVAB1ZA |
| 146 | 10 Señales de que Tienes una Inteligencia Extraordinaria Y No Lo Sabías                             | Mente Descubierta                           | 15:00    | 2026-06-17 | otros                                  |                 | https://www.youtube.com/watch?v=j7FyV1ksjlc |
| 147 | El arte visual de Los Redondos                                                                        | Televisión Pública Noticias                 | 0:49     | 2026-06-08 | otros                                  |                 | https://www.youtube.com/watch?v=XnhFX45GM8s |
| 148 | INFJs Don't Think in Lines — They Think in Patterns No One Else Can See                               | Brainy Touch                                | 20:50    | 2026-06-08 | otros                                  |                 | https://www.youtube.com/watch?v=wKDaP1qzhdQ |
| 149 | Por qué los inteligentes fingen ser normales — La Persona (Carl Jung)                                 | Psicología In Depth                         | 5:11     | 2026-06-07 | otros                                  |                 | https://www.youtube.com/watch?v=exIPbkZlDA0 |
| 150 | Pensamiento ARBORESCENTE ¿o pensamiento RIZOMÁTICO? en alta capacidad                                 | Bea Sánchez                                 | 13:04    | 2026-06-07 | otros                                  |                 | https://www.youtube.com/watch?v=8n-zZj2CSG4 |
| 151 | Alta Capacidad: 3 CLAVES con base cerebral, funcional y observable.                                   | Bea Sánchez                                 | 13:23    | 2026-06-07 | otros                                  |                 | https://www.youtube.com/watch?v=ocnm-ncPlMA |
| 152 | Músicos Doble Excepcionalidad: TDAH, TCA, Autismo, Tourette, dislexia, depresión y +                  | Bea Sánchez                                 | 11:29    | 2026-06-07 | otros                                  |                 | https://www.youtube.com/watch?v=RerjlwXElFs |
| 153 | Buscando a Wally: La vida de un adulto con TDAH \| Elena Benítez \| TEDxIgualada                      | TEDx Talks                                  | 10:49    | 2026-06-06 | charlas                                |                 | https://www.youtube.com/watch?v=RBkQD_URQ-M |
| 154 | Completa. Jana Martínez-Piqueras, experta en altas capacidades: Niños y niñas con altas capacidades   | AprendemosJuntos                            | 42:33    | 2026-06-04 | otros                                  |                 | https://www.youtube.com/watch?v=pvUlZJY0DT0 |
| 155 | Open Code: Este es Mi setup definitivo (Skills + Comandos + MCPs + Multi Agentes)                     | The Coder Cave \| Programación y Tecnología | 57:05    | 2026-06-01 | agents, hardware                       | ia-agentes-code | https://www.youtube.com/watch?v=kdx2yB0zLSM |
| 156 | 5 AI Workflows Every Interior Designer Should Try                                                     | Salmaan Mohamed                             | 8:40     | 2026-05-31 | interior                               | diseno-arq      | https://www.youtube.com/watch?v=POsaBs5AusA |
| 157 | I Connected Claude AI to Revit - The Results Scared Me                                                | Archi Vlogs                                 | 9:44     | 2026-05-28 | revit, llm                             | software-arq    | https://www.youtube.com/watch?v=vmVvpKSSxWE |
| 158 | ¿LA IA VA A REEMPLAZAR A TODOS? \| El FUTURO del TRABAJO contado por un ESPECIALISTA                  | Infobae                                     | 15:21    | 2026-05-26 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=nqQ9G3V_zzo |
| 159 | Rhino User Webinar: Integrating Machine Learning models in Rhino 8                                    | McNeel Europe                               | 40:11    | 2026-05-26 | rhino                                  | software-arq    | https://www.youtube.com/watch?v=KV1CT4EMVuY |
| 160 | Claude AI for Architects \| 6 Ways to Use It in Your Design Practice                                  | Salmaan Mohamed                             | 9:39     | 2026-05-26 | llm, arq                               | ia-agentes-code | https://www.youtube.com/watch?v=YXHkjqoGmHg |
| 161 | Grasshopper AI: Machine Learning Generates Full Floor Plans Instantly                                 | Algorithmix Design                          | 1:38     | 2026-05-26 | rhino, grasshopper, planos             | software-arq    | https://www.youtube.com/watch?v=1hQAek0DDGw |
| 162 | Antigravity 2: No solo programa... Ahora lo HACE TODO                                                 | Xavier Mitjana                              | 17:16    | 2026-05-24 | descartado                             |                 | https://www.youtube.com/watch?v=1iitERYvi80 |
| 163 | ¡Mezcla Sprite con carbón y el resultado te va a dejar con la boca abierta!                           | SuperConsejos                               | 2:19     | 2026-05-24 | descartado                             |                 | https://www.youtube.com/watch?v=S9_SpqIIKa0 |
| 164 | Cómo crear tu propio CRM y Chatbot de WhatsApp con IA (Tutorial Paso a Paso) 🚀                       | Federico Feres                              | 22:16    | 2026-05-20 | llm, whatsapp                          | ia-agentes-code | https://www.youtube.com/watch?v=OWc1WZtNykg |
| 165 | Argentina - Buenos Aires - Pope Francis Tribute - FULL SET VIDEO (18.04.2026) Padre Guilherme         | Padre Guilherme                             | 2:32:10  | 2026-05-18 | otros                                  |                 | https://www.youtube.com/watch?v=rPw4E5WTEGE |
| 166 | THIS is the Biggest Thing Since CGI                                                                   | Corridor Crew                               | 26:47    | 2026-05-14 | gaussian-splatting, repos              | ia-agentes-code | https://www.youtube.com/watch?v=X8yRlA7jqEQ |
| 167 | SkySplat (free): Gaussian Splatting in Blender made easy                                              | Nicko16                                     | 9:46     | 2026-05-14 | blender, gaussian-splatting            | software-arq    | https://www.youtube.com/watch?v=iO48fxcsAys |
| 168 | Generate 3D from ANY Video! │Gaussian Splatting Tutorial w/ Postshot                                  | Black Mixture                               | 18:50    | 2026-05-14 | gaussian-splatting, repos              | ia-agentes-code | https://www.youtube.com/watch?v=Xn4h0vJ-wYQ |
| 169 | 3D Gaussian Splatting \| How to Clean, Export & Share Your 3DGS Model with Clients (Supersplat Guide) | UFLY UAS                                    | 14:41    | 2026-05-13 | gaussian-splatting, repos              | ia-agentes-code | https://www.youtube.com/watch?v=9YyPNiFHwpg |
| 170 | These Are the Best Tools to Create Gaussian Splatting                                                 | XR AI Spotlight                             | 17:20    | 2026-05-13 | llm, gaussian-splatting, metaverso     | ia-agentes-code | https://www.youtube.com/watch?v=CrlSey4RmVI |
| 171 | Crea videos Largos 100% Gratis e Ilimitado  - Flujo de Trabajo completo                               | Tutoriales Informáticos + IA                | 15:54    | 2026-05-03 | video-ia, llm                          | ia-video-audio  | https://www.youtube.com/watch?v=sOw-Dff5qVQ |
| 172 | Inteligencia artificial: cómo entenderla sin miedo \| José Ignacio Latorre, físico cuántico           | AprendemosJuntos                            | 57:48    | 2026-05-03 | charlas, llm                           | ia-agentes-code | https://www.youtube.com/watch?v=mm4W5Y-TNH0 |
| 173 | 😱¡NUEVA IA! Crea VIDEOS LARGOS GRATIS en 4K Automático y SIN ESFUERZO                                | Tutoriales Informáticos + IA                | 9:44     | 2026-04-21 | video-ia, llm, n8n                     | ia-video-audio  | https://www.youtube.com/watch?v=WHrec4Q0seY |
| 174 | Convierte TODOS tus documentos en un CEREBRO DIGITAL                                                  | Xavier Mitjana                              | 16:47    | 2026-04-16 | llm, notebook                          | ia-agentes-code | https://www.youtube.com/watch?v=MDa13zptsro |
| 175 | NADIE está creando webs así con ANTIGRAVITY...                                                        | Andres Web                                  | 8:09     | 2026-04-16 | descartado                             |                 | https://www.youtube.com/watch?v=GthseaWsjDg |
| 176 | CREA un AGENTE INMOBILIARIO PERSONALIZADO para tus LEADS con IDEALISTA y n8n                          | Alejandro Susillo                           | 33:55    | 2026-04-15 | n8n                                    | ia-agentes-code | https://www.youtube.com/watch?v=UHXLw7d8JXI |
| 177 | Curso de Desarrollo con Inteligencia Artificial 2026: De cero a producción                            | MoureDev by Brais Moure                     | 3:18:52  | 2026-04-15 | vibe-coding                            | ia-agentes-code | https://www.youtube.com/watch?v=X0oHLHIL7Mk |
| 178 | Claude Code: Tokens ilimitados con estos 15 Trucos                                                    | Agustín Medina \| AI Agency Academy         | 16:50    | 2026-04-12 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=hDt-7qCiQ5A |
| 179 | Anthropic acaba de matar el No-Code (Claude Managed Agents)                                           | Benjamín Cordero                            | 32:44    | 2026-04-10 | llm, agents                            | ia-agentes-code | https://www.youtube.com/watch?v=gLjeJJNi74k |
| 180 | Cómo extraer leads de Google Maps con Outscraper (sin complicarte)                                    | Gabriel Martínez - Reachflow ⚡️             | 5:51     | 2026-04-05 | descartado                             |                 | https://www.youtube.com/watch?v=sQGAlPMhoA0 |
| 181 | GEMMA 4: La IA 100% GRATIS de Google. ¡Cómo usarla en tu PC!                                          | Xavier Mitjana                              | 25:25    | 2026-04-05 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=JTh79ZUnobM |
| 182 | What's new in Twinmotion 2026.1                                                                       | Twinmotion Guru                             | 5:58     | 2026-03-25 | twinmotion                             | software-arq    | https://www.youtube.com/watch?v=0j3GQb08r64 |
| 183 | DEJA de APRENDER herramientas IA  (El 99% es Hype)                                                    | Agustín Medina \| AI Agency Academy         | 25:14    | 2026-03-24 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=NC9B_NqvQrg |
| 184 | ¿Va a desaparecer la programación? La verdad sobre la IA - Brais Moure (MoureDev)                     | Uri Sabat                                   | 1:16:41  | 2026-03-23 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=yEotzWQxAqs |
| 185 | 8 Herramientas IA que Uso Todos los Días (Resultados Reales)                                          | Tege Digital                                | 19:51    | 2026-03-23 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=wiD6AtPOxpQ |
| 186 | Por qué la IA te da RESPUESTAS MEDIOCRES (otros sacan ORO)                                            | Gustavo Entrala                             | 23:05    | 2026-03-23 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=fZ7ZeH65PFA |
| 187 | Google AI Studio cambió todo: crea apps full stack gratis sin configurar nada                         | Rodrigo Olivares - Crea con IA              | 5:36     | 2026-03-23 | vibe-coding, llm                       | ia-agentes-code | https://www.youtube.com/watch?v=O8FYsuizzfA |
| 188 | Cómo Crear Sitios Webs Claude Code + Nano banana 2 + Kling 3.0                                        | Agustín Medina \| AI Agency Academy         | 17:13    | 2026-03-23 | nanobanana, video-ia, llm, vibe-coding | ia-imagen       | https://www.youtube.com/watch?v=3GhfWOnp6Ok |
| 189 | ¡Cómo APRENDER en TIEMPO RECORD con IA! 🚀 Así usan NotebookLM en el MIT                              | Xavier Mitjana                              | 23:59    | 2026-03-23 | llm, notebook                          | ia-agentes-code | https://www.youtube.com/watch?v=OefqBTBREgY |
| 190 | ¡100% GRATIS! CapCut PRO y 100% Legal - Método Actualizado (2026)                                     | Tutoriales Informáticos + IA                | 8:07     | 2026-03-21 | descartado                             |                 | https://www.youtube.com/watch?v=MNwEY87C_ik |
| 191 | NEW Google Antigravity + Stitch + Claude Cowork Projects + NemoClaw + Minimax M2.7 Updates!           | Julian Goldie SEO                           | 1:24:47  | 2026-03-21 | llm, marketing                         | ia-agentes-code | https://www.youtube.com/watch?v=ak9Z0pkLcWY |
| 192 | Claude Code: Cómo Crear Tareas Programadas Paso a Paso                                                | Nicolas Dubois                              | 9:38     | 2026-03-20 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=OU3twlRhB0k |
| 193 | Google acaba de lanzar estas novedades en Gemini                                                      | Migue Baena IA                              | 16:29    | 2026-03-20 | descartado                             |                 | https://www.youtube.com/watch?v=eqIB91o8nxw |
| 194 | Cómo uso Claude Cowork para hacer en minutos lo que antes me llevaba semanas 🚀🚀                     | Jose A. Rubio                               | 29:40    | 2026-03-19 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=c92lm4KGVvM |
| 195 | Crea Tu Propio RAG personal en Claude Code \| Paso a Paso                                             | Agustín Medina \| AI Agency Academy         | 17:08    | 2026-03-18 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=74iB941XRPk |
| 196 | Gemini Cli + Nano Banana 2 is INSANE! 🤯                                                              | Julian Goldie SEO                           | 8:11     | 2026-03-16 | nanobanana, llm, marketing             | ia-imagen       | https://www.youtube.com/watch?v=XA5MiWUkRow |
| 197 | Most Architects Are Missing These 10 AI Tools (2026) ⌛                                                | Salmaan Mohamed                             | 8:48     | 2026-03-16 | arq, llm                               | ia-agentes-code | https://www.youtube.com/watch?v=4-_k6UdMUUU |
| 198 | Google lanza 6 bombas NUEVAS en Gemini GRATIS: Esto puedes hacer ahora                                | Alejavi Rivera                              | 28:27    | 2026-03-14 | descartado                             |                 | https://www.youtube.com/watch?v=HsQHwZFto2M |
| 199 | How to create viral shorts using AI automation (N8N + ChatGPT + FFmpeg)                               | Javid Jamae                                 | 3:20     | 2026-02-05 | llm, n8n                               | ia-agentes-code | https://www.youtube.com/watch?v=LzSV4EfI_dw |
| 200 | 10 Free University Courses That Are Better Than Paid Ones                                             | Shane Hummus                                | 14:46    | 2026-01-18 | otros                                  |                 | https://www.youtube.com/watch?v=qHwIiwjrT1I |
| 201 | No Human Could Explain INFJs Like This                                                                | Dear Fellow INFJ                            | 11:17    | 2026-01-04 | otros                                  |                 | https://www.youtube.com/watch?v=H6wJNiNloWk |
| 202 | 8 Dificultades de Ser Altamente Inteligente que la Psicología Rara Vez Explica                        | FueraDelRuido                               | 10:42    | 2025-12-29 | otros                                  |                 | https://www.youtube.com/watch?v=6aRcdaDyLCk |
| 203 | Archi-Tech Talk E9: How BIG Is Integrating D5?                                                        | ArchiTech Network                           | 55:41    | 2025-11-27 | charlas, arq, viz                      | diseno-arq      | https://www.youtube.com/watch?v=dU3EFQiUS9A |
| 204 | 20 Signs You’re NEURODIVERGENT & How to Unlock Your Greatest Potential \| Mayim Bialik’s Breakdown    | Dr. Mayim Bialik                            | 1:15:00  | 2025-11-24 | otros                                  |                 | https://www.youtube.com/watch?v=deateY1ZJU0 |
| 205 | 50 Signs You’re A True INFJ (Rare Personality Type)                                                   | The INFJ Circle                             | 12:37    | 2025-11-08 | otros                                  |                 | https://www.youtube.com/watch?v=TgbiccIYhwk |
| 206 | 5 INSANE Ways to Use Nano Banana for Architecture and Interior Design                                 | Nuno Silva                                  | 6:47     | 2025-11-06 | nanobanana, arq, interior              | ia-imagen       | https://www.youtube.com/watch?v=6IYOKjZCWlI |
| 207 | Blender Earth Modeler Add-on \| 3D Google Earth (City/Terrain) inside Blender                         | Imagiscope Tech                             | 5:24     | 2025-11-03 | blender                                | software-arq    | https://www.youtube.com/watch?v=80GrFXFOayE |
| 208 | Parametric Floor Plan  + Open Nest Exercise & Rhino Parametric Architecture tutorial                  | David Copete Parametric                     | 29:42    | 2025-10-25 | rhino, arq, parametrico, planos        | software-arq    | https://www.youtube.com/watch?v=L_r6SroevxY |
| 209 | Google actualiza su MEJOR HERRAMIENTA gratuita 🤯 6 casos de uso BRUTALES                             | Xavier Mitjana                              | 19:57    | 2025-10-24 | descartado                             |                 | https://www.youtube.com/watch?v=rHF4iMsH3_I |
| 210 | 10 COSAS INCREÍBLES que puedes hacer GRATIS con las IAs de Google (Gemini, NotebookLM, OPAL, Veo…)    | Migue Baena IA                              | 27:37    | 2025-10-24 | descartado                             |                 | https://www.youtube.com/watch?v=hUnNum9p0ME |
| 211 | NotebookLM ACTUALIZADO... ¡Crea en 1 CLIC! 🍌 Y más novedades sobre IA                                | Xavier Mitjana                              | 29:40    | 2025-10-20 | descartado                             |                 | https://www.youtube.com/watch?v=VUOCXqwZmLE |
| 212 | La forma REAL de programar con IA en 2026                                                             | MoureDev by Brais Moure                     | 16:00    | 2025-10-19 | llm, vibe-coding                       | ia-agentes-code | https://www.youtube.com/watch?v=uquw8yUKaYM |
| 213 | 10 Signs You’re Not Just an INFJ… You’re a Sigma INFJ                                                 | Interesting Psychology                      | 21:28    | 2025-10-17 | otros                                  |                 | https://www.youtube.com/watch?v=UEhvDDM5LKA |
| 214 | El papel de las células cerebrales humanas en el futuro de la IA \| Bloomberg Primer                  | Bloomberg en Español                        | 24:02    | 2025-08-31 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=cPoUnoM-Kt4 |
| 215 | Andrés Rieznik: CONICET, inteligencia artificial y la batalla CULTURAL \| La Última Frontera          | Filo News                                   | 48:10    | 2025-08-29 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=qR9FLvlQwfA |
| 216 | La Extraña Matemática Que Predice (Casi) Todo                                                         | Veritasium en español                       | 32:32    | 2025-08-25 | otros                                  |                 | https://www.youtube.com/watch?v=6pO6Mm2qJaE |
| 217 | The Weird Traits of INFJ Personalities                                                                | BI️ Studio of Emotional Intelligence        | 16:11    | 2025-08-17 | otros                                  |                 | https://www.youtube.com/watch?v=rKr5p_3hQoM |
| 218 | Cómo Los Maestros Japoneses Convierten la Arena en Espadas                                            | Veritasium en español                       | 24:02    | 2025-08-17 | otros                                  |                 | https://www.youtube.com/watch?v=3KsR03Ir6xM |
| 219 | Why Empaths Attract People Who Secretly Resent Their Light  Carl Jung \| Carl Jung Original           | The Psychoanalysis                          | 44:08    | 2025-08-16 | otros                                  |                 | https://www.youtube.com/watch?v=4yrG1MIFJKQ |
| 220 | Fractales: qué son estos patrones infinitos y por qué se les llama "la huella digital de Dios"        | BBC News Mundo                              | 6:24     | 2025-08-16 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=0zii09KeDis |
| 221 | Dub in the Treehouse 🌴🛸✨ \| 2h20m Psychedelic Reggae Dub                                            | Futuristic Sound                            | 2:20:31  | 2025-08-15 | otros                                  |                 | https://www.youtube.com/watch?v=iJi5a2c32n4 |
| 222 | La espiral de Fibonacci es más especial de lo que parece \| La matemática del número áureo            | Lemnismath                                  | 16:15    | 2025-08-12 | otros                                  |                 | https://www.youtube.com/watch?v=6HP4SidWzIY |
| 223 | SOI Open House: #TaludContinental4 \| Live from R/V Falkor (too)                                      | Schmidt Ocean Institute                     | 57:05    | 2025-08-12 | otros                                  |                 | https://www.youtube.com/watch?v=VtLAkt44jKQ |
| 224 | I Wish I Knew this when I Started Acrylic Painting.                                                   | Ten Hundred                                 | 28:37    | 2025-08-11 | otros                                  |                 | https://www.youtube.com/watch?v=l0E2nLLwXUM |
| 225 | Lance 27.1 Mar Del Plata Canyon \| SOI Divestream 821                                                 | Schmidt Ocean Institute                     | 7:47:57  | 2025-08-05 | otros                                  |                 | https://www.youtube.com/watch?v=3OEvDvoFGMQ |
| 226 | Mejores Páginas Web De Cursos Gratuitos (con certificado)                                            | Adrián Sáenz                                | 6:44     | 2025-07-29 | otros                                  |                 | https://www.youtube.com/watch?v=IA2pr0kHzd0 |
| 227 | 7 Strange Things INFJ Would Die For                                                                   | Brainy Touch                                | 22:49    | 2025-07-22 | otros                                  |                 | https://www.youtube.com/watch?v=gerFtROg-ow |
| 228 | The Childhood Trauma of INFJ (Nobody Talks About This)                                                | Brainy Touch                                | 11:18    | 2025-07-20 | otros                                  |                 | https://www.youtube.com/watch?v=ETIY2k5jiM0 |
| 229 | Ciencia fascinante para personas curiosas \| Miguel Alcubierre, doctor en Física                      | AprendemosJuntos                            | 1:10:58  | 2025-07-19 | otros                                  |                 | https://www.youtube.com/watch?v=uXDiwHgy3Fo |
| 230 | Olympic Boxer Faces Aggressive VR Opponent! \| Thrill of the Fight 2 (Boxing Game)                    | Tony Jeffries                               | 25:10    | 2025-07-12 | metaverso                              | diseno-arq      | https://www.youtube.com/watch?v=Gf5KPKhBfwo |
| 231 | Are You An Empath? The 20 Traits & How To Use Sensitivity As A Super Power                            | Dr. Mayim Bialik                            | 1:10:59  | 2025-07-11 | otros                                  |                 | https://www.youtube.com/watch?v=opX0sbuLG7Q |
| 232 | 9 AI Skills You MUST Have to Become Rich in 2026                                                      | Dan Martell                                 | 19:23    | 2025-07-10 | otros                                  |                 | https://www.youtube.com/watch?v=Eq8JgI3HmjI |
| 233 | Reverse Engineering RollerCoaster Tycoon \| How does it work?                                         | Nathan Baggs                                | 38:54    | 2025-07-10 | otros                                  |                 | https://www.youtube.com/watch?v=r9gRk-Px7l4 |
| 234 | E-Ink Weather Dashboard with a Raspberry Pi                                                           | AKZ Dev                                     | 6:15     | 2025-07-05 | otros                                  |                 | https://www.youtube.com/watch?v=65sda565l9Y |
| 235 | Top AI courses that you can take for free                                                             | Scholar Strategy by Nistha Tripathi         | 0:08     | 2025-06-27 | otros                                  |                 | https://www.youtube.com/watch?v=S5KUpTgoSco |
| 236 | Facundo Díaz: ¿la IA y la computación cuántica transformarán nuestra realidad? \| La Última Frontera  | Filo News                                   | 59:35    | 2025-06-25 | llm                                    | ia-agentes-code | https://www.youtube.com/watch?v=fH8Bu3RpaL8 |
| 237 | LEARNING ARKIO \| DAY 1 \| OCULUS QUEST \| VR                                                         | Nikhil Bang                                 | 16:33    | 2025-05-27 | metaverso                              | diseno-arq      | https://www.youtube.com/watch?v=EEqYvtw7J0E |
| 238 | Qué son (realmente): 19 Señales de que Eres Altas Capacidades Intelectuales                           | Jimena González                             | 6:55     | 2025-05-25 | otros                                  |                 | https://www.youtube.com/watch?v=yxxxFsXNTZ0 |
| 239 | ✅ Cómo VECTORIZAR un LOGO o IMAGEN en Illustrator [ rápido y sencillo ]                               | Saber Programas Imagen                      | 4:38     | 2025-05-25 | otros                                  |                 | https://www.youtube.com/watch?v=ZeESXFWoyxU |
| 240 | How The INFJ Brain Mirrors Neurodivergent Patterns                                                    | BrainWatched                                | 26:10    | 2025-05-24 | otros                                  |                 | https://www.youtube.com/watch?v=GknLS0PUPAE |
| 241 | Anécdotas y Señales de Autismo en Mujeres de Altas Capacidades, con Andrea Bou ♾️                     | Jimena González                             | 38:17    | 2025-05-24 | otros                                  |                 | https://www.youtube.com/watch?v=IoZhkm-GJDU |
| 242 | _(sin titulo)_                                                                                        |                                             |          | 2025-05-20 | otros                                  |                 | https://www.youtube.com/watch?v=Un9SHPVAAbE |
| 243 | Open-source AI music is finally here!                                                                 | AI Search                                   | 31:22    | 2025-05-13 | otros                                  |                 | https://www.youtube.com/watch?v=zw46L4pDFWo |
| 244 | How To Become A Master Storyteller                                                                    | Kallaway                                    | 11:14    | 2025-05-13 | otros                                  |                 | https://www.youtube.com/watch?v=t5Z-Q1bg1tU |
| 245 | 8 Japanese Aesthetics That Might Change How You See Beauty                                            | Dans Le Gris                                | 16:28    | 2025-05-11 | otros                                  |                 | https://www.youtube.com/watch?v=PdXz1HNKz9A |
| 246 | The Fractal Menger Sponge and Pi                                                                      | Stand-up Maths                              | 13:06    | 2025-05-10 | otros                                  |                 | https://www.youtube.com/watch?v=8pj8_zjelDo |
| 247 | Everything is Connected -- Here's How: \| Tom Chi \| TEDxTaipei                                       | TEDx Talks                                  | 17:49    | 2025-05-08 | charlas                                |                 | https://www.youtube.com/watch?v=rPh3c8Sa37M |
| 248 | 3D space mouse: is it USEFUL? - Tech for architects & designers                                       | UH Studio Design Academy                    | 3:29     | 2025-05-08 | arq, hardware                          | diseno-arq      | https://www.youtube.com/watch?v=8TBoQdE91CE |
| 249 | Physicist Explores The Missing Link Between Alchemy & Quantum Mechanics \| Dr. Theresa Bullard        | André Duqum                                 | 2:15:44  | 2025-05-07 | otros                                  |                 | https://www.youtube.com/watch?v=mrKiH4J0_5U |
| 250 | Avoid these 6 Mistakes When Talking to an INFP                                                        | Matt Sherman - Geek Psychology              | 12:25    | 2025-05-02 | otros                                  |                 | https://www.youtube.com/watch?v=YheeL8KSdvw |
| 251 | 10 Things People Hate About INFPs                                                                     | Matt Sherman - Geek Psychology              | 29:10    | 2025-05-02 | otros                                  |                 | https://www.youtube.com/watch?v=8qks_-n02T8 |
| 252 | El ENGAÑO del Ordenador Cuántico de Microsoft                                                         | QuantumFracture                             | 22:52    | 2025-04-28 | otros                                  |                 | https://www.youtube.com/watch?v=6LA-N6vFoJs |
| 253 | Top Physicist: “Reality Is Not Physical”                                                              | Be Inspired                                 | 23:18    | 2025-04-25 | otros                                  |                 | https://www.youtube.com/watch?v=pEo6eN9ZVnM |
| 254 | Quantum Decision Tree                                                                                 | Glenn Cowell                                | 0:26     | 2025-04-18 | otros                                  |                 | https://www.youtube.com/watch?v=9kpYz2zfLgs |
| 255 | Decision Tree - A Fractal Poem (with a philosophical surprise)                                        | Mike Naylor                                 | 3:20     | 2025-04-18 | otros                                  |                 | https://www.youtube.com/watch?v=Gv6UzG3KxyQ |
| 256 | Instantly Bend Reality Using 33rd Degree Knowledge (Top 1% Secret)                                    | Vibration of the Universe                   | 31:41    | 2025-04-11 | otros                                  |                 | https://www.youtube.com/watch?v=a7LJPgAO3Ok |
| 257 | Once you master Quantum Entanglement, You UNLOCK The Hidden Energy of your Subconscious               | David McEwen                                | 31:49    | 2025-04-08 | otros                                  |                 | https://www.youtube.com/watch?v=1KM7IQ8jglg |
| 258 | Visualization method they don't want you to know about (shifts reality instantly)                     | David McEwen                                | 24:03    | 2025-04-08 | viz                                    | diseno-arq      | https://www.youtube.com/watch?v=HSTLbkNVu9g |
| 259 | AI Reset: "Life As We Know It Will Be Gone In 5 Years" - Upcoming Utopia vs Dystopia \| Salim Ismail  | Tom Bilyeu                                  | 3:19:16  | 2025-04-05 | charlas, llm                           | ia-agentes-code | https://www.youtube.com/watch?v=uyqujcyRZ90 |

---

### ARQ/3D-Print

Archivo Takeout: `ARQ_3D-Print-vídeos.csv` · Videos: 34

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Is This ChatGPT for 3D Printing? \| Create Printable 3D Models in SECONDS | Slant 3D | 10:09 | 2025-10-15 |  | llm, viz | ia-agentes-code | https://www.youtube.com/watch?v=thfXHrAZVJI |
| 2 | HUGE 3D AI Update: Hunyuan3D 3.0 Is Finally Here! | PixelArtistry | 23:58 | 2025-10-15 |  | ai-3d | ia-imagen | https://www.youtube.com/watch?v=dckhcvrgx-s |
| 3 | Quick AI Image to 3D Concept Models - Hunyuan 3D with ComfyUI | Urban Decoders | 6:31 | 2025-10-14 |  | comfyui, ai-3d | ia-imagen | https://www.youtube.com/watch?v=EuAe-4nXFSk |
| 4 | I Tried NANO BANANA AI: Can One Photo Make a 3D Model? | BIM Design Studio | 4:41 | 2025-10-14 |  | nanobanana, viz | ia-imagen | https://www.youtube.com/watch?v=b-OXLKABuK4 |
| 5 | Google Map 3D to FBX - 3D Modeling Tutorial | Freedom Arts 3D Workflow | 12:06 | 2025-10-14 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=FiLN_d1bGRU |
| 6 | 🧠 DISEÑO 3D con Inteligencia Artificial ► Butaca SURREALISTA en PromeAI | bydavidparra | 6:35 | 2025-10-14 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=WDMKMkkJ8wg |
| 7 | ProArchitect #004 - Mesh vs NURBS (basics of CAD geometry) | ProArchitect | 11:01 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=50TeShIuPQU |
| 8 | Esta I.A nos dejó sin Laburo? \| Cómo pasar de 2D a 3D con un solo click - Guía Paso a Paso | Día de la Toalla | 11:30 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=ZyjXzIwGFXo |
| 9 | NEXT-GEN 3D – Intelligent 3D Layer Segmentation (Hunyuan and Tripo 3D) | Urban Decoders | 10:01 | 2025-10-13 |  | ai-3d | ia-imagen | https://www.youtube.com/watch?v=USO3IT1K3zI |
| 10 | I Tried Nano Banana AI: Free 3D Building from Just a Photo! | LandSpace Architecture | 5:17 | 2025-10-13 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=Ur1TamXxJqw |
| 11 | Mastering Miniature Architecture: 3D Printing & Model-Making Techniques \| #miniaturebuildersstudio | Miniature Builders Studio | 0:12 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=jbIabPnSOz8 |
| 12 | 3d Printing for Architects / My Process for Fast and Easy Model-making | Life of an Architect | 4:57 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=sXqDb967iJU |
| 13 | Large Architectural Model 3D Printed in Only 11 Days | BigRep 3D Printers | 1:23 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=Ynuq4sUlERQ |
| 14 | MATT Architecture: Rapid model making with 3D printing - Ultimaker: 3D Printing Story | UltiMaker | 4:13 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=mMU_FG-KuX4 |
| 15 | Printing a New Architecture \| James Rose \| TEDxUTK | TEDx Talks | 9:47 | 2025-10-13 |  | arq, charlas | diseno-arq | https://www.youtube.com/watch?v=VBo7ZIS_MY8 |
| 16 | How to 3D print your CITY using Blender and Google Maps | Andrew Sponer | 8:58 | 2025-10-13 |  | blender, 3d-print | software-arq | https://www.youtube.com/watch?v=kzeJSy1z8W4 |
| 17 | 5 plataformas donde descargar modelos 3d | Bugeo 3d | 6:15 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=Xmo2izTtc_w |
| 18 | 3D Printing Materials Explained: Compare FDM, SLA, and SLS | Formlabs | 6:18 | 2025-10-13 |  | 3d-print | construccion | https://www.youtube.com/watch?v=9B-HGhN_jCk |
| 19 | Types of 3D Printers - 11 Different Types of 3D Printers - Introduction to 3D Printing | Rainmaker 3D | 20:10 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=DMWzMpjSJLM |
| 20 | Why STL is dead and 3MF is the future of 3D printing | Prusa 3D | 3:47 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=BABdR9d8Cp4 |
| 21 | Largest Community of 3D-printed Homes \| Wolf Ranch in Texas | ICON | 1:01 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=k0REJf3rv44 |
| 22 | Zaha Hadid · Knit Candela (2018) | Museo Universitario Arte Contemporáneo | 5:12 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=7C7QwqivQPI |
| 23 | Concrete Choreography | Digital Building Technologies | 1:59 | 2025-10-13 |  | concreto | construccion | https://www.youtube.com/watch?v=rvd20U-QgKw |
| 24 | All the Different 3d printing Filaments Explained! | Technivorous 3d Printing | 10:24 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=qajTuTQUPsQ |
| 25 | Inside The World’s Largest 3D Printed Neighborhood | CNBC | 9:11 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=WOR612WviMs |
| 26 | #𝟎𝟓: ¡Impresión 3D + realidad aumentada! | Fundación Movistar Argentina | 8:54 | 2025-10-13 |  | 3d-print, metaverso | construccion | https://www.youtube.com/watch?v=fDzyhE6RUSg |
| 27 | Introduction to Stereolithography | Formlabs | 2:20 | 2025-10-13 |  | 3d-print | construccion | https://www.youtube.com/watch?v=yW4EbCWaJHE |
| 28 | Large Architectural Model 3D Printed in Only 11 Days #3dprinting #bigrep #shorts | BigRep 3D Printers | 0:48 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=LcLQ0nR5AQc |
| 29 | From Blueprint to 3D Print 🏗️✨ \| Architectural Model Making Process | Vutuk Design and Media | 2:10 | 2025-10-13 |  | 3d-print, arq | construccion | https://www.youtube.com/watch?v=Exw7pjbSGOc |
| 30 | 3Djony: Helping architects start 3D printing | Prusa 3D | 4:56 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=u65oFz3h9Xc |
| 31 | I 3d Printed a $2,700 Kumiko Panel | Paper View | 6:20 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=w5P7E7muk9o |
| 32 | Custom Models in UNREAL 5 and GOOGLE MAPS using Cesium ( Revit, Rhino, Sketchup) | Urban Decoders | 20:54 | 2025-10-13 |  | rhino, revit, unreal, sketchup | software-arq | https://www.youtube.com/watch?v=aKi1Q3JRn7U |
| 33 | 3D Modeling & Design with SubD | Mario Elementza | 1:11:43 | 2025-10-13 |  | arq-3d-print | construccion | https://www.youtube.com/watch?v=dQ1viXMvWX4 |
| 34 | Electroplating 3D Printed Jewelry \| FULL TUTORIAL | HEN3DRIK - Electroplating 3D Prints | 11:22 | 2025-10-13 |  | 3d-print | construccion | https://www.youtube.com/watch?v=sGntt6eInis |

---

### ARQ/AutoCAD2D

**Tu descripcion:** Lisp, Bloques,

Archivo Takeout: `ARQ_AutoCAD2D-vídeos.csv` · Videos: 40

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Como hacer Bloques Dinámicos en 3D, en #AutoCAD | Roberto Marroquin | 4:57 | 2025-10-14 |  | autocad | software-arq | https://www.youtube.com/watch?v=CrFZZe0NXXo |
| 2 | Master AutoCAD Lisp: Importing Google Earth Data & Hatching Area Tables | Civil Engineering Survey | 7:43 | 2025-10-13 |  | autocad | software-arq | https://www.youtube.com/watch?v=-NItmOrxoj4 |
| 3 | ¿Machine Learning y AutoCAD? ¡¡¡Resultados INTERANTES!!! | Axel T. | 9:37 | 2025-10-13 |  | autocad | software-arq | https://www.youtube.com/watch?v=PxxN6lujNSk |
| 4 | Why You Should Learn Lisp In 2025 | Gavin Freeborn | 21:50 | 2025-10-13 |  | arq-autocad2d | software-arq | https://www.youtube.com/watch?v=GWdf1flcLoM |
| 5 | LISP, el "lenguaje de DIOS" | LinuxChad | 22:26 | 2025-07-10 |  | arq-autocad2d | software-arq | https://www.youtube.com/watch?v=-QHTPXOHvIo |
| 6 | AutoCAD - How To Use Sheet Sets | You Can Draft! | 30:43 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=PUnPyEgA_zQ |
| 7 | Constraint Workflow | AutoCAD | 4:45 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=ULDIMQJsC9Q |
| 8 | Constraints and Parameters in AutoCAD | Micrographics | 9:27 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=fGMFbOZGcGI |
| 9 | Markup Import and Markup Assist for Autodesk Docs \| AutoCAD 2026 | AutoCAD | 2:02 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=H6_iIlG6nHw |
| 10 | AutoCAD Mastery: Discover the Top 50 Commands in YQArch Guide - Best Tutorials | CAD Concepts | 45:00 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=druGovW29eQ |
| 11 | Como geolocalizar en autocad / Como insertar un mapa de google earth | Arshiredú | 0:47 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=XUqvkSVxMs8 |
| 12 | "50 Powerful AutoCAD Productive Lisp Programs : Best CAD Tutorials" | CAD Concepts | 43:31 | 2025-05-25 |  | autocad | software-arq | https://www.youtube.com/watch?v=yhKC-Ddmitg |
| 13 | 🚀 Ultimate AutoCAD Tutorial: Shrinking DWG Files with Ease! 📐 | Civil Engineering Survey | 3:52 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=3dZLxAPe8hw |
| 14 | Effortless Data Extraction: AutoCAD Lisp for MS Word and Notepad | Civil Engineering Survey | 2:27 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=zy9wkGY8H90 |
| 15 | Master Dynamic Labeling in CAD with the Latest Lisp fAREA Update | Civil Engineering Survey | 5:16 | 2025-05-24 |  | arq-autocad2d | software-arq | https://www.youtube.com/watch?v=U-ClpRmsLK0 |
| 16 | Save Time in AutoCAD: Instantly Convert Area to Table with YQArch | Civil Engineering Survey | 3:09 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=MKo7JeXKyi0 |
| 17 | New LISP for AutoCAD: Table Area, Parameters, Radius & Coordinates! | Civil Engineering Survey | 5:30 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=wcE6hKs2dT4 |
| 18 | WOW! ChatGPT Just Built a Lisp Tool for AutoCAD in Minutes! | Civil Engineering Survey | 4:38 | 2025-05-24 |  | autocad, llm | software-arq | https://www.youtube.com/watch?v=tZaK-75AP8w |
| 19 | AutoLISP Programming \| Part 4: Dynamic Text Placement Tutorial | ATC CAD | 19:05 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=fhV0Gx7qUmA |
| 20 | Make Your AutoLISP Pro! Adding Command Line Options and Blocks to AutoCount | ATC CAD | 26:46 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=zDxSQscpOKI |
| 21 | How to Automatically Load AutoLISP Routines Into AutoCAD | ATC CAD | 11:31 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=Ylm2K7Us4AA |
| 22 | 📝Crea Barra de Menú en #AutoCAD con Tús Comandos #Autolisp 2019 | Cursodecadd2d | 10:30 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=q74lWmNOFY4 |
| 23 | ⏳ Cómo ser MÁS EFICIENTE en AutoCAD creando MACROS con la Grabadora de Acciones | Martín Cipoletta | 15:36 | 2025-05-24 |  | autocad | software-arq | https://www.youtube.com/watch?v=zcn_Z6ocT1I |
| 24 | Do Architects Still Draw by Hand? | The Revit Kid | 1:02:46 | 2025-05-11 |  | revit, arq | software-arq | https://www.youtube.com/watch?v=m6QxygZ3iN0 |
| 25 | How to create elevations automatically in AutoCAD using a Lisp file | skilled.design | 0:26 | 2025-04-23 |  | autocad | software-arq | https://www.youtube.com/watch?v=HbB4srVWLvs |
| 26 | _(sin titulo)_ |  |  | 2025-04-23 |  | arq-autocad2d | software-arq | https://www.youtube.com/watch?v=Nx6A_mb8Na4 |
| 27 | AutoCAD Acotar todas las dimensiones con un solo click (Lisp) | Señor Chong | 1:15 | 2025-04-23 |  | autocad | software-arq | https://www.youtube.com/watch?v=SVq8K0HqIak |
| 28 | ✨ New LISP Magic: AutoCAD Automated Polyline Dimensioning | Civil Engineering Survey | 1:49 | 2025-04-23 |  | autocad, n8n | software-arq | https://www.youtube.com/watch?v=9yGrq4oE6lk |
| 29 | How to make automatic dimensions for all lots (all segments) at once in AutoCAD (Using Lisp) | Engineer DZ-tutorial | 5:24 | 2025-04-23 |  | autocad, n8n | software-arq | https://www.youtube.com/watch?v=i1dFBrdE-Ik |
| 30 | AutoCAD's Copy Field Lisp Automatic Update Areas. Insert Field With Suffix | Civil Engineering Survey | 4:11 | 2025-04-23 |  | autocad, n8n | software-arq | https://www.youtube.com/watch?v=_zXjmVALLdM |
| 31 | AutoCAD's Lisp Area Label, Area to Table and Area to File Automatic Field Update | Civil Engineering Survey | 5:42 | 2025-04-23 |  | autocad, n8n | software-arq | https://www.youtube.com/watch?v=sSXuwlNTN5I |
| 32 | AutoCAD Polyline area and Perimeter leader Lisp & Manual Tips insert field | Civil Engineering Survey | 3:27 | 2025-04-23 |  | autocad | software-arq | https://www.youtube.com/watch?v=xw8BUjiNIh8 |
| 33 | AutoCAD LISP Coordinates Report Of Polyline Segment's & Export to txt, Csv & Table Report in AutoCAD | Civil Engineering Survey | 9:01 | 2025-04-23 |  | autocad | software-arq | https://www.youtube.com/watch?v=NV-L4sbJNcY |
| 34 | AutoCAD LISP PDIM AND DPL | Civil Engineering Survey | 4:15 | 2025-04-23 |  | autocad | software-arq | https://www.youtube.com/watch?v=8OE38rS3w68 |
| 35 | Amazing Section Graphics in Revit Tutorial | Balkan Architect | 20:30 | 2025-04-08 |  | revit, arq | software-arq | https://www.youtube.com/watch?v=ZNOVHjF4RJg |
| 36 | Freecad - Parametric Cabinet Assembly - Woodworking | Deltahedra | 34:56 | 2025-03-05 |  | freecad, parametrico | software-arq | https://www.youtube.com/watch?v=oXLrEydllwc |
| 37 | 🧠 Calcula ESCALERAS con ChatGPT!!!【EN MENOS DE 1 MINUTO】 | bydavidparra | 5:20 | 2025-02-04 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=b6QrN9mtBnA |
| 38 | 🧠 AREAS de AutoCAD AUTOMATICAS con CHATGPT  ► En un Plano Arquitectónico!!! | bydavidparra | 5:02 | 2025-02-04 |  | autocad, llm, n8n, planos | software-arq | https://www.youtube.com/watch?v=lzuO7ZEAiXI |
| 39 | 🧠 Creo MILES de BLOQUES de AutoCAD con CHATGPT  ► EN MINUTOS!!! | bydavidparra | 9:20 | 2025-02-04 |  | autocad, llm | software-arq | https://www.youtube.com/watch?v=yb0zVJfpc4o |
| 40 | SOLUCIÓN DEFINITIVA: Error FlexNet License Finder en Autodesk 2025\| No Más Interrupciones | AGUIRRE Y COMPAÑIA EIRL | 6:13 | 2025-02-04 |  | arq-autocad2d | software-arq | https://www.youtube.com/watch?v=Enl7k1NOZes |

---

### ARQ/docs

Archivo Takeout: `ARQ_docs-vídeos.csv` · Videos: 24

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Archi-Tech Talk E9: How BIG Is Integrating D5? | ArchiTech Network | 55:41 | 2025-11-27 | Si | charlas, arq, viz | diseno-arq | https://www.youtube.com/watch?v=dU3EFQiUS9A |
| 2 | Why Rhino is KING for Innovative Architecture! | ArchiTech Network | 9:29 | 2025-10-15 |  | rhino, arq | software-arq | https://www.youtube.com/watch?v=N_5Ju9czZ-E |
| 3 | EP 4 \| ArchiTech Office Tours \| Foster + Partners | ArchiTech Network | 1:23:26 | 2025-10-15 |  | arq-docs | diseno-arq | https://www.youtube.com/watch?v=p-oF3aIG_OA |
| 4 | EP 2 \| ArchiTech Office Tours \| Zaha Hadid Architects | ArchiTech Network | 1:09:36 | 2025-10-15 |  | arq | diseno-arq | https://www.youtube.com/watch?v=aoWlS_2Hr10 |
| 5 | EP 10 \| ArchiTech Office Tours \| BIG HQ | ArchiTech Network | 1:15:59 | 2025-10-15 |  | arq-docs | diseno-arq | https://www.youtube.com/watch?v=h8nVH03zzZk |
| 6 | EP 18 \| ArchiTech Office Tours \| MVRDV \| Part 1: Office Tour | ArchiTech Network | 52:04 | 2025-10-15 |  | arq | diseno-arq | https://www.youtube.com/watch?v=XwTxSqFR-wY |
| 7 | Leaving Zaha Hadid Architects & AI Driven Architecture \| Tim Fu | BlessedArch | 45:03 | 2025-10-14 | Si | charlas, arq | diseno-arq | https://www.youtube.com/watch?v=ezbD51v4i0A |
| 8 | @PAACADEMYY AI-Driven Design Practice – Stable Diffusion in Architecture (Cas Esbach / MVRDV) | Parametric Architecture | 3:23:18 | 2025-10-14 |  | stable-diffusion, arq, parametrico | ia-imagen | https://www.youtube.com/watch?v=FCKhn42cxHk |
| 9 | Patrik Schumacher (Zaha Hadid Architects) talks about the Metaverse | BlessedArch | 1:03:45 | 2025-10-14 |  | arq, metaverso | diseno-arq | https://www.youtube.com/watch?v=VjGeAKsVB7Q |
| 10 | Breaking Down the Best Architecture Competition Boards of 2024 | Show It Better | 16:44 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=YkAuu4oDSJ4 |
| 11 | AI will not replace architects - Patrik Schumacher from Zaha Hadid Architects | BlessedArch | 21:35 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=9Fft67Mq_0c |
| 12 | How MVRDV is using AI to design their buildings | Show It Better | 18:21 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=dvKAyTRptkw |
| 13 | Evolution of Architectural Drawings - From Hand-Drawing to Computational Design to AI | Parametric Architecture | 8:30 | 2025-10-14 |  | arq, parametrico, dibujo | diseno-arq | https://www.youtube.com/watch?v=0vPzLPMg4y4 |
| 14 | Concepts: Parametric Architecture \| Edu-Archs | Edu-Archs | 11:33 | 2025-10-14 |  | arq, parametrico | diseno-arq | https://www.youtube.com/watch?v=F92tRbqFAO4 |
| 15 | Do Architects Still Draw by Hand? | The Revit Kid | 1:02:46 | 2025-10-13 |  | revit, arq | software-arq | https://www.youtube.com/watch?v=m6QxygZ3iN0 |
| 16 | "BIG" Diagrams in Revit Tutorial | The Revit Kid | 14:24 | 2025-10-13 |  | revit, diagramas | software-arq | https://www.youtube.com/watch?v=gV4YThNggdk |
| 17 | Archi-Tech Talk E3 \| Video Games, Architecture and Participatory Urbanism | ArchiTech Network | 58:58 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=SiRJhIivWfg |
| 18 | How Frank Gehry's Guggenheim Bilbao Changed Architecture Forever | The B1M | 32:01 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=FnrPZuN0m-0 |
| 19 | Bjarke Ingels: 3 warp-speed architecture tales | TED | 18:12 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=4AYE3w5TWHs |
| 20 | Bjarke Ingels - My evolutionary journey as an architect \| Architects, not Architecture. | Architects not Architecture | 51:09 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=IVIhD3l7HvI |
| 21 | Arquitectura de hierro y vidrio | Academia Play | 1:58 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=inghnTbYpSk |
| 22 | Abstract: The Art of Design \| Bjarke Ingels: Architecture \| FULL EPISODE \| Netflix | Netflix | 44:21 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=rKeFCd1j5BE |
| 23 | The Bauhaus Design Process | Roberts Architecture | 22:40 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=0ryRpgLWgs0 |
| 24 | Big Time \| Architect Bjarke Ingels Documentary | Standart | 1:30:09 | 2025-10-13 |  | arq, charlas | diseno-arq | https://www.youtube.com/watch?v=gHubfCPQNUU |

---

### ARQ/IA

Archivo Takeout: `ARQ_IA-vídeos.csv` · Videos: 32

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Masterclass · El nuevo perfil del IA Manager en un estudio de arquitectura | B:Side Academy | 53:58 | 2026-07-03 |  | llm, arq, charlas | ia-agentes-code | https://www.youtube.com/watch?v=RXOWifxRkp0 |
| 2 | Patrik Schumacher: Upgrading Architecture's Core Competency \| ZHA \| ATN Summit 2026 | ArchiTech Network | 1:04:10 | 2026-07-01 |  | arq, charlas | diseno-arq | https://www.youtube.com/watch?v=4UHNeJChmOk |
| 3 | German Otto Bodenbender: Human and Machine: The Augmented Architect \| BIG \| ATN Summit 2026 | ArchiTech Network | 26:25 | 2026-06-29 |  | arq, charlas | diseno-arq | https://www.youtube.com/watch?v=tgO7k72g5ag |
| 4 | German Otto Bodenbender: Human and Machine: The Augmented Architect \| BIG \| ATN Summit 2026 | ArchiTech Network | 1:29 | 2026-06-29 |  | arq, charlas | diseno-arq | https://www.youtube.com/watch?v=lXOTLQd-Sro |
| 5 | Most Architects Are Missing These 10 AI Tools (2026) ⌛ | Salmaan Mohamed | 8:48 | 2026-03-16 | Si | arq, llm | ia-agentes-code | https://www.youtube.com/watch?v=4-_k6UdMUUU |
| 6 | _(sin titulo)_ |  |  | 2025-12-05 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=pg68lUYSxe4 |
| 7 | TOP uses of Google Earth with AI | Urban Decoders | 8:09 | 2025-11-03 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=JNVV4sQ_2dw |
| 8 | Architecture Programs to Learn in 2021/22 to Become A Future Proof Archi-Tech | ArchiTech Network | 47:42 | 2025-10-15 |  | arq | diseno-arq | https://www.youtube.com/watch?v=1DDoQgcBmAk |
| 9 | Foyr vs Coohom \| Rendering Speed, Assets & Pricing Explained (2025) | Salmaan Mohamed | 11:54 | 2025-10-15 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=0xaPs5MQiBs |
| 10 | 8 MUST HAVE FREE Extensions for ARCHITECTS \| 2025 | Salmaan Mohamed | 4:37 | 2025-10-15 |  | arq | diseno-arq | https://www.youtube.com/watch?v=bo5rl8hGisE |
| 11 | Controlling Blender with my voice using LLM | Polyfjord Deep Dive | 15:33 | 2025-10-14 |  | blender, llm | software-arq | https://www.youtube.com/watch?v=ytomieYqUCQ |
| 12 | How To Create Real-Time Renders with AI (synced to 3D model) | Design Input | 37:42 | 2025-10-14 |  | viz | diseno-arq | https://www.youtube.com/watch?v=GmXkrgqvWvk |
| 13 | Top 10 AI Model for Architecture \| Stable diffuision for Architecture | Archi Lab | 3:12 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=Ga0vZwq7hW4 |
| 14 | 6 ChatGPT SECRETS that every ARCHITECT Should Know \| OpenAI 4.0 Image Generator 🔥 | Salmaan Mohamed | 10:30 | 2025-10-14 |  | llm, arq | ia-agentes-code | https://www.youtube.com/watch?v=GN8IK2Wbw8E |
| 15 | Modelar IFC con IA | IFC Addict | 55:00 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Eht46GIociI |
| 16 | Nano Banana for Exterior Design Architecture \| EVERYTHING YOU SHOULD KNOW | Salmaan Mohamed | 6:01 | 2025-10-14 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=T-tpBjPkEl8 |
| 17 | Beautiful Parametric Architecture with Blender | UH Studio Design Academy | 26:53 | 2025-10-14 |  | blender, arq, parametrico | software-arq | https://www.youtube.com/watch?v=_AJ3_wOSNBQ |
| 18 | AI will not replace architects - Patrik Schumacher from Zaha Hadid Architects | BlessedArch | 21:35 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=9Fft67Mq_0c |
| 19 | How MVRDV is using AI to design their buildings | Show It Better | 18:21 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=dvKAyTRptkw |
| 20 | Architecture Software in 2025. | Show It Better | 11:11 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=VIL-5Rsi_9I |
| 21 | Open BIM con IFC y FreeCAD | IFC Addict | 1:02:02 | 2025-10-14 |  | freecad | software-arq | https://www.youtube.com/watch?v=0pW9XbmsKBM |
| 22 | Part 1, Course - Residential Building: Parametric Massing. Blender Architecture | UH Studio Design Academy | 1:16:12 | 2025-10-14 |  | blender, arq, parametrico | software-arq | https://www.youtube.com/watch?v=Wr7-w_DspYM |
| 23 | Cype Open BIM: ¿El futuro GRATUITO del cálculo y diseño de instalaciones? | BIMdesign consulting | 11:27 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=m7vk01-TXWA |
| 24 | IA en architecture : 10 usages concrets que je mets en place pour les architectes | Future Architecture | 28:13 | 2025-10-13 |  | llm, arq | ia-agentes-code | https://www.youtube.com/watch?v=bNAoXc8h_zA |
| 25 | Create blender 3d scenes with Claude AI \| Blender MCP Setup Instructions | Code Bear | 3:25 | 2025-10-13 |  | blender, llm, agents | software-arq | https://www.youtube.com/watch?v=oN1LoMz-6VM |
| 26 | ONLY 1% of Architects Know These 20 KILLER illustrator Tips | Surviving Architecture | 20:18 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=dXJjWfej8JQ |
| 27 | I connected Claude AI to Blender 3D...Mind-Blowing Results (MCP) | Max Novak | 15:50 | 2025-10-13 |  | blender, llm, agents | software-arq | https://www.youtube.com/watch?v=r7H60u0kHRA |
| 28 | Draw Floor Plans 3X FASTER!! 🤯 Rayon Design | Salmaan Mohamed | 0:28 | 2025-10-13 |  | planos | diseno-arq | https://www.youtube.com/watch?v=V4w4MUuh0XU |
| 29 | Game Changer ComfyUi #architecture #architectureschool  #ai #rendering #parametricdesign #comfyui | Alphonso Peluso | 1:10 | 2025-10-13 |  | comfyui, arq | ia-imagen | https://www.youtube.com/watch?v=KRldrZ1yzCA |
| 30 | The ONLY AI TOOL ARCHITECTS Will Ever Need \| UNLIMITED FREE \| AiriLAB 🔥 | Salmaan Mohamed | 16:10 | 2025-10-13 |  | llm, arq | ia-agentes-code | https://www.youtube.com/watch?v=sXOy03F8Pkk |
| 31 | GOOGLE Nano Banana Update ARCHITECTS Shouldn't MISS \| Step-By-Step Walkthrough | Salmaan Mohamed | 8:27 | 2025-10-13 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=v1fXmGYm_5s |
| 32 | The Rise of BIM 2.0: 9 Startups Redefining the Future of Architecture Software | ArchiTech Network | 20:15 | 2025-10-13 |  | arq | diseno-arq | https://www.youtube.com/watch?v=dturff3XgSk |

---

### ARQ/Rhino+Grasshopper

Archivo Takeout: `ARQ_Rhino+Grasshopper-vídeos.csv` · Videos: 31

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Fully automated dimensions with Grasshopper #grasshopper3d | How to Rhino | 0:25 | 2026-07-16 |  | rhino, grasshopper, n8n | software-arq | https://www.youtube.com/watch?v=vATO2GEwg_M |
| 2 | Rhino AI Is Here — and You’re Already Behind | Philipp Galvan Design | 10:31 | 2026-07-16 |  | rhino | software-arq | https://www.youtube.com/watch?v=66YU-W_MCzQ |
| 3 | NEW Rhino Plugin Changes Environmental Analysis | How to Rhino | 12:18 | 2026-06-24 |  | rhino | software-arq | https://www.youtube.com/watch?v=bikpynJGCN8 |
| 4 | Grasshopper for Advanced Users - Full Course | Gediminas Kirdeikis | 5:04:31 | 2026-04-12 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=DksmgSLtMww |
| 5 | AI Plugin for Grasshopper We’ve Been Waiting For | How to Rhino | 18:18 | 2025-11-29 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=4mr7thwfzKo |
| 6 | Blender Earth Modeler Add-on \| 3D Google Earth (City/Terrain) inside Blender | Imagiscope Tech | 5:24 | 2025-11-03 | Si | blender | software-arq | https://www.youtube.com/watch?v=80GrFXFOayE |
| 7 | How To Import ANY Location to Rhino | How to Rhino | 10:53 | 2025-11-03 |  | rhino | software-arq | https://www.youtube.com/watch?v=YtlK4046VRQ |
| 8 | How To Create Real-Time Renders with AI (synced to 3D model) | Design Input | 37:42 | 2025-10-28 |  | viz | diseno-arq | https://www.youtube.com/watch?v=GmXkrgqvWvk |
| 9 | Parametric Floor Plan  + Open Nest Exercise & Rhino Parametric Architecture tutorial | David Copete Parametric | 29:42 | 2025-10-25 | Si | rhino, arq, parametrico, planos | software-arq | https://www.youtube.com/watch?v=L_r6SroevxY |
| 10 | Viewing your Rhino model in Augmented Reality with Fologram in less than 10 mins! | ArchiTech Network | 8:14 | 2025-10-15 |  | rhino | software-arq | https://www.youtube.com/watch?v=Z8BAZANjB1s |
| 11 | Learn How To Create Animations In Grasshopper with the ATN Animation Challenge! | ArchiTech Network | 29:51 | 2025-10-15 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=BFAeDLHtruI |
| 12 | 📐 De Superficie a Sólido en Rhino \| 3 Métodos Eficientes 🚀 | Arkpe | 2:20 | 2025-10-15 |  | rhino | software-arq | https://www.youtube.com/watch?v=mPwZl6AOsm8 |
| 13 | Control Rhino and Grasshopper Control with Claude AI - MCP | Urban Decoders | 10:00 | 2025-10-14 |  | rhino, grasshopper, llm, agents | software-arq | https://www.youtube.com/watch?v=q1RuBmDKgyw |
| 14 | How to use ChatGPT to Create Designs in Rhino3d! AND Get Better Results! | Nate's Studio Desk | 23:19 | 2025-10-14 |  | rhino, llm | software-arq | https://www.youtube.com/watch?v=HlDzBzh0BZI |
| 15 | Stadium Design : reveal potentials of Parametric Design | ATELIER DESIGNA | 1:49 | 2025-10-14 |  | parametrico | diseno-arq | https://www.youtube.com/watch?v=DFgj0xbLCPk |
| 16 | Custom Models in UNREAL 5 and GOOGLE MAPS using Cesium ( Revit, Rhino, Sketchup) | Urban Decoders | 20:54 | 2025-10-14 |  | rhino, revit, unreal, sketchup | software-arq | https://www.youtube.com/watch?v=aKi1Q3JRn7U |
| 17 | Grasshopper for Beginners - Full Course | Gediminas Kirdeikis | 11:46:18 | 2025-10-14 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=b0elmzjWlE8 |
| 18 | Chat GPT for Grasshopper | The Different Design | 21:30 | 2025-10-14 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=yqo-vs8IqDE |
| 19 | Connecting Chat GPT with Grasshopper | Arturo Tedeschi | 14:22 | 2025-10-14 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=gL3B5KwZq2M |
| 20 | Dynamic Sections with Rhino 7 - Workflow | Gediminas Kirdeikis | 22:01 | 2025-10-14 |  | rhino | software-arq | https://www.youtube.com/watch?v=_haYBNgth_0 |
| 21 | Rhino for Architecture: Carve Building Envelope Using Sun Light (Rhino, Grasshopper, Ladybug) | Gediminas Kirdeikis | 38:02 | 2025-10-14 |  | rhino, grasshopper, arq | software-arq | https://www.youtube.com/watch?v=0GCAMgdOjo4 |
| 22 | GEOMETRIC WORKFLOWS in RHINO | Andrew Friedenberg | 17:59 | 2025-10-14 |  | rhino | software-arq | https://www.youtube.com/watch?v=GlQMmikoNJQ |
| 23 | Pixelate any shape like MVRDV or Bjarke Ingels (Grasshopper & SubD Tutorial) | Andrew Friedenberg | 32:45 | 2025-10-14 |  | rhino, grasshopper, arq | software-arq | https://www.youtube.com/watch?v=lyCQ-rCzC9A |
| 24 | Concepts: Parametric Architecture \| Edu-Archs | Edu-Archs | 11:33 | 2025-10-14 |  | arq, parametrico | diseno-arq | https://www.youtube.com/watch?v=F92tRbqFAO4 |
| 25 | _(sin titulo)_ |  |  | 2025-10-13 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=fVIuO-2e7fY |
| 26 | food4Rhino webinar: Designing apartment floor plans with PlanFinder (English) | McNeel Europe | 1:03:29 | 2025-10-13 |  | planos | diseno-arq | https://www.youtube.com/watch?v=NbeMHbvyHYw |
| 27 | Parametric Architecture Tiny Home Design Module Design Development Grasshopper Rhino 3D #grasshopper | David Copete Parametric | 3:10:04 | 2025-10-13 |  | rhino, grasshopper, arq, parametrico | software-arq | https://www.youtube.com/watch?v=c1jxgMnkIo8 |
| 28 | Stadium Base Form Overview Rhino and Grasshopper | David Copete Parametric | 18:51 | 2025-10-13 |  | rhino, grasshopper, parametrico | software-arq | https://www.youtube.com/watch?v=cwa90PFsKkk |
| 29 | #AI -Aided Architectural #Design Workflow #grasshopper #chatgpt #python #midjourney #lookx | GETnFORM | 0:16 | 2025-10-13 |  | rhino, grasshopper, midjourney, llm | software-arq | https://www.youtube.com/watch?v=DgcDM0wON8g |
| 30 | How To Design A Stadium With Grasshopper, Rhinoscript & Python #parametricdesign | ThinkParametric | 0:12 | 2025-10-13 |  | rhino, grasshopper | software-arq | https://www.youtube.com/watch?v=_1S8g-YaVzA |
| 31 | Why Rhino is KING for Innovative Architecture! | ArchiTech Network | 9:29 | 2025-10-13 |  | rhino, arq | software-arq | https://www.youtube.com/watch?v=N_5Ju9czZ-E |

---

### ARQ/Twinmotion-Unreal_Engine

Archivo Takeout: `ARQ_Twinmotion-Unreal_Engine-vídeos.csv` · Videos: 21

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Unreal Engine 5.8 for Architects - 2026 Full Course | Gediminas Kirdeikis | 10:24:36 | 2026-07-08 |  | unreal, arq | software-arq | https://www.youtube.com/watch?v=CnoC-v9xB_E |
| 2 | Twinmotion 2025.2 + ChatGPT = Next-Level Realism (Automotive Render Part 2) | Render Reboot | 9:24 | 2025-10-26 |  | twinmotion, llm, viz | software-arq | https://www.youtube.com/watch?v=VvT0ykZn6JY |
| 3 | Install Cesium in UE5.6 for Free \| No Google Maps API Key Needed | Unreal Fusion | 5:22 | 2025-10-14 |  | unreal | software-arq | https://www.youtube.com/watch?v=mkxpVZDGw50 |
| 4 | Custom Models in UNREAL 5 and GOOGLE MAPS using Cesium ( Revit, Rhino, Sketchup) | Urban Decoders | 20:54 | 2025-10-14 |  | rhino, revit, unreal, sketchup | software-arq | https://www.youtube.com/watch?v=aKi1Q3JRn7U |
| 5 | Twinmotion for Architecture - 2024 Full Beginner Course | Gediminas Kirdeikis | 6:10:37 | 2025-10-13 |  | twinmotion, arq | software-arq | https://www.youtube.com/watch?v=2aUUcsVnq_8 |
| 6 | #Twinmotion for Virtual Production #virtualproduction #papergirls | Twinmotion | 0:55 | 2025-05-12 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=_AQYAU_Gz6g |
| 7 | Master Twinmotion 2025.1 Renders with AI Workflow Step by Step Tutorial Full Guide | Render Reboot | 26:20 | 2025-04-08 |  | twinmotion, viz | software-arq | https://www.youtube.com/watch?v=ayVwROGzwRY |
| 8 | Mastering Twinmotion 2024.1.2 Creating Jaw-dropping Floor Plans! | Render Reboot | 14:11 | 2025-04-08 |  | twinmotion, viz, planos | software-arq | https://www.youtube.com/watch?v=WazHgQnXgmI |
| 9 | Lumen en Twinmotion - Tutorial de Twinmotion | Iscar Software de Arquitectura S.L | 9:11 | 2025-04-07 |  | twinmotion, arq | software-arq | https://www.youtube.com/watch?v=vQ5eovbi-mo |
| 10 | How to Create a Building Animation \| Twinmotion 2020 | Architecture Vanguard | 28:36 | 2025-04-06 |  | twinmotion, arq | software-arq | https://www.youtube.com/watch?v=lZO_CLfJiO4 |
| 11 | Twinmotion 2024.1.2 - Restaurant Rendering, Artificial Lights On/Off | Twinmotion Guru | 42:35 | 2025-04-02 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=AxhDbJFfI_s |
| 12 | Camera Animation Enhancements in Twinmotion 2025.1 \| Twinmotion Tutorial | Twinmotion | 6:48 | 2025-04-01 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=rxRp2UTQGgM |
| 13 | How to light a space with no windows \| Twinmotion Tutorial | Twinmotion | 5:02 | 2025-04-01 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=Bj-k7HFUbMw |
| 14 | Lumen rendering tips \| Twinmotion Tutorial | Twinmotion | 8:59 | 2025-04-01 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=C_9E4V6CzTw |
| 15 | How to visualize construction steps \| Twinmotion Tutorial | Twinmotion | 3:49 | 2025-04-01 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=wAUsN6vamGA |
| 16 | Beginner tips for creating cinematic videos \| Twinmotion Tutorial | Twinmotion | 4:30 | 2025-04-01 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=ebdoW9xBKcY |
| 17 | TWINMOTION Real-time 3d architecture visualization- note tool | Mohammad El Ashram | 10:28 | 2025-04-01 |  | twinmotion, llm, arq, viz | software-arq | https://www.youtube.com/watch?v=efQUw99yfow |
| 18 | Building Interactive 3D Configurators in Twinmotion 2025.1 \| Twinmotion Tutorial | Twinmotion | 24:12 | 2025-04-01 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=2pbTzjhX1Sc |
| 19 | Twinmotion 2024.1 - Download My User Library For Free | Twinmotion Guru | 2:23 | 2025-03-05 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=sOzyJfwsAHY |
| 20 | Twinmotion 2025.1 - Convert 2D images to 3D models with AI | Twinmotion Guru | 2:49 | 2025-03-05 |  | twinmotion, viz | software-arq | https://www.youtube.com/watch?v=gaUMtFulpPY |
| 21 | Twinmotion 2024.1 - Final Guide: How To Create Animations | Twinmotion Guru | 32:20 | 2025-02-04 |  | twinmotion | software-arq | https://www.youtube.com/watch?v=pTz0DH7nEjk |

---

### IA/Metaverso-VR/AR

Archivo Takeout: `IA_Metaverso-VR_AR-vídeos.csv` · Videos: 9

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | ¡META HACE CAMBIOS! 👉240 Hz en Quest 3, Half Life Alyx GRATIS con Steam Frame y Steam Link con CABLE | VrPatch | 6:40 | 2026-09-05 | Si | metaverso | diseno-arq | https://www.youtube.com/watch?v=69ekfLN0fjE |
| 2 | German Otto Bodenbender: Human and Machine: The Augmented Architect \| BIG \| ATN Summit 2026 | ArchiTech Network | 26:25 | 2026-06-23 |  | arq, charlas | diseno-arq | https://www.youtube.com/watch?v=tgO7k72g5ag |
| 3 | 20 EXPERIENCIAS INCREÍBLES en VR  para Meta Quest 3 y 3s que debes probar! 🍿 | NEXT Manu | 8:34 | 2026-02-27 |  | metaverso | diseno-arq | https://www.youtube.com/watch?v=j3Wl6L_RzN8 |
| 4 | VIAJAR por el MUNDO como Google Earth en REALIDAD VIRTUAL con Meta Quest 3 y 3s 🌎 | NEXT Manu | 8:05 | 2025-11-07 |  | metaverso | diseno-arq | https://www.youtube.com/watch?v=bO3en9O6tfc |
| 5 | LEARNING ARKIO \| DAY 1 \| OCULUS QUEST \| VR | Nikhil Bang | 16:33 | 2025-10-14 | Si | metaverso | diseno-arq | https://www.youtube.com/watch?v=EEqYvtw7J0E |
| 6 | Make your own Paint by Numbers in VR - Vermillion | Vermillion | 3:12 | 2025-10-14 |  | metaverso | diseno-arq | https://www.youtube.com/watch?v=fa1fexD5wrQ |
| 7 | Patrik Schumacher (Zaha Hadid Architects) talks about the Metaverse | BlessedArch | 1:03:45 | 2025-10-14 |  | arq, metaverso | diseno-arq | https://www.youtube.com/watch?v=VjGeAKsVB7Q |
| 8 | Visualizar modelo de Revit con Realidad Virtual en Twinmotion \| Meta Quest 3 para Arquitectura | De punto y línea | 16:33 | 2025-10-14 |  | revit, twinmotion, arq, metaverso | software-arq | https://www.youtube.com/watch?v=RJVoNYfYy-s |
| 9 | Metaverso: Oportunidades para la arquitectura, construcción y sector inmobiliario | Las Condes Design | 1:27:14 | 2025-10-14 |  | arq, metaverso | diseno-arq | https://www.youtube.com/watch?v=tX4WAiFJnSQ |

---

### libros

Archivo Takeout: `libros-vídeos.csv` · Videos: 6

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | 10 Free University Courses That Are Better Than Paid Ones | Shane Hummus | 14:46 | 2025-12-02 | Si | otros |  | https://www.youtube.com/watch?v=qHwIiwjrT1I |
| 2 | El Manifiesto Comunista, de Marx y Engels - explicación del libro | GusFai: Filosofía - Psicoanálisis - Psicología | 41:55 | 2025-02-27 |  | filosofia |  | https://www.youtube.com/watch?v=DuKcZEG8ITo |
| 3 | Café La República \| Utopía y desencanto. | La Once Diez | 40:54 | 2025-02-27 |  | libros | gestion | https://www.youtube.com/watch?v=ryCRA86WYKs |
| 4 | Rem Koolhaas's 'Delirious New York' — AB+C 108 — 1/3 | About Buildings + Cities | 1:11:32 | 2025-02-27 |  | libros | gestion | https://www.youtube.com/watch?v=XSR2UFpjB-A |
| 5 | The embodied image - Juhani Pallasmaa, architect, Helsinki | Lecture replay - Archizoom @EPFL Architecture | 59:11 | 2025-02-27 |  | arq | diseno-arq | https://www.youtube.com/watch?v=ooyToG4ennU |
| 6 | Audio libro- La Mano Que Piensa, Juhani Pallasmaa   \|VOZ Beatriz Herrera\| LIAR 2021A | BEATRIZ AZUCENA HERRERA BOTELLO | 3:41:26 | 2025-02-27 |  | libros | gestion | https://www.youtube.com/watch?v=HATZHCeAdcM |

---

### 🛒MKT📈SEM/SEO

Archivo Takeout: `🛒MKT📈SEM_SEO-vídeos.csv` · Videos: 2

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Marketing Audit Pro - Clase 2 - Auditorías en vivo | The BIG | 1:56:05 | 2025-10-18 |  | marketing | gestion | https://www.youtube.com/watch?v=aTCKS38dRss |
| 2 | Marketing Audit Pro - Clase 1 - Marketing Digital desde Cero | The BIG | 1:18:17 | 2025-10-18 |  | marketing | gestion | https://www.youtube.com/watch?v=uJTqd5lVnAM |

---

### IA/🧩Vibe_Coding

**Tu descripcion:** Rol: creación de sistemas, plataformas o productos. Herramientas: Bubble, FlutterFlow, WeWeb, Xano, Supabase, Airtable, Glide, Replit, Framer, etc. Enfocado en: front + lógica + bases de datos + APIs → productos interactivos.

Archivo Takeout: `IA_🧩Vibe_Coding-vídeos.csv` · Videos: 18

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | La forma REAL de programar con IA en 2026 | MoureDev by Brais Moure | 16:00 | 2025-10-19 | Si | llm, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=uquw8yUKaYM |
| 2 | Build a $1M Legal AI Assistant App (Lovable & N8N) | Damian Malliaros | 23:30 | 2025-10-15 |  | vibe-coding, n8n | ia-agentes-code | https://www.youtube.com/watch?v=FYVhsnLH4kg |
| 3 | Cursor AI Agents Work Like 10 Developers (Cursor VP Live Demo) | Greg Isenberg | 29:42 | 2025-10-15 |  | agents, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=8QN23ZThdRY |
| 4 | Cursor Vibe Coding Tutorial - For COMPLETE Beginners (No Experience Needed) | Tech With Tim | 1:05:53 | 2025-10-15 |  | vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=8AWEPx5cHWQ |
| 5 | ⚡️Programación para Principiantes: Python Primeros Pasos | Ing.Wilmer Planchez | 31:51 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=xl3vlFObhFI |
| 6 | Más allá del contexto - Divide y vencerás | VIBECODING HACKS | 8:06 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Bnd-pheoS8c |
| 7 | El Curso de Programación que SÍ que Tienes que Hacer | MoureDev by Brais Moure | 6:55 | 2025-10-14 |  | vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=MCgXcI4fR4M |
| 8 | Code Anything with Perplexity, Here's How | David Ondrej | 21:44 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Xd2b81Q2qL0 |
| 9 | ¡El NUEVO AI Studio Vibe Coder de Google es Una LOCURA! | IA Innova | 10:03 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=wkqAT56NbAY |
| 10 | Curso de Desarrollo con IA Gratis - Clase 2 | MoureDev by Brais Moure | 1:30:41 | 2025-10-14 |  | llm, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=ssPPIY3EJcc |
| 11 | Lovable Livestream - Introducing Lovable Cloud + AI | Lovable | 1:03:28 | 2025-10-14 |  | vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=Xqams9Ao8bI |
| 12 | Curso de Desarrollo con IA Gratis - Clase 3 + Presentación Máster de Desarrollo con IA | MoureDev by Brais Moure | 1:42:45 | 2025-10-14 |  | llm, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=NijkYdsCfjA |
| 13 | Google Gemini CLI Is FREE & Crazy Powerful: Real World Coding Test & First Impressions | aiwithbrandon | 35:04 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=CqL5kB8pOfo |
| 14 | OpenCode: FASTEST AI Coder + Opensource! BYE Gemini CLI & ClaudeCode! | WorldofAI | 10:34 | 2025-10-13 |  | llm, opencode | ia-agentes-code | https://www.youtube.com/watch?v=hJm_iVhQD6Y |
| 15 | I Create Dashboard in One Minute using Python \| Python for beginners \| #python #coding #programming | Code Nust | 1:04 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=zvDvixsjOS8 |
| 16 | 5 FREE AI APIs You Should Use #ai #developer #llm #softwaredeveloper #code #coding | PlivoAI | 0:45 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=mni63pkxZfA |
| 17 | This new AI tool is INSANE (and it’s FREE) | Dan the creator | 20:58 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Q0A9j1mPh4k |
| 18 | I Built a FULL Web App with n8n, Lovable & Supabase (NO CODE!) | Zubair Trabzada \| AI Workshop | 32:22 | 2025-10-13 |  | vibe-coding, n8n | ia-agentes-code | https://www.youtube.com/watch?v=niMkgYRZfMk |

---

### IA/🤖gen_Agents

**Tu descripcion:** LLM(evolucion); GPTs personalizados  Agents de OpenDevin, CrewAI, LlamaIndex, AutoGPT  Casos prácticos en flujo de trabajo(n8n); Multi-agent systems (redes de agentes colaborativos); Autoevaluación, feedback loops y conciencia sintética

Archivo Takeout: `IA_🤖gen_Agents-vídeos.csv` · Videos: 23

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | La Actualización de N8N que Cambiará para Siempre las Agencias de IA | Claudio Conde | 13:42 | 2025-10-18 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=R5Qz76n6UeE |
| 2 | Building a Mobile Backend with N8N & AI Agent Tools | DailyAi.Studio | 19:38 | 2025-10-15 |  | llm, agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=jOEI48y59wk |
| 3 | Tutorial N8N: ¡Construir Chatbot en WhatsApp! (Método fácil) | Virola | 15:48 | 2025-10-15 |  | n8n, whatsapp | ia-agentes-code | https://www.youtube.com/watch?v=M5ZSjBnACtM |
| 4 | Cursor AI Agents Work Like 10 Developers (Cursor VP Live Demo) | Greg Isenberg | 29:42 | 2025-10-15 |  | agents, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=8QN23ZThdRY |
| 5 | 3 Game-Changing NEW AI Agent Updates in n8n 🔥 | Zubair Trabzada \| AI Workshop | 13:12 | 2025-10-15 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=PnboBlU6huU |
| 6 | Build the Ultimate Internal AI Agent for Business Automation (n8n, free templates) | Bo Sar | 37:43 | 2025-10-14 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=mcOaNuMehQI |
| 7 | I Built a Marketing Team with 1 AI Agent and No Code (free n8n template) | Nate Herk \| AI Automation | 33:56 | 2025-10-14 |  | agents, n8n, marketing | ia-agentes-code | https://www.youtube.com/watch?v=ldETapkr8Hg |
| 8 | How to Build & Sell AI Agents: Ultimate Beginner’s Guide | Liam Ottley | 3:50:40 | 2025-10-14 |  | agents | ia-agentes-code | https://www.youtube.com/watch?v=w0H1-b044KY |
| 9 | Cómo Empezar Una Agencia de IA (De Cero a Tu Primer Cliente) | Agustín Medina \| AI Agency Academy | 13:50:30 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=D8o3m6GbwGw |
| 10 | 10 Insane AI Agent Use Cases in n8n! (steal these) | Jono Catliff | 16:30 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=Dt6u-yFEpsk |
| 11 | 3 años Dirigiendo una Agencia de IA de Éxito en 28 Minutos | Claudio Conde | 28:07 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=EFIBb_RjRh0 |
| 12 | Agent Zero: Agente de IA que aprende y se adapta solo (Open Source) \| Tutorial paso a paso | Conciencia Artificial | 16:31 | 2025-10-13 |  | llm, agents | ia-agentes-code | https://www.youtube.com/watch?v=oFCbFGGlmNE |
| 13 | How to Automate Replies to Instagram DMs With AI (n8n + ManyChat) | Yashica Jain | 28:13 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=WObjwvp1Rd8 |
| 14 | Copia y Pega estos 3500 Workflows de Agentes de IA de n8n GRATIS | Claudio Conde | 12:26 | 2025-10-13 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=8nHKX6Bbk-4 |
| 15 | Build & Sell n8n AI Agents (8+ Hour Course, No Code) | Nate Herk \| AI Automation | 8:26:39 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=Ey18PDiaAYI |
| 16 | Don't Sell N8N Workflows, Sell AI Infrastructure - Here's How (Massive Opportunity) | Ethan Nelson | 14:08 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=GKCBpj9FQXU |
| 17 | Project Management AI Agent n8n | Alex Safari \| AI for Small Business | 34:40 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=TzZEgHeLuxE |
| 18 | Stop Selling n8n Agents, Sell AI Systems - Here’s How (Insane Opportunity) | Nick Puru \| AI Automation | 18:48 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=VQRiwK7q1Do |
| 19 | Say Goodbye to ClickUp: Get Your Own AI Project Manager – No SaaS, No Limits, With n8n and Baserow | The Automated Ai | 6:46 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=DZCazlOh7Fk |
| 20 | Build your own AI Assistant Project Management Workflow with n8n Baserow LinkedIn Posting Automation | The Automated Ai | 25:22 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=T9elG0EoGQ4 |
| 21 | How to Build AI Agents with n8n in 2025! (Full Course) | AI Foundations | 5:09:38 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=geR9PeCuHK4 |
| 22 | Bonus - Hoja de ruta para lanzar tu agencia | NocodeHackers | 15:12 | 2025-10-13 |  | llm, agents | ia-agentes-code | https://www.youtube.com/watch?v=j7A-MwU2bUk |
| 23 | N8N Full Tutorial: Easy Google AI Agent in 2025 For Beginners (No Code) | AI Andy | 19:03 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=ExBnzrlkt00 |

---

### IA/🧠gen_Txt (LLMs)

**Tu descripcion:** Large Language Models: ChatGPT, Gemini, Claude, NotebookLM; Comparativas de modelos  Casos de uso (escritura, resúmenes, educación)  Prompt engineering básico y avanzado  Integraciones con herramientas de texto

Archivo Takeout: `IA_🧠gen_Txt (LLMs)-vídeos.csv` · Videos: 30

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | TOP uses of Google Earth with AI | Urban Decoders | 8:09 | 2025-11-03 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=JNVV4sQ_2dw |
| 2 | 10 COSAS INCREÍBLES que puedes hacer GRATIS con las IAs de Google (Gemini, NotebookLM, OPAL, Veo…) | Migue Baena IA | 27:37 | 2025-10-24 | Si | descartado |  | https://www.youtube.com/watch?v=hUnNum9p0ME |
| 3 | Curso Completo ChatGPT de cero (Actualizado 2025) | Daxus Latam | 31:06 | 2025-10-15 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Jr4aLb-8fOA |
| 4 | Creé 7 Apps con Google AI Studio | Nardella | 9:19 | 2025-10-15 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=u8LiZSr5GFU |
| 5 | 🚨 El Nuevo GROK 4 de Elon Musk es una locura (y GRATIS) | Inteligencia Artificial Noticias | 8:02 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=QU0tir7GrHs |
| 6 | n8n with ComfyUI AI Image Automation for Beginners (NOCODE) | Ahmad \| AI Automation | 17:48 | 2025-10-14 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=nuUf3f36RUE |
| 7 | Web Scraping with GPT-4 Vision AI + Puppeteer is Mind-Blowingly EASY! | ByteGrad | 24:14 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=fjP328HN-eY |
| 8 | Controlling Blender with my voice using LLM | Polyfjord Deep Dive | 15:33 | 2025-10-14 |  | blender, llm | software-arq | https://www.youtube.com/watch?v=ytomieYqUCQ |
| 9 | How to create any n8n workflow using ChatGPT | David Ondrej | 28:54 | 2025-10-14 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=lZuxqbw8IX4 |
| 10 | 6 ChatGPT SECRETS that every ARCHITECT Should Know \| OpenAI 4.0 Image Generator 🔥 | Salmaan Mohamed | 10:30 | 2025-10-14 |  | llm, arq | ia-agentes-code | https://www.youtube.com/watch?v=GN8IK2Wbw8E |
| 11 | ¡Este es el GEMINI del FUTURO! 🤯 Y muchas MÁS NOVEDADES | Xavier Mitjana | 43:43 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=7H5RiNqd0Cs |
| 12 | 🧠Te ENSEÑO ChatGPT desde CERO...! ► GUÍA para PRINCIPIANTES (Descarga y Configuración) | bydavidparra | 12:11 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=_imU9QnfeR8 |
| 13 | 🧠 RENDERS con ChatGPT para DISEÑO ARQUITECTONICO ► Nueva Creación de Imágenes | bydavidparra | 10:49 | 2025-10-14 |  | llm, viz | ia-agentes-code | https://www.youtube.com/watch?v=s47jwJcdFuI |
| 14 | EASIEST Way to Fine-Tune a LLM and Use It With Ollama | Warp | 5:18 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=pxhkDaKzBaY |
| 15 | _(sin titulo)_ |  |  | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=PGrc4wSmqfc |
| 16 | How to use Openrouter (Access Every LLM At Once) | TheAIGRID | 12:26 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=XK8Kp4Tkb88 |
| 17 | I connected Claude AI to Blender 3D...Mind-Blowing Results (MCP) | Max Novak | 15:50 | 2025-10-13 |  | blender, llm, agents | software-arq | https://www.youtube.com/watch?v=r7H60u0kHRA |
| 18 | Project Planning for Beginners \| Google Project Management Certificate | Grow with Google | 36:55 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=hHPAc0LFfZA |
| 19 | Activé los agentes de Perplexity… y esto se descontroló | Migue Baena IA | 23:09 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=ynx_5uWL1ZM |
| 20 | ChatGPT Image Hacks To Build Your Brand Faster (Full Tutorial) | Andrew Lane \| Design Hacker | 23:09 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=SF5K4weDGlg |
| 21 | The Best AI Meeting Notetakers of 2026 | Automation Helpers | 10:18 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=0inVCwpbP3s |
| 22 | This AI POSTS Viral LinkedIn Content FOR You | Zubair Trabzada \| AI Workshop | 25:50 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=GMdqqgRJL-8 |
| 23 | 10 COSAS INCREÍBLES que Gemini puede hacer por ti GRATIS (y no estás aprovechando) | Migue Baena IA | 26:26 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=ppzx6NzHwH0 |
| 24 | How Power BI Developers SHOULD use ChatGPT | Power BI Park | 16:28 | 2025-10-13 |  | llm, gestion | ia-agentes-code | https://www.youtube.com/watch?v=qDoAhWOaTdM |
| 25 | NotebookLM revoluciona la forma de estudiar y aprender | Emowe | 34:41 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=XdxOIMdDA9o |
| 26 | ¡Google arrasa con su Nueva IA GRATIS! Estos 8 casos lo demuestran | Alejavi Rivera | 25:37 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=sOwtfYEGFQw |
| 27 | La NUEVA función de NotebookLM + Gemini 2.5 🤯 \| 5 FLUJOS REALES desde 1 solo informe | Migue Baena IA | 19:38 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Fkb0zMos03A |
| 28 | Google actualiza la FUNCIÓN MÁS POTENTE de GEMINI... ¡GRATIS! 🤯 | Xavier Mitjana | 11:17 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=DHEiMSkwhUw |
| 29 | Google acaba de soltar 4 bombas en Gemini… y ya puedes usarlas | Migue Baena IA | 19:47 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=70mlfY10hyw |
| 30 | Google AI Studio Tutorial: 10 Funciones Ocultas de Gemini (Guía 2025) | 💡Tecno Curiosos💡 | 29:22 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=HxSeuVRXtTo |

---

### IA/⚙️Workflows(Autom.)

**Tu descripcion:** Automatizaciones (n8n, Make, Zapier); Integraciones de IA Integraciones en tiempo real (API, webhooks, pipelines creativos) con herramientas (Google Workspace, Notion, Discord, etc.);  Diseño de pipelines de trabajo IA-humanos;

Archivo Takeout: `IA_⚙️Workflows(Autom.)-vídeos.csv` · Videos: 91

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | [Workshop] Arquitectura multi-agente: De 0 a AI Engineer en 30 minutos | LIDR - Carreras potenciadas por IA | 0:53 | 2026-08-18 |  | llm, arq | ia-agentes-code | https://www.youtube.com/watch?v=4NhfzVanyqQ |
| 2 | Crea Tu Propio RAG personal en Claude Code \| Paso a Paso | Agustín Medina \| AI Agency Academy | 17:08 | 2026-03-18 | Si | llm, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=74iB941XRPk |
| 3 | Antigravity: Crea Webs Animadas en 15 Minutos (Sin Código) | Alvaro Morales \| IA | 14:48 | 2026-03-16 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=HUg7Uns3Nc8 |
| 4 | Claude Code + Nano Banana 2 = Insane $10,000 Websites | Jack Roberts | 22:48 | 2026-03-15 |  | nanobanana, llm, vibe-coding | ia-imagen | https://www.youtube.com/watch?v=TZUTe7s11-I |
| 5 | Google Antigravity + N8N: Crea y Automatiza TODO Gratis (Paso A Paso) | Alvaro Morales \| IA | 22:42 | 2026-03-14 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=7gvlm6ZaJEQ |
| 6 | CODE vs NO-CODE para construir una página web en 2026 | NocodeHackers | 48:55 | 2026-02-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=O1kwIU26JgQ |
| 7 | Te Enseño la Guía Definitiva de Google Antigravity: De Principiante a Experto | Josema Fernández \| IA | 50:15 | 2026-02-12 |  | llm, vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=liqfwPC4FmA |
| 8 | Curso completo: Agentic Workflows (Antigravity) @googleantigravity | Nicolas Dubois | 1:32:59 | 2026-02-12 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=9G5efpw8pp4 |
| 9 | Google Antigravity FULL COURSE 4 HOURS (Build & Automate Anything) | Julian Goldie SEO | 4:42:51 | 2026-02-08 |  | marketing | gestion | https://www.youtube.com/watch?v=BeRnLV8EZJs |
| 10 | NotebookLM + Google Antigravity: Build ANYTHING! (For FREE) | Ahmad \| AI Automation | 13:24 | 2026-02-08 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=VAFp6Q98zSU |
| 11 | I Built an Automated Video Editing Workflow with n8n and FFmpeg (Full Breakdown) | Ahmad \| AI Automation | 13:02 | 2026-02-04 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=utRom_HkMFg |
| 12 | 🔴 Curso GRATIS IA 2026 - Día 1 - ChatGPT, Projects y GPTs | Inteligencia Artificial | 1:36:32 | 2026-01-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=BF4fQlUDC7s |
| 13 | Nuevo MCP en N8N: Construí un Chatbot que Usa tus Workflows en Minutos | Nicolas Dubois | 13:39 | 2025-12-07 |  | llm, agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=z373oesubj4 |
| 14 | Google Gemini 3 Pro + N8N: Analizá Videos y Creá Contenido en Minutos | Nicolas Dubois | 8:41 | 2025-12-02 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=SYZkBz9ab0w |
| 15 | Probando AI Workflow Builder de N8N: Creá Agentes y Flujos Solo con Texto | Nicolas Dubois | 9:25 | 2025-10-24 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=FipBT2kPnjM |
| 16 | I Built a Photoshop AI Agent That Uses Google's New NanoBanana #n8n #artificialintelligence | Nate Herk \| AI Automation | 1:38 | 2025-10-19 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=TWvjqpk3uSQ |
| 17 | El juego para aprender a trabajar con Git | MoureDev by Brais Moure | 0:19 | 2025-10-18 |  | vibe-coding | ia-agentes-code | https://www.youtube.com/watch?v=_wenMYRYmOw |
| 18 | Consigue un Servidor Gratis para siempre ⏳: Tutorial Paso a Paso (Oracle Free Tier) 💻🔥 | Dev Knives | 23:58 | 2025-10-18 |  | hardware | gestion | https://www.youtube.com/watch?v=l0tSPtSCp7M |
| 19 | 2 Ways To Get Free AI API Keys (Unlimited) \| Gemini, DeepSeek, Kimi, Claude & More | Astro K Joseph | 9:40 | 2025-10-15 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=E14hUveM4us |
| 20 | Tutorial N8N: ¡Construir Chatbot en WhatsApp! (Método fácil) | Virola | 15:48 | 2025-10-15 |  | n8n, whatsapp | ia-agentes-code | https://www.youtube.com/watch?v=M5ZSjBnACtM |
| 21 | Scrapea Cualquier Web con IA + N8N + Firecrawl y crea tu propia newsletter automática | VA360 \| @Valen | 45:40 | 2025-10-15 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=gCWWvs3EIjc |
| 22 | Build a Micro-SaaS / App with N8N – Stop Selling Automations, Start Selling Products | Automation-Tribe | 8:23 | 2025-10-15 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=XYQmc2uQuz8 |
| 23 | 🟡 La MEJOR Forma de Usar DeepSeek en Local Junto a n8n para automatizar lo que sea | aDevSays | 16:00 | 2025-10-15 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=Krp5GCb7mXE |
| 24 | N8N CURSO COMPLETO 6 HORAS – Automatiza, Crea y Vende Agentes IA | Agustín Medina \| AI Agency Academy | 6:44:49 | 2025-10-15 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=SF8Ddp0RaF8 |
| 25 | DON’T Sell AI Agents, Sell AI Operating Systems Instead | Jack Roberts | 16:14 | 2025-10-14 |  | agents | ia-agentes-code | https://www.youtube.com/watch?v=pPU8jcsrfqY |
| 26 | N8N Full Tutorial: Building AI Agents in 2025 for Beginners! | AI Foundations | 31:43 | 2025-10-14 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=ZbIVOy_GPyQ |
| 27 | HOW TO CONNECT CLICKUP TO N8N – STEP BY STEP | The West Reviews | 1:12 | 2025-10-14 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=5rTnsona19o |
| 28 | Connect ComfyUI and n8n - Step-by-Step Guide | Gary Judge | 9:20 | 2025-10-14 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=AOjxHMMck7s |
| 29 | Run Supabase 100% LOCALLY for Your AI Agents | Cole Medin | 29:36 | 2025-10-14 |  | agents | ia-agentes-code | https://www.youtube.com/watch?v=pOsO40HSbOo |
| 30 | The 9 Best Ways to Scrape Any Website in N8N | Nick Saraev | 1:08:45 | 2025-10-14 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=y-eEbmNeFZo |
| 31 | Scrape ANY Website for FREE with Crawl4AI + n8n (No Code) | Mahmut Kasimoglu | 43:33 | 2025-10-14 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=1CDGpbZItiY |
| 32 | _(sin titulo)_ |  |  | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Wice8TGRgKc |
| 33 | 7 Best Construction Project Management Software 2026 (Full Demo) | Business Solution | 16:29 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=fZm4rEtkPBc |
| 34 | How to Deploy n8n on Google Cloud Free Tier \| Complete n8n Self-Hosting Tutorial | Asif Syed | 17:08 | 2025-10-14 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=NNTbwOCPUww |
| 35 | 😱 Instala N8N sin pagar ni un peso PASO a PASO 👌 | CodingTube | 3:42 | 2025-10-14 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=QCinm3x-90o |
| 36 | n8n with ComfyUI AI Image Automation for Beginners (NOCODE) | Ahmad \| AI Automation | 17:48 | 2025-10-14 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=nuUf3f36RUE |
| 37 | Next-Level AI Web Scraping: ScrapeGraphAI Tutorial | Made By Agents | 23:44 | 2025-10-14 |  | agents | ia-agentes-code | https://www.youtube.com/watch?v=4_PBPoaoYKA |
| 38 | Web Scraping with GPT-4 Vision AI + Puppeteer is Mind-Blowingly EASY! | ByteGrad | 24:14 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=fjP328HN-eY |
| 39 | How to create any n8n workflow using ChatGPT | David Ondrej | 28:54 | 2025-10-14 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=lZuxqbw8IX4 |
| 40 | IA WORKFLOWS: Curso Gratis de Inteligencia Artificial con Certificado (Jon Hernández y Romuald Fons) | The BIG | 4:07:44 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=kUBxSxb8eOQ |
| 41 | Getting Started with AI Automation: Your easy start with Make AI Tools | Make | 6:52 | 2025-10-14 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=XguXU3NjnpE |
| 42 | We Tested & Reviewed the 15 Top Project Management Tools \| Our Top Recommendations Revealed ✅ | ClickUp | 11:58 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=8zCQ2W1CphE |
| 43 | Turn Your Miro Board Into a PDF 🙌🏻 | Miro | 1:04 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=UzJLjaG2uG8 |
| 44 | Los Nuevos MCPs Nativos son el Futuro de la IA: Conecta Gmail, Airtable, Calendar y 200+ Apps | Víctor Pérez | 11:55 | 2025-10-13 |  | llm, agents | ia-agentes-code | https://www.youtube.com/watch?v=wZHNHkWFaOY |
| 45 | ClickUp Tutorial 2026: Complete Guide From Beginner To Advanced (Verified Power User) | Antonio Monteiro | 56:50 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=DjeUeK9b-hI |
| 46 | How to use ClickUp as a CRM (ClickUp CRM Tutorial) | Stewart Gauld | 18:22 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=2iVv455dc6A |
| 47 | API Mercado Libre desde Cero. Crear Aplicación, Obtener Token, Primeras Peticiones usando Postman | miguelsanchezco | 39:56 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=lvPAGzUFacE |
| 48 | 10 Project Management Tools You Didn't Know (and Why You Need Them) | Tool Finder | 13:03 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=VscFv_9PYpc |
| 49 | Make n8n Public — Free Production Setup with Docker + Ngrok (No Domain, No Cost!) | Zero2Launch \| AI Automation | 14:18 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=RvAD2__YYjg |
| 50 | 🚀 n8n + Firecrawl MCP: "Text to Results" - Easily Scrape ANY Websites, Trending Products and News! | Zero2Launch \| AI Automation | 8:59 | 2025-10-13 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=Ejd11WE6qaw |
| 51 | I Found A Free VPS That No One Knows! (16GB RAM, 8 CPU) | PawnHoster | 3:21 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=sz4-c1vs0bo |
| 52 | Paying for software is stupid… 10 free and open-source SaaS replacements | Fireship | 6:23 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=e5dhaQm_J6U |
| 53 | Replace Your Expensive Cloud Tools With These (Self-Hostable) Alternatives | Simon Høiberg | 7:23 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=vpiiqbpdkNk |
| 54 | How To Get A Free Cloud Server Forever? | Dmitry Lambert | 12:04 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=1MIarVwoFlg |
| 55 | Project Planning for Beginners \| Google Project Management Certificate | Grow with Google | 36:55 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=hHPAc0LFfZA |
| 56 | The BEST 10 n8n Apps Released in 2025 (I Wish I Knew Sooner) | Jono Catliff | 26:40 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=hpagfM-r2Bs |
| 57 | 7 Proyectos de Automatización con Python que Debes Probar | Código Espinoza - Automatiza tu Vida | 0:43 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=PBQV2gsgSKs |
| 58 | _(sin titulo)_ |  |  | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=D-hRe1Ssqq4 |
| 59 | Easily Automate Business Tasks – No-Code Automation Course | freeCodeCamp.org | 3:00:39 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=5kJv254sebQ |
| 60 | Mercadolibre API escaneo de productos: Cómo interactuar con la API de MercadoLibre Chile Parte 2 | Gabriel Luces | 5:09 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=-u9qcjjKBas |
| 61 | Mercadolibre API escaneo de productos: Cómo interactuar con la API de MercadoLibre Chile | Gabriel Luces | 2:31 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=6xj6NygJQVo |
| 62 | Mercado Libre Web Scraping en Google Sheets con API | MatchKraft-es | 1:03 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=76TB5s1H8rE |
| 63 | Crawl4AI: The Ultimate AI Website Scraping Guide | Mervin Praison | 7:36 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=KAvuVUh0XU8 |
| 64 | AI YouTube Videos on Autopilot \| Local Workflow with n8n + ComfyUI | Brousla Workflows | 17:34 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=GWmK5igoEZ0 |
| 65 | How to Connect ComfyUI to N8N (Best Method) | Mindly Nova | 1:40 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=_WpbBIEtJUs |
| 66 | How to Connect n8n to ComfyUI on Runpod \| $0.15 for 24GB VRAM \| Step-By-Step Tutorial | Dorian Oslov \| The Decode AI | 35:00 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=RgrEAge_5Kk |
| 67 | The SHOCKING Truth About Hosting n8n in the Cloud for Free | Zero2Launch \| AI Automation | 4:05 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=lzIWU33E-UE |
| 68 | Curso N8N desde cero, creando un asistente virtual con Whatsapp + Google Calendar + OPENAI | Pildoras de programación | 1:38:41 | 2025-10-13 |  | n8n, whatsapp | ia-agentes-code | https://www.youtube.com/watch?v=p3gz4pFxL4U |
| 69 | The Best Free Project Management Tool | Damian Mathew (Badger) | 9:21 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=RlWzYbxC05s |
| 70 | Huly \| Open-source replacement for Linear, Jira, Slack & Notion | Huly | 3:54 | 2025-10-13 |  | gestion | gestion | https://www.youtube.com/watch?v=WKmpm0ms_Sg |
| 71 | Build AI-Powered Project Management Tools (Full Guide) | Blazing Zebra | 14:31 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=rbVTTZPbGfw |
| 72 | Set up Google Credentials in n8n in 5 minutes (2025) | Nate Herk \| AI Automation | 4:43 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=3Ai1EPznlAc |
| 73 | Say Goodbye to ClickUp: Get Your Own AI Project Manager – No SaaS, No Limits, With n8n and Baserow | The Automated Ai | 6:46 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=DZCazlOh7Fk |
| 74 | 🔥100% FREE LLM Setup in n8n – No OpenAI, No Tokens | Zero2Launch \| AI Automation | 8:03 | 2025-10-13 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=5vX_YwME8TM |
| 75 | n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code | Cole Medin | 33:46 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=c5dw_jsGNBk |
| 76 | Only 1% of n8n Builders Know This Node Exists (LangChain Code Node) | Bart Slodyczka | 20:31 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=4o0AJYBEiBo |
| 77 | Connect N8N and ClickUp in 60 Seconds: Automate Your Workflow | Austin Reed \| Horizon Dev | 0:54 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=5Kx38hRDnGk |
| 78 | Cómo automatizar tareas con solo un audio en Click Up fácil y rápido usando N8N | Ale Vogeler | 30:15 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=2lO0Iif8jnA |
| 79 | 5 FREE AI APIs You Should Use #ai #developer #llm #softwaredeveloper #code #coding | PlivoAI | 0:45 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=mni63pkxZfA |
| 80 | This Social Media AI System Creates & Posts Unique Content | Jack Roberts | 24:07 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=PHjdXFW0y04 |
| 81 | Create Unlimited Viral Instagram Posts (One Click) | Jack Roberts | 26:31 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=-E0kaamo3uw |
| 82 | Automatizá tu creatividad: ComfyUI \| n8n \| Vercel V0 | Morfeo Academy | 42:29 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=7n7A9emeiVQ |
| 83 | _(sin titulo)_ |  |  | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=-6uPrD1rfeQ |
| 84 | AI Thumbnail Generator for YouTube in ONE Click! (No Photoshop Needed) | Zero2Launch \| AI Automation | 4:54 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=RXO2YKdPMGI |
| 85 | Esta IA Crea Contenido Diario Para Redes Sociales (100% automático) | Adrián Sáenz | 48:07 | 2025-10-13 |  | llm, n8n | ia-agentes-code | https://www.youtube.com/watch?v=MGvUGEk1O9Y |
| 86 | n8n + OCR + AI: Automatically Rename & Sort Your Files (No-Code Automation) | Alexandru Dragomir | 1:46 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=7PvIObFo-s4 |
| 87 | Cómo conectar n8n con los NUEVOS Nodos GOOGLE: Crea Videos, Imágenes y Texto | Víctor Pérez | 5:53 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=DRwGZZXykDM |
| 88 | Cómo Empezar Una Agencia de IA (De Cero a Tu Primer Cliente) | Agustín Medina \| AI Agency Academy | 13:50:30 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=D8o3m6GbwGw |
| 89 | How To Scrape Any Website Without Paying For Api's In n8n (Free Workflow) | SW Automation | 20:51 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=hTWz1-WbE5M |
| 90 | Seriously, please watch this before you start learning n8n | The AI Architects \| Tom Crawshaw | 6:49 | 2025-10-13 |  | n8n, arq | ia-agentes-code | https://www.youtube.com/watch?v=ofC4OeNjDx8 |
| 91 | 🔴 Flujos de trabajo con IA - DÍA 2 IA WORKFLOWS | Inteligencia Artificial | 1:19:08 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=H1WCEVNiv1M |

---

### IA/🎨gen_Img

**Tu descripcion:** Inteligencia Artificial Generativa (generación de imágenes, renders, ilustraciones, estilos.) **ComfyUI** (flujos .json, outputs)  Stable Diffusion, Leonardo, PromeAI, Playground, Midjourney, etc.

Archivo Takeout: `IA_🎨gen_Img-vídeos.csv` · Videos: 71

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Model Jam: Latest Image & Video Model Releases | ComfyUI | 55:07 | 2026-10-07 | Si | comfyui | ia-imagen | https://www.youtube.com/watch?v=7V7Aazicx-s |
| 2 | Finally! New best local AI image editor is here | AI Search | 19:38 | 2026-10-06 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=BaE6UBfNdQk |
| 3 | AI x Archviz Free ComfyUI FLUX2 x LTX 2.5 Workflow | Paul Hansen | 30:01 | 2026-10-03 |  | comfyui, viz | ia-imagen | https://www.youtube.com/watch?v=946yTMjz-go |
| 4 | ComfyUI for Animation: Keyframe Exploration at Any Camera Angle (GPT Image 2) | ComfyUI | 0:57 | 2026-10-03 | Si | comfyui | ia-imagen | https://www.youtube.com/watch?v=6Jzr81R7sE4 |
| 5 | 3 AI workflows I actually use as an Architect | Show It Better | 14:49 | 2026-09-04 | Si | arq, agents | ia-agentes-code | https://www.youtube.com/watch?v=lEfSoR5JCaQ |
| 6 | Building a Python API for Comfy UI with Gradio | Code Crafters Corner | 38:26 | 2026-08-16 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=yspMVTL08Rc |
| 7 | Run ComfyUI From Claude/Cursor with Comfy MCP | ComfyUI | 57:11 | 2026-07-15 |  | comfyui, llm, agents, vibe-coding | ia-imagen | https://www.youtube.com/watch?v=sX2sJ5-4MS4 |
| 8 | VIDEOS EN MASA con VEO 3.1 GRATIS: La Nueva IA que lo hace en AUTOMÁTICO | Tutoriales Informáticos + IA | 12:57 | 2026-03-20 |  | video-ia, llm, n8n | ia-video-audio | https://www.youtube.com/watch?v=m9E1ihTxxls |
| 9 | Claude Code + Nano Banana 2 = Insane $10,000 Websites | Jack Roberts | 22:48 | 2026-03-16 |  | nanobanana, llm, vibe-coding | ia-imagen | https://www.youtube.com/watch?v=TZUTe7s11-I |
| 10 | EJECUTA IA en LOCAL GRATIS 👉 ¡Genera Código, Vídeo, Imágenes y Texto! | Dot CSV Lab | 27:33 | 2025-10-24 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=kVQjUXHJZkE |
| 11 | Nano banana is Googles Best Image Model?  #aiautomation #n8n | Tyler AI | 1:50 | 2025-10-19 |  | nanobanana, n8n | ia-imagen | https://www.youtube.com/watch?v=24LRFgPfKuA |
| 12 | Use N8N and Replicate to create Flux images in 1 min! | Premium Business Automation | 0:57 | 2025-10-19 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=RGWWf4qMLyM |
| 13 | I Built a Photoshop AI Agent That Uses Google's New NanoBanana #n8n #artificialintelligence | Nate Herk \| AI Automation | 1:38 | 2025-10-19 |  | agents, n8n | ia-agentes-code | https://www.youtube.com/watch?v=TWvjqpk3uSQ |
| 14 | Google Nano Banana AI for Landscape Design \| Prompts, Renderings & Workflows Explained | LandSpace Architecture | 8:05 | 2025-10-15 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=0NQnYJHshs4 |
| 15 | FLUX Kontext Dev COMPLETE Comfyui  Installation and Beginners Guide | Urban Decoders | 10:32 | 2025-10-14 |  | comfyui, flux | ia-imagen | https://www.youtube.com/watch?v=JoA0Saf1Pgo |
| 16 | How to train your LoRA: FULL Guide with Easy Local training for FLUX AI | Urban Decoders | 10:27 | 2025-10-14 |  | flux | ia-imagen | https://www.youtube.com/watch?v=U43VBFZKe08 |
| 17 | AI Architecture - Ideas to renders in seconds with ComfyUI | LightSketch | 19:59 | 2025-10-14 |  | comfyui, arq, viz | ia-imagen | https://www.youtube.com/watch?v=UG5wVg4zcZc |
| 18 | Top 10 AI Model for Architecture \| Stable diffuision for Architecture | Archi Lab | 3:12 | 2025-10-14 |  | arq | diseno-arq | https://www.youtube.com/watch?v=Ga0vZwq7hW4 |
| 19 | How to use and test a LoRA | ATELIER DESIGNA | 41:10 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=Mr8gSQPMPTM |
| 20 | ComfyUI for Everything (other than stable diffusion) | Design Input | 32:53 | 2025-10-14 |  | comfyui, stable-diffusion | ia-imagen | https://www.youtube.com/watch?v=fUcDAExxndQ |
| 21 | Advanced AI Sketch to Image: Style transfer with comfyui and IPadapter | Urban Decoders | 8:02 | 2025-10-14 |  | comfyui, dibujo | ia-imagen | https://www.youtube.com/watch?v=4_37qy9Rfr0 |
| 22 | 🔮 ComfyUI Best Upscale Methods for Low VRAM Graphic Cards  [AMD 4GB] | Ai Underground Art | 7:24 | 2025-10-14 |  | comfyui, upscaling | ia-imagen | https://www.youtube.com/watch?v=tNcdmVLsJmQ |
| 23 | ⏳ How to install ComfyUI on low VRAM  AMD Graphic Cards [AMD 4GB] | Ai Underground Art | 13:00 | 2025-10-14 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=LYUtzUKqIlg |
| 24 | The Ultimate ComfyUi Workflow for Architects | Alphonso Peluso | 1:28:56 | 2025-10-14 |  | comfyui, arq | ia-imagen | https://www.youtube.com/watch?v=-zmgjdB8E1U |
| 25 | Free Image-to-Video AI \| WAN 2.1 + LTX (March 2025 Demo) | ATELIER DESIGNA | 16:58 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=UxGd3-yWXpI |
| 26 | MidJourney for Architects Prompt Styles | Alphonso Peluso | 7:38 | 2025-10-14 |  | midjourney, arq | ia-imagen | https://www.youtube.com/watch?v=RZv1m7yPPZA |
| 27 | Stable Diffusion RunPod Updated | Alphonso Peluso | 21:48 | 2025-10-14 |  | stable-diffusion | ia-imagen | https://www.youtube.com/watch?v=xYnK94zHYo8 |
| 28 | Comfyui 101 Flux Upscale Workflow: Step-by-Step Guide \| Part 7 | Monzon Media | 27:21 | 2025-10-14 |  | comfyui, upscaling | ia-imagen | https://www.youtube.com/watch?v=G2m3vzg5bn8 |
| 29 | realtime archviz with stable diffusion 03/2024 | Paul Hansen | 0:57 | 2025-10-14 |  | stable-diffusion, viz | ia-imagen | https://www.youtube.com/watch?v=31tqnDZ2_Pg |
| 30 | Master AI image generation - ComfyUI FULL TUTORIAL | AI Search | 1:18:44 | 2025-10-14 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=g74Cq9Ip2ik |
| 31 | ComfyUI Tutorial Series: Ep01 - Introduction and Installation | pixaroma | 21:16 | 2025-10-14 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=Zko_s2LO9Wo |
| 32 | NANO BANANA AI Surprised Me with This Architectural Render… | BIM Design Studio | 2:41 | 2025-10-14 |  | nanobanana, arq, viz | ia-imagen | https://www.youtube.com/watch?v=47D7E4_iruk |
| 33 | Nano Banana for Exterior Design Architecture \| EVERYTHING YOU SHOULD KNOW | Salmaan Mohamed | 6:01 | 2025-10-14 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=T-tpBjPkEl8 |
| 34 | DALLE 3: el rival que Midjourney no esperaba. ¿Cuál es mejor? | DonebyLaura | 11:31 | 2025-10-14 |  | midjourney | ia-imagen | https://www.youtube.com/watch?v=3SYPKQNXCD8 |
| 35 | Storyboard | Morfeo Academy | 9:13 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=QrZyNRxNzE8 |
| 36 | How to Use Midjourney as an Architect #shorts #design #architecture #ai | The Architecture Grind | 0:35 | 2025-10-14 |  | midjourney, arq | ia-imagen | https://www.youtube.com/watch?v=OtYG-mUiq4g |
| 37 | @PAACADEMYY AI-Driven Design Practice – Stable Diffusion in Architecture (Cas Esbach / MVRDV) | Parametric Architecture | 3:23:18 | 2025-10-14 |  | stable-diffusion, arq, parametrico | ia-imagen | https://www.youtube.com/watch?v=FCKhn42cxHk |
| 38 | Ai animation made with Stable Diffusion+Deforum #stablediffusion #ai #deforum #architecture #shorts | Alphonso Peluso | 0:17 | 2025-10-14 |  | stable-diffusion, arq | ia-imagen | https://www.youtube.com/watch?v=dRetukP_Brc |
| 39 | 🧠 RENDERS con ChatGPT para DISEÑO ARQUITECTONICO ► Nueva Creación de Imágenes | bydavidparra | 10:49 | 2025-10-14 |  | llm, viz | ia-agentes-code | https://www.youtube.com/watch?v=s47jwJcdFuI |
| 40 | Archviz x AI - a FREE Workflow for ComfyUI (TEASER) | Paul Hansen | 0:47 | 2025-10-13 |  | comfyui, viz | ia-imagen | https://www.youtube.com/watch?v=L0cIuyF7Q8E |
| 41 | CÓMO RENDERIZAR un BOCETO con IA usando PROME AI | 1ClickTutorials | 1:43 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=9aYwsmCtUT4 |
| 42 | All-in-one FLUX Control Nets with Loras | Urban Decoders | 12:58 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=AvcXrJjaFZo |
| 43 | Lora Training using only ComfyUI!! | AIFuzz | 11:15 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=gt_E-ye2irQ |
| 44 | _(sin titulo)_ |  |  | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=hZCTiZi-EPw |
| 45 | FREE LoRA Training on Colab—Stable Diffusion 1.5 Guide | INTProgrammer | 14:24 | 2025-10-13 |  | stable-diffusion | ia-imagen | https://www.youtube.com/watch?v=DiDYymQsOWc |
| 46 | Create SEAMLESS AI Timelapse Videos from frames (both cloud and local comfyUI options) | Urban Decoders | 8:01 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=xVMpO5lX2NA |
| 47 | Game Changer ComfyUi #architecture #architectureschool  #ai #rendering #parametricdesign #comfyui | Alphonso Peluso | 1:10 | 2025-10-13 |  | comfyui, arq | ia-imagen | https://www.youtube.com/watch?v=KRldrZ1yzCA |
| 48 | A.I. STABLE DIFFUSION (ARCHITECTURE ANIMATION WALKTHOUGH) | Đình Nguyễn | 0:21 | 2025-10-13 |  | stable-diffusion, arq | ia-imagen | https://www.youtube.com/watch?v=oeQN3MvAyUI |
| 49 | ComfyUI: Intro to Control Net- Sketch to Render (Part III) | Urban Decoders | 12:07 | 2025-10-13 |  | comfyui, viz, dibujo | ia-imagen | https://www.youtube.com/watch?v=oGwTMmWXMjc |
| 50 | AI Meets Design: Enhancing 3D Workflow with Stable Diffusion, ComfyUI, 3DS Max, ControlNet - Live! | Amir Ferdos | 1:55:56 | 2025-10-13 |  | 3dsmax, comfyui, stable-diffusion | software-arq | https://www.youtube.com/watch?v=daX0VM4WdXk |
| 51 | COMFYUI para principiantes: La mejor guía desde cero 🚀 | Nekodificador Lab | 24:19 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=0Db_ZMz8bWY |
| 52 | Controlnet for Architecture Visualization : AI Architecture Design | Archi Lab | 5:35 | 2025-10-13 |  | arq, viz | diseno-arq | https://www.youtube.com/watch?v=hr2ri5SBPfU |
| 53 | How to Connect ComfyUI to N8N (Best Method) | Mindly Nova | 1:40 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=_WpbBIEtJUs |
| 54 | How to Connect n8n to ComfyUI on Runpod \| $0.15 for 24GB VRAM \| Step-By-Step Tutorial | Dorian Oslov \| The Decode AI | 35:00 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=RgrEAge_5Kk |
| 55 | ✨ComfyUI: Te hago EXPERTO✨ ComfyUI-Manager + Workflow text-to-image PASO A PASO - Video # 2 🚀 | YASKAD | 23:46 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=n-niYeoZ_gs |
| 56 | 🟩 56 – ComfyUI Studio 2.5.6: Cómo instalar, qué incluye y por qué es un cambio brutal | Tecnolitas | 24:02 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=i0mpxtD33No |
| 57 | 🚀¿Qué MODELOS puedes usar en COMFYUI? Guía Completa para Principiantes | ArquiKev | 10:12 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=LRLyH0dmFEk |
| 58 | Entrena tu propio LoRA con POCAS imágenes en Stable Diffusion XL  (Tutorial) | Alex Otano | 19:34 | 2025-10-13 |  | stable-diffusion | ia-imagen | https://www.youtube.com/watch?v=IikYM9tb_GE |
| 59 | What is a LoRA? Full Guide how to use with ComfyUI | Urban Decoders | 11:30 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=AYdEaJe74Dk |
| 60 | ComfyUI 2D to stylized 3D Workflow (Not actual 3D) | AIFuzz | 9:04 | 2025-10-13 |  | comfyui | ia-imagen | https://www.youtube.com/watch?v=Kc44fxiptxk |
| 61 | BASIC Comfyui Tutorial for Archviz x AI - 15/17 IMG2VIDEO | Paul Hansen | 7:48 | 2025-10-13 |  | comfyui, viz | ia-imagen | https://www.youtube.com/watch?v=hpireXqXuU0 |
| 62 | Flux Kontext LoRA Training for ComfyUI with ai-toolkit | ComfyUI | 58:15 | 2025-10-13 |  | comfyui, flux | ia-imagen | https://www.youtube.com/watch?v=U9QKhRMKIwc |
| 63 | Automatizá tu creatividad: ComfyUI \| n8n \| Vercel V0 | Morfeo Academy | 42:29 | 2025-10-13 |  | comfyui, n8n | ia-imagen | https://www.youtube.com/watch?v=7n7A9emeiVQ |
| 64 | Nano Banana + Wan 2.2 in ComfyUI - Making videos with Gemini Flash Image | ComfyUI | 1:32:09 | 2025-10-13 |  | comfyui, nanobanana, llm | ia-imagen | https://www.youtube.com/watch?v=3DMPgVDh35g |
| 65 | Nano Banana Just Unlocked AI Motion Graphics | Futurepedia | 18:55 | 2025-10-13 |  | nanobanana | ia-imagen | https://www.youtube.com/watch?v=9yBMtvD_CFw |
| 66 | AI Thumbnail Generator for YouTube in ONE Click! (No Photoshop Needed) | Zero2Launch \| AI Automation | 4:54 | 2025-10-13 |  | n8n | ia-agentes-code | https://www.youtube.com/watch?v=RXO2YKdPMGI |
| 67 | ¡FÁCIL! Automatiza la EDICIÓN de IMÁGENES con este COMBO de Google 🤯 100% GRATIS | Xavier Mitjana | 17:17 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=jbDttmzgpp8 |
| 68 | QWEN Model (GGUF) - Architectural Explorations inside ComfyUI | za_Lab | 3:02 | 2025-10-13 |  | comfyui, llm, arq | ia-imagen | https://www.youtube.com/watch?v=bLoW-tZEkik |
| 69 | GOOGLE Nano Banana has CHANGED Architecture Forever \| Step-By-Step Walkthrough | Salmaan Mohamed | 7:20 | 2025-10-13 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=CWBL_tH4fI4 |
| 70 | NANO BANANA EN COMFYUI 🍌 | Morfeo Academy | 59:37 | 2025-10-13 |  | comfyui, nanobanana | ia-imagen | https://www.youtube.com/watch?v=fP7VStOfJJ4 |
| 71 | ComfyUI For Architecture - Simple SDXL Inpainting Workflow | za_Lab | 2:56 | 2025-10-13 |  | comfyui, stable-diffusion, arq | ia-imagen | https://www.youtube.com/watch?v=px8POauudLY |

---

### IA/🎬gen_Vid

**Tu descripcion:** Inteligencia Artificial Generativa (AUDIOVISUAL) Sora, Pika, Runway, VEO, Kling, entre otros.

Archivo Takeout: `IA_🎬gen_Vid-vídeos.csv` · Videos: 18

| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Seedance HUMILLA a VEO 3 y KLING  🤯 El NUEVO REY del vídeo con IA ya está aquí | Migue Baena IA | 22:27 | 2025-10-14 |  | video-ia, llm | ia-video-audio | https://www.youtube.com/watch?v=DN4kUXKgs0o |
| 2 | Storyboard | Morfeo Academy | 9:13 | 2025-10-14 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=QrZyNRxNzE8 |
| 3 | A.I. STABLE DIFFUSION (ARCHITECTURE ANIMATION WALKTHOUGH) | Đình Nguyễn | 0:21 | 2025-10-13 |  | stable-diffusion, arq | ia-imagen | https://www.youtube.com/watch?v=oeQN3MvAyUI |
| 4 | Make AI videos with talking + pose + reference control. MultiTalk & VACE tutorial | AI Search | 33:06 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=FMo9oN2EAvE |
| 5 | Nano Banana + Wan 2.2 in ComfyUI - Making videos with Gemini Flash Image | ComfyUI | 1:32:09 | 2025-10-13 |  | comfyui, nanobanana, llm | ia-imagen | https://www.youtube.com/watch?v=3DMPgVDh35g |
| 6 | Nano Banana Just Unlocked AI Motion Graphics | Futurepedia | 18:55 | 2025-10-13 |  | nanobanana | ia-imagen | https://www.youtube.com/watch?v=9yBMtvD_CFw |
| 7 | WAN Animate just broke the internet (Open-Source Character Replacement) | Sirio | 16:51 | 2025-10-13 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=m7cdSfIiALE |
| 8 | 🟢Genera Videos con NUEVA IA de China - GRATIS e Ilimitado (Waver) | Tutoriales Informáticos + IA | 11:00 | 2025-09-16 |  | llm | ia-agentes-code | https://www.youtube.com/watch?v=dGspXhfJLNI |
| 9 | How to Create Videos with Google’s Nano Banana AI in n8n (No-Code Tutorial) | Ahmad \| AI Automation | 38:33 | 2025-09-15 |  | nanobanana, n8n | ia-imagen | https://www.youtube.com/watch?v=EF_w7P9zha4 |
| 10 | GOOGLE Nano Banana has CHANGED Architecture Forever \| Step-By-Step Walkthrough | Salmaan Mohamed | 7:20 | 2025-09-04 |  | nanobanana, arq | ia-imagen | https://www.youtube.com/watch?v=CWBL_tH4fI4 |
| 11 | NANO BANANA EN COMFYUI 🍌 | Morfeo Academy | 59:37 | 2025-09-01 |  | comfyui, nanobanana | ia-imagen | https://www.youtube.com/watch?v=fP7VStOfJJ4 |
| 12 | 🚀 Probando NANO BANANA + VEO3 en WHISK: ¿El COMBO más BRUTAL de IA? 🔥 | Máximo Bruno | 17:56 | 2025-09-01 |  | nanobanana, llm | ia-imagen | https://www.youtube.com/watch?v=yJIM3XQpUng |
| 13 | GOOGLE VEO 3: GUÍA DEFINITIVA Desde Cero para Videos VIRALES y Prompts | Arca Artificial by Lordwind Enrique | 21:13 | 2025-09-01 |  | video-ia | ia-video-audio | https://www.youtube.com/watch?v=oodW_W15rLY |
| 14 | Google VEO 3 & FLOW Guía Definitiva - CREA VIDEOS CON IA (Curso GRATIS) | Date Un Top | 56:04 | 2025-09-01 |  | video-ia, llm | ia-video-audio | https://www.youtube.com/watch?v=dGLrdrutXUs |
| 15 | How to use Nano Banana for AI Filmmaking (FREE workflow) | Jack Vs. AI | 22:40 | 2025-08-31 |  | nanobanana | ia-imagen | https://www.youtube.com/watch?v=NlLBXqaN8AY |
| 16 | How to use Nano Banana for FREE (AI filmmaking guide) | Jack Vs. AI | 17:57 | 2025-08-31 |  | nanobanana | ia-imagen | https://www.youtube.com/watch?v=ogU3Di7rvnc |
| 17 | 🟢Aplicación 100% GRATIS para usar VEO 3 - ¡Incluso puede ser Ilimitado! | Tutoriales Informáticos + IA | 10:04 | 2025-08-31 |  | video-ia, llm | ia-video-audio | https://www.youtube.com/watch?v=ZmYcQPecJTw |
| 18 | NUEVO Método AGOSTO! VEO 3 GRATIS! Sin Tarjeta y 100% Legal 😱 | MUSYN | 5:28 | 2025-08-31 |  | video-ia | ia-video-audio | https://www.youtube.com/watch?v=-Y6gSvQX6JM |

---

## Parte B — Canales fuera de scope (para tu revision)

Estos 66 canales de tus 157 suscripciones no matchearon las keywords
del scope (arquitectura + IA + software arq + construccion + NFTs).

**La columna *Parece ser* es una sugerencia mia para que puedas escanear rapido.**
Vos completes la columna *Tu veredicto*: sumar a `<categoria>`, descartar, o dejar pendiente.

| # | Canal | Link | Parece ser | Tu veredicto | Notas |
|---|---|---|---|---|---|
| 1 | U-tad | https://www.youtube.com/channel/UC179ukpiFWZSTGWjHLocA0A | Educacion general |  |  |
| 2 | Vibration of the Universe | https://www.youtube.com/channel/UC1OKTDlgiP2ZYLCkzw-CIWw | sin pista (revisar) |  |  |
| 3 | Schmidt Ocean Institute | https://www.youtube.com/channel/UC1m5LdKP0m64n8nY3NhK6Zg | Ciencia |  |  |
| 4 | MatemáticasTV | https://www.youtube.com/channel/UC2AXB2-VLUGx3HMTMKbgomQ | Educacion general |  |  |
| 5 | Lautaro Pavlin | https://www.youtube.com/channel/UC2rvFoYTSDMEXuZ9jJCA6Ww | sin pista (revisar) |  |  |
| 6 | Ing.Wilmer Planchez | https://www.youtube.com/channel/UC2y8N0nTQMvoja9jOxC1pgQ | sin pista (revisar) |  |  |
| 7 | Un loco y su tecnología | https://www.youtube.com/channel/UC2zp7AWsYhZaGmYTjP8hZ7A | sin pista (revisar) |  |  |
| 8 | The Chopra Well | https://www.youtube.com/channel/UC6d0RMVcoXNCkTpG8PW2dBA | TV / entertainment |  |  |
| 9 | Pawn After Dark | https://www.youtube.com/channel/UC6psXRry78z8sPaRkR2oUKQ | TV / entertainment |  |  |
| 10 | Alex The Analyst | https://www.youtube.com/channel/UC7cs8q-gJRlGwj4A8OmCmXg | Educacion general |  |  |
| 11 | J. Krishnamurti - Official Channel | https://www.youtube.com/channel/UC88A5W9XyWx7WSwthd5ykhw | Filosofia / espiritualidad |  |  |
| 12 | Dr.HouseMD | https://www.youtube.com/channel/UC97YM2FZ32sr7aCDzEyzesw | TV / entertainment |  |  |
| 13 | Only Developers | https://www.youtube.com/channel/UCAvJZaWnM-tro-JP2Rh8S5g | sin pista (revisar) |  |  |
| 14 | NirnaethGameDev | https://www.youtube.com/channel/UCBk6jGfS8dS7QzW0yCHc7bw | TV / entertainment |  |  |
| 15 | Matt Sherman - Geek Psychology | https://www.youtube.com/channel/UCCWoIKYEkSKqEP24hWbe7nA | Negocios / podcasts |  |  |
| 16 | Sawan Kumar | https://www.youtube.com/channel/UCCqB4fklHc1rAhJt4OmzkrQ | Creatores arq |  |  |
| 17 | Diego Vásquez \| IA builder | https://www.youtube.com/channel/UCDLRV0Hsf0rgzMx5bWWgf7g | IA / tech |  |  |
| 18 | Josema Fernández \| IA | https://www.youtube.com/channel/UCERX0a6PiDc3gDVZ1Vf_tBw | sin pista (revisar) |  |  |
| 19 | AMP Tech | https://www.youtube.com/channel/UCG4H4Qf-ZU9Ycr_PQ4egqDQ | sin pista (revisar) |  |  |
| 20 | Screen Culture | https://www.youtube.com/channel/UCGA2OgjW608QEaGwxA7aRTg | sin pista (revisar) |  |  |
| 21 | The Diary Of A CEO | https://www.youtube.com/channel/UCGq-a57w-aPwyi3pW7XLiHw | Negocios / podcasts |  |  |
| 22 | Veritasium | https://www.youtube.com/channel/UCHnyfMqiRRG1u-2MsSQLbXA | Ciencia |  |  |
| 23 | AprendemosJuntos | https://www.youtube.com/channel/UCI6QcXatdaEAaRTRjl3dc0w | Educacion general |  |  |
| 24 | Melodías de Luz Interior | https://www.youtube.com/channel/UCJqdhH1idDA9RLoG69Zyg_Q | Filosofia / espiritualidad |  |  |
| 25 | Jack Vs. AI | https://www.youtube.com/channel/UCKBj5HPTd64zoQmkGNseKUw | sin pista (revisar) |  |  |
| 26 | IAC LATAM | https://www.youtube.com/channel/UCKxdz4Ot1vrhLnU-RPr9mRA | sin pista (revisar) |  |  |
| 27 | NASA | https://www.youtube.com/channel/UCLA_DiR1FfKNvjuUpBHmylQ | Ciencia |  |  |
| 28 | BUDS Lab Team Member | https://www.youtube.com/channel/UCN1553rrViZJ38Wpm_a51OA | sin pista (revisar) |  |  |
| 29 | Brainy Touch | https://www.youtube.com/channel/UCOAGXFh7tqOu3YoxvmLhoSw | sin pista (revisar) |  |  |
| 30 | NEXT Manu | https://www.youtube.com/channel/UCPA627vvesTcWg5d3XeSvOA | sin pista (revisar) |  |  |
| 31 | Freedom Arts 3D Workflow | https://www.youtube.com/channel/UCPi437n6fBnO_z0vexNgv_w | Software arq / 3D |  |  |
| 32 | La fan de Margarita | https://www.youtube.com/channel/UCTIAxEpHPX1RT5vL8LsXQFQ | sin pista (revisar) |  |  |
| 33 | Dr. Mayim Bialik | https://www.youtube.com/channel/UCTOocPnDh2YQZZwh86K2OxA | sin pista (revisar) |  |  |
| 34 | Tutoriales Informáticos + IA | https://www.youtube.com/channel/UCWIh59roXmtyvwoMR93gWzA | sin pista (revisar) |  |  |
| 35 | Veritasium en español | https://www.youtube.com/channel/UCXtxgWwk55kVJo9lCCZRdmg | Ciencia |  |  |
| 36 | 3Blue1Brown | https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw | Ciencia |  |  |
| 37 | Be Inspired | https://www.youtube.com/channel/UCaKZDEMDdQc8t6GzFj1_TDw | sin pista (revisar) |  |  |
| 38 | BrainWatched | https://www.youtube.com/channel/UCb0DEaqM6Cnosv4pkEUwAOQ | sin pista (revisar) |  |  |
| 39 | QuantumFracture | https://www.youtube.com/channel/UCbdSYaPD-lr1kW27UJuk8Pw | IA / tech |  |  |
| 40 | Study Sonic Focus | https://www.youtube.com/channel/UCbkK0kd3xMIWIFyLl4f5I2A | Musica / arte |  |  |
| 41 | fidargroups | https://www.youtube.com/channel/UCc15uitcZE5Kp5Otn8Wrrbg | sin pista (revisar) |  |  |
| 42 | Albert Olgaard | https://www.youtube.com/channel/UCdrYxpEy-e8uVDWYzFK3dCA | sin pista (revisar) |  |  |
| 43 | Buddha's Wisdom | https://www.youtube.com/channel/UCf6oZ5g1QglnpG0GpBrjxSQ | Filosofia / espiritualidad |  |  |
| 44 | James Webb Space Telescope (JWST) | https://www.youtube.com/channel/UCfi4_aCc2nEhtUMSGqaim_Q | Ciencia |  |  |
| 45 | Cisco DevNet | https://www.youtube.com/channel/UChRmUH4H5hiYzPiFhvNoCIg | IA / tech |  |  |
| 46 | Inteligencia Artificial | https://www.youtube.com/channel/UCl5-lvQyfILb-l2abPk4Ntg | IA / tech |  |  |
| 47 | Ringa Tech | https://www.youtube.com/channel/UCm9QZ70KuIVShztZ7HmE4NQ | IA / tech |  |  |
| 48 | VR Boxing Club | https://www.youtube.com/channel/UCmR_Fu9NhgV6LJ86jfOuciQ | sin pista (revisar) |  |  |
| 49 | Leantime | https://www.youtube.com/channel/UCn1tfy7jFcnddiCdH9uZM0Q | sin pista (revisar) |  |  |
| 50 | Tom Bilyeu | https://www.youtube.com/channel/UCnYMOamNKLGVlJgRUbamveA | Negocios / podcasts |  |  |
| 51 | Omnity Meditación | https://www.youtube.com/channel/UCnjsFhatLwYKvcpXJM2uP9g | Filosofia / espiritualidad |  |  |
| 52 | Xavier Mitjana | https://www.youtube.com/channel/UCp2Zmdh40GJJJ2T5vWsMZDA | sin pista (revisar) |  |  |
| 53 | StarTalk | https://www.youtube.com/channel/UCqoAEDirJPjEUFcF2FklnBA | Ciencia |  |  |
| 54 | Jason Lewis - Mind Amend | https://www.youtube.com/channel/UCrpFW99zAUaJT8cKmqeagkg | Arq vanguardia / teoria |  |  |
| 55 | Vermillion | https://www.youtube.com/channel/UCryxQ2E3uHuxEFDvutOyEow | sin pista (revisar) |  |  |
| 56 | Gary Judge | https://www.youtube.com/channel/UCrzDCmG_X2tmsAr_-9Iefiw | Negocios / podcasts |  |  |
| 57 | Onen Gabe | https://www.youtube.com/channel/UCuVa0u7qjPmlgov7LJdOUEQ | sin pista (revisar) |  |  |
| 58 | Vast Coding | https://www.youtube.com/channel/UCvD5vcbsjWNv5iv1EGFNBjA | IA / tech |  |  |
| 59 | Museo Argentino de Ciencias Naturales | https://www.youtube.com/channel/UCvJMYTBR-q2W6XcF1ofAYWw | Ciencia |  |  |
| 60 | Gabriel Luces | https://www.youtube.com/channel/UCviYRG8WWSaQkt3QW9gw3HA | sin pista (revisar) |  |  |
| 61 | Alerta Critica | https://www.youtube.com/channel/UCxIQcXnWQHEEo1RUM1DABwg | IA / tech |  |  |
| 62 | MoureDev by Brais Moure | https://www.youtube.com/channel/UCxPD7bsocoAMq8Dj18kmGyQ | IA / tech |  |  |
| 63 | Alejavi Rivera | https://www.youtube.com/channel/UCxcDzs-4quJV4QsairlFYNg | sin pista (revisar) |  |  |
| 64 | CodingTube | https://www.youtube.com/channel/UCy44Oi7rEHR7-kuQXVCkJqA | IA / tech |  |  |
| 65 | Misterios Retro | https://www.youtube.com/channel/UCyOO3I8J-P4DS-x0xQeHv3w | TV / entertainment |  |  |
| 66 | CACHETADA | https://www.youtube.com/channel/UCyvYUEcpUKi8P5gY5u1Patg | TV / entertainment |  |  |

---

## Parte C — Canales en scope (resumen)

Estos si matchearon. Ya esta el detalle en [[wiki/glosario/interno/canales-youtube|canales-youtube]].

| Categoria | Canales |
|---|---|
| arq+IA | 19 |
| software arq | 33 |
| estudios intl. | 4 |
| IA general | 13 |
| NFTs/tokens | 1 |
| construccion | 7 |
| creadores | 9 |
| noticias intl. | 1 |
| metaverso | 4 |
| **total** | **91** |

## Metodologia y origen

- Fuente: `C:\Users\Solch16\Downloads\Takeout\YouTube y YouTube Music\`
- Marcadores: `C:\Users\Solch16\Downloads\Takeout\Chrome\Marcadores.html`
- Generado: 2026-10-08
- Decision HITL: filtrar el ruido (quedan solo los canales del rubro)
- Proximo paso: completar Parte B (veredictos) y regenerar el script si actualizas el Takeout

---

## Parte D — Marcadores de Chrome

434 bookmarks en 36 carpetas, agrupados por tu carpeta de origen.
Cada link tiene un tag inferido por el nombre del sitio (para filtrar rapido).

### Carpetas

| Carpeta | Bookmarks | Categoria |
|---|---|---|
| comfyui+IC+img | 77 | software arq |
| 01-Sketch | 37 | software arq |
| ArchViz UE-Comfy | 35 | software arq |
| apps | 31 | sin categoria |
| Apps | 26 | sin categoria |
| Presupuestos | 20 | construccion |
| Other Bookmarks | 19 | personal |
| GCBApp | 17 | construccion |
| CASABLANCA | 16 | construccion |
| PC's | 15 | personal |
| busqueda_celular | 12 | personal |
| E# | 12 | educacion |
| VPS's | 12 | personal |
| COMFYUI | 10 | software arq |
| GCBA-INFO-TEC | 9 | construccion |
| Agents | 9 | ia |
| Nueva carpeta | 9 | sin categoria |
| LIBROS | 8 | libros |
| PROGRAMAS | 8 | software arq |
| MUEBLES_CARP | 6 | construccion |
| ALURA | 6 | educacion |
| #HON | 5 | construccion |
| BIM | 5 | software arq |
| CAD-Bloques3D | 4 | software arq |
| ANCAFLEX | 4 | construccion |
| REVEAR | 4 | construccion |
| WEBER | 4 | construccion |
| aldershot | 3 | software arq |
| CAD-Bloques2D | 2 | software arq |
| SINTEPLAST | 2 | construccion |
| IA.RQ | 2 | ia |
| DURLOCK | 1 | construccion |
| KEKOL | 1 | construccion |
| G# | 1 | educacion |
| AVISO_OBRA | 1 | construccion |
| A# | 1 | educacion |

### Links por carpeta

**comfyui+IC+img** (77 bookmarks · software arq)

- [Models \| OpenRouter](https://openrouter.ai/models)
- [Gemini 2.5 Flash Image Preview (Nano Banana) - API, Providers, Stats](https://openrouter.ai/google/gemini-2.5-flash-image-preview)
- [GenAI API Pricing: Haliuo, Vidu, Pixverse \| Pay-Per-Use \| fal.ai](https://fal.ai/pricing)
- [n8n y comfyui - Buscar con Google](https://www.google.com/search?sca_esv=ad175a4a610f2e0b&udm=7&sxsrf=ANbL-n7Fhj0ZGTwDHVHPt_6NzeBryl0WDQ:1772660343816&q=n8n+y+comfyui&sa=X&ved=2ahUKEwje0eawmoeTAxW7O7kGHdqyLvkQ8ccDKAJ6BAgZEAQ&biw=730&bih=666&dpr=0.9)
- [(429) Como conectar N8N + ComfyUI (GUIA DEFINITIVA) - YouTube](https://www.youtube.com/watch?v=eKdu9XEjFws)
- [(429) Automatizá tu creatividad: ComfyUI \| n8n \| Vercel V0 - YouTube](https://www.youtube.com/watch?v=7n7A9emeiVQ)
- [(429) Connect ComfyUI and n8n - Step-by-Step Guide - YouTube](https://www.youtube.com/watch?v=AOjxHMMck7s)
- [(429) n8n with ComfyUI AI Image Automation for Beginners (NOCODE) - Yo](https://www.youtube.com/watch?v=nuUf3f36RUE)
- [ComfyUI](https://cloud.comfy.org/cloud/login?previousFullPath=%252Fcloud%252Fsubscribe%253Ftier%253Dfree)
- [ComfyUI](https://cloud.comfy.org/cloud/login)
- [Luma API \| AI Video Generator API](https://lumalabs.ai/api)
- [CRM inmobiliario: ¿cómo optimizar tu tiempo y el de tu equipo?](https://blog.tokkobroker.com/crm-inmobiliario?utm_source=chatgpt.com)
- [Gemini](https://gemini.google.com/app/6e2658e09b934b86?hl=es)
- [Gammas - Gamma](https://gamma.app/)
- [Enrich your projects with multimedia - PandaSuite](https://pandasuite.com/features/multimedia/)
- [Panel - Genially](https://app.genially.com/teams/68023f924812c9d3b690c364/spaces/68023f924812c9d3b690c37a/templates/all?search=choice+board)
- [DaVinci - AI Art Generator](https://davinci.ai/onboarding/continue)
- [How It Works - Ark](https://arkdesign.ai/how-it-works/)
- [TestFit: Real Estate Feasibility Platform](https://www.testfit.io/)
- [Free 3D Home Design Software & Floor Planner Online](https://www.coohom.com/)
- [Free AI Home Design \| Speed, Style, and Customization](https://www.coohom.com/case/ai-home-design)
- [Software Gratuito de diseño para el hogar 3D \| Modelos + 1M y renderiz](https://www.homestyler.com/)
- [Create Art or Modify Images with AI](https://openart.ai/home)
- [Meta](https://auth.meta.com/register/instagram/?waterfall_id=d197c3f2-4d97-4ef7-8067-e08c63e033ec&source_app_id=391894423991568&redirect_uri=https%3A%2F%2Fauth.meta.com%2Foidc%2F%3Fapp_id%3D391894423991568%26scope%3Dopenid%2Blinking%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.meta.ai%252Foidc%252Fcallback%252F%26state%3DATlfN4rcZHWjTb9h-4HzTwtGW9Vd0ek9AqiUxtKBOE8tOhNaeI-9vflcF61qRsC4UpCbYuIgZlksuOgVelbFpTl_LcBkTAFmA3LJCO8Cwm5bG9n1NrlrnH-cg1ZCTa6SBJHVTEzL5n4pjYxri8l6ZVUSlEkELZ6IXcX9j1wQ21SSmbPXGGJ5dCyXwAeq5zfIYUAdORsYolNBxRONcmd_ZErkJt-o7bPf3KO6RrXQ2QsPLbD5ttx2UY-aela112jGKGhKIdzniWhoJhRH1OZGps1BOdE7BtzwHjy4etfnKWs6h8ZSYwzjNjyp9xc&csi=fd2b1c3b-c0be-4dcd-8cae-1c92f19cbd34&oidc_at=eyJhbGciOiJkaXIiLCJraWQiOjcsImN0eSI6IkpXVCJ9...AbscehN-J_YoL0xrPl-aNHxGbKM-2k1UrzWFdpHt0vzk4jUGmZVhwQMUIhwrV4ZkN2wQxSqnqfSvtbRJhLpoDw2YyFoAhEAnbrtqLcIJt9sJmYy9sdPqx3dzpQf7G_QxF5Zs39t4JAnK9odkcAV4of1vja_YlfRzYea9en2YO2gBXrsouxwXrslygj2qlKdGaM7OKC3M0a61Xe3iI3A27fF-VQjfqAYD-gOmZUQGOZdlNdjeaQcIuP5XSL7qn-4DW31LmKfI5SizoTVK2X1t_ok9LmCUe_AblPIePvTOBOWx2HPTU0UlUo9ispYvYil5KfkWYnHeipHtolh-dMwBB2CZzYCmytzvgF1kiY3e6aiX6f54Brsi6RVdZrWfzr2r8-DTvgwfrYFAX_NuArcD436musoRC6MpGG95k24PS7WckZAteSnUvCVrPc19QSO-NcV4wfbjjEHraguJF_2SD0ATDbmh-oXmRZJ3j0DjVS91SgTn75wWtJU0SdNhY9b5I475rFhZYawWVCUa0YJs31IcwD4YAkGkzEI-4TewjYJF4G7KhatKsHZK29YPur4iqyLxLbWTNMemgecWtFgE3meins2CBrV2KdCfOhnM_r0cc3Uqub4r8wdkbX_i9_Jf0jfrTyFA6-S6tu0vnfMuYqR8eDuehIPv-9aRAlALCFDcbbSTjkBe4dvVHXmbtQApauMI2c6RQ2ncbtwV0sQTri4AwYAK-hqNXB1ASmIQOJ0H8ytsMCU5QHRiDx1OgvaSDw0FyxAUj7d1xw3mtiXzaKVEo_C9S6rvu5jeK-v1kZvMiZ9RHlguzi32NuoQKJ_P5rZbkEJfm8GNSrJFbJfX-O1um87vwknAZYk1CyqmGHxqtHK-SU0Uzr-V.)
- [Meta AI](https://www.meta.ai/)
- [Generative AI in Higher Education \| The ChatGPT Effect \| Cecilia Ka Yu](https://www.taylorfrancis.com/books/oa-mono/10.4324/9781003459026/generative-ai-higher-education-cecilia-ka-yuk-chan-tom-colloton)
- [Leonardo's Rule and the Geometry of Nature - Tumamoc Sketchbook](https://tumamocsketchbook.com/2021/07/drawing-a-tree-like-leonardo.html)
- [Precios de Synthesia \| Desde USD 18 por mes](https://www.synthesia.io/es/precios)
- [Chat \| Google AI Studio](https://aistudio.google.com/prompts/new_chat)
- [Krita \| Digital Painting. Creative Freedom.](https://krita.org/es/)
- [Godot Engine - Free and open source 2D and 3D game engine](https://godotengine.org/)
- [Krea](https://www.krea.ai/?error=invalid_request&error_code=400&error_description=OAuth+callback+with+invalid+state)
- [Ideogram](https://ideogram.ai/t/my-images)
- [Image Creation - Leonardo.Ai](https://app.leonardo.ai/image-generation)
- [Nextcloud - Open source content collaboration platform](https://nextcloud.com/)
- [p-31416](https://github.com/p-31416)
- [Overview \| Inkscape](https://inkscape.org/about/overview/)
- [Powerful Workflow Automation Software & Tools - n8n](https://n8n.io/)
- [Request an instant trial - Nextcloud](https://nextcloud.com/instant-trial/)
- [Civitai: The Home of Open-Source Generative AI](https://civitai.com/)
- [Low-code programming for event-driven applications : Node-RED](https://nodered.org/)
- [Documentation : Node-RED](https://nodered.org/docs/)
- [Capa gratuita de AWS \| Cloud computing gratis \|AWS](https://aws.amazon.com/es/free/?gclid=Cj0KCQjwjdTCBhCLARIsAEu8bpI8HhLYDNETPt_rKdamRMnxH_mbeTq7Q1xVVZmDyppmxV_LmFzdkZcaAmHcEALw_wcB&trk=dbffff0f-263c-4cc2-9188-a2eaa7f5f3d4&sc_channel=ps&ef_id=Cj0KCQjwjdTCBhCLARIsAEu8bpI8HhLYDNETPt_rKdamRMnxH_mbeTq7Q1xVVZmDyppmxV_LmFzdkZcaAmHcEALw_wcB:G:s&s_kwcid=AL!4422!3!676949705019!p!!g!!oracle!20656884925!159790792452&gad_campaignid=20656884925&gbraid=0AAAAADjHtp-ifYXxKhTCh8WTv2mkNLxz8&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all&awsm.page-all-free-tier=9)
- [My Map - Mappedin](https://app.mappedin.com/editor/edit/685c80aa06a9e4000b1987c7)
- [Beautiful 3D House Designs & Floor Plans \| Free](https://arcadium3d.com/projects/5ca7ca7b-3f09-4f75-b921-212034dbc7e5)
- [My library \| Plans \| Finch](https://app.finch3d.com/plans)
- [Floorplan Generator \| Maket](https://platform.maket.ai/projects/685c7c95083c358cc5126852/floorplan-generator?tool=floorplan-generator)
- [Arquitecto AI - Renderizador de Arquitectura AI, GPT para Inspiración](https://ai-architect.net/)
- [Claw Cloud](https://us-west-1.run.claw.cloud/signin?link=GCMSU8Y0CNN7)
- [OpenAI Platform](https://platform.openai.com/api-keys)
- [Hugging Face – The AI community building the future.](https://huggingface.co/)
- [ImagineArt AI Tools](https://www.imagine.art/dashboard?token=896150c230af450abc3023c280c1c5281753745905058newsession&isSignUp=true&isSubscribed=false&referral=false)
- [Generador de arquitectura AI \| usBIM.codesign AI \| ACCA software](https://www.accasoftware.com/es/generador-imagenes-ia-para-arquitectura?_gl=1*1w3c4yy*_ga*NjYzODA2OTkwLjE3NTM4MDIwOTA.*_ga_K4Y50QD36K*czE3NTM4MDIwODkkbzEkZzAkdDE3NTM4MDIwODkkajYwJGwwJGgxMjYwNTkwNDE0)
- [No Code App Builder: Create Custom, AI-Powered Apps \| Glide](https://www.glideapps.com/)
- [Flux AI: Free Online Flux Kontext, Flux.1 AI Image Generator](https://flux-ai.io/)
- [Adobe Firefly](https://firefly.adobe.com/?ff_channel=adobe_com&ff_campaign=ffly_homepage&ff_source=firefly_seo&media=featured)
- [Intercambio de caras en línea gratis](https://faceswap.so/es/editor)
- [Free AI Video Prompt Generator for Text to Video AI](https://videoweb.ai/ai-video-prompt-generator/)
- [LMArena](https://lmarena.ai/)
- [Use Cases - Elai.io. See how AI videos can help your brand](https://elai.io/use-cases/)
- [invideo AI - Turn ideas into videos - AI video creator](https://ai.invideo.io/workspace/2f5ebeb0-6532-4e45-b64a-42326668b2f7/account/usage)
- [EaseMate IA: Asistente de IA Todo en Uno para Estudio, Trabajo y Creat](https://www.easemate.ai/es?index=)
- [Vidnoz AI - Home](https://aiapp.vidnoz.com/index.html)
- [Civitai's Guide to Video Gen Prompting - Civitai Education](https://education.civitai.com/civitais-guide-to-video-gen-prompting/#panning)
- [Google AI Studio](https://aistudio.google.com/app/prompts/1TOf-56ymY-2vjPUDmZhgUwFEvXkRw3Mz)
- [Glosario de IA Generativa: Términos clave en imagen y audio](https://aishotlab.com/glosario-de-ia-generativa-para-imagen-y-audio/)
- [Checklist: Construye tu ecosistema de apps con IA \| Gamma](https://gamma.app/docs/Checklist-Construye-tu-ecosistema-de-apps-con-IA-a9spz8k5rwb8k0z?mode=doc)
- [Pricing \| Wispr Flow](https://wisprflow.ai/pricing)
- [Bonus Vibe Code Day](https://franconejos.com/bonus-vibe-code-day)
- [HexaGen \| Community creations](https://gen.hexa3d.io/)
- [The Official Community for Vibe Coders](https://www.vibecoders.la/me/profile)
- [Homepage](https://www.renderforest.com/es/home/main)
- [Qwen Image Edit Camera Control - a Hugging Face Space by multimodalart](https://huggingface.co/spaces/multimodalart/Qwen-Image-Edit-Angles-2)
- [¿No cierras ventas? Sistema de Conversión Inmobiliaria 2026](https://trichterconsulting.com/recibo-muchas-consultas-pero-no-puedo-cerrar-ventas-en-mi-inmobiliaria-como-solucionarlo/)
- [AILINK I Google Antigravity + N8N: Automatizaciones Gratis (Paso A Pas](https://www.notion.so/ailink/AILINK-I-Google-Antigravity-N8N-Automatizaciones-Gratis-Paso-A-Paso-I-Agust-n-Medina-2f4bc10133ae805eb78bc65acbc3d8cd)
- [Chao Antigravity! Claude Code ahora es GRATIS y SIN Límites (Ollama) 💣](https://www.youtube.com/watch?v=kPjOxHdp3OI&list=WL&index=5)
- [Fake Chat Maker](https://fakechatmaker.com/)

**01-Sketch** (37 bookmarks · software arq)

- [GIMP - GNU Image Manipulation Program](https://www.gimp.org/)
- [Funciones \| Krita](https://krita.org/es/features/)
- [Login \| Figma](https://www.figma.com/login)
- [Create - AI Image Generator \| Create Art or Modify Images with AI](https://openart.ai/create)
- [Stability AI Image Models — Stability AI](https://stability.ai/stable-image)
- [Stable Diffusion en línea](https://stablediffusionweb.com/es/app/image-to-image)
- [Generador de arte de IA gratuito: Crea arte de IA a partir de texto -](https://www.seaart.ai/es/eventCenter?type=daily)
- [App - DaVinci AI](https://davinci.ai/app)
- [ChatGPT](https://chatgpt.com/?utm_source=google&utm_medium=paidsearch_brand&utm_campaign=DEPT_SEM_Google_Brand_Acquisition_LATAM_Argentina_Consumer_CPA_BAU_Mix_ImageGen_English&utm_term=dalle%20openai&gad_source=1&gad_campaignid=22413836137&gbraid=0AAAAA-IW-UXM4aYZRnLcn8DscyBokISEN&gclid=CjwKCAjwuIbBBhBvEiwAsNypvTI9kAwp5fOuhz9mSg7fvNDpanGWpb1kX3Dtnm1jWVkVLAWj3CfNKRoClM8QAvD_BwE)
- [Midjourney](https://www.midjourney.com/explore?tab=top)
- [Stable Diffusion en línea](https://stablediffusionweb.com/es)
- [Generative Design \| Architecture Design Software \| Maket](https://www.maket.ai/)
- [Webui Installation Guides · CS1o/Stable-Diffusion-Info Wiki](https://github.com/CS1o/Stable-Diffusion-Info/wiki/Webui-Installation-Guides#amd-comfyui-with-directml)
- [DreamShaper - 8 \| Stable Diffusion Checkpoint \| Civitai](https://civitai.com/models/4384/dreamshaper)
- [ComfyUI Workflows - Developer Community](https://openart.ai/workflows/home?utm_source=google%2Cgoogle&utm_medium=cpc%2Ccpc&utm_campaign=Exp_ComfyUI_Workflow%2C20788293821&utm_content=Dev_Site&utm_term=comfyui&gad_source=1&gad_campaignid=20788293821&gbraid=0AAAAAp6wzGRg0_Lb-AsEfK4hlSbdsd6wa&gclid=Cj0KCQjwoZbBBhDCARIsAOqMEZUYcOdaHvrzM01LhZsPnmsC87sFOwKGjNtDRsGFDid5fli6rowzsc0aAs14EALw_wcB)
- [ComfyUI Prompt Techniques \| ComfyUI Wiki](https://comfyui-wiki.com/en/interface/prompt)
- [ComfyUI Advanced Tutorials \| ComfyUI Wiki](https://comfyui-wiki.com/en/tutorial/advanced)
- [Rhino User's Guide - Introduction](https://docs.mcneel.com/rhino/7/usersguide/en-us/index.htm)
- [Kaggle Notebooks](https://www.kaggle.com/code?searchQuery=lora)
- [Civitai \| Share your models](https://civitai.green/search/models?category=buildings&baseModel=SD%201.5&modelType=Controlnet&modelType=LORA&modelType=VAE&sortBy=models_v9&query=sd1.5)
- [Cursos en línea: Aprende de todo y a tu propio ritmo \| Udemy](https://www.udemy.com/cart/subscribe/course/5196004/)
- [Rhino - Recorte selectivo](https://www.rhino3d.com/features/clipping/selective-clipping/)
- [Tutorial gratuito sobre Twinmotion - Introducción a Twinmotion \| Udemy](https://www.udemy.com/course/introduccion-a-twinmotion/)
- [Course: Crecimiento de curva en 2D y 3D usando Grasshopper \| Udemy](https://www.udemy.com/course/crecimiento-de-curva-en-grasshoppper/learn/lecture/31893488?components=add_to_cart%2Cbase_purchase_section%2Cbuy_button%2Ccacheable_buy_button%2Cdeal_badge%2Cdiscount_expiration%2Cgift_this_course%2Clifetime_access_context%2Cprice_text%2Cpurchase%2Cpurchase_tabs_context%2Crecommendation%2Credeem_coupon%2Cone_click_checkout#overview)
- [SectionTools for Rhino \| Food4Rhino](https://www.food4rhino.com/en/app/sectiontools-rhino)
- [mcneel/RhinoMCP: AI features for Rhino](https://github.com/mcneel/rhinomcp)
- [jingcheng-chen/rhinomcp: RhinoMCP connects Rhino 3D to AI Agent throug](https://github.com/jingcheng-chen/rhinomcp)
- [Rhino MCP Platform](https://mcneel.github.io/RhinoMCP/)
- [Claude Code – Rhino MCP Platform](https://mcneel.github.io/RhinoMCP/docs/getting-started/cc-plugin/)
- [MCP Rhinoceros – Pepe Vazquez - 2025](https://fabacademy.org/2025/labs/aindustriosa/students/pepe-vazquez/docs/commands/mcprhino/)
- [(1557) Rhino MCP for Beginners – Full Walkthrough + Setup - YouTube](https://www.youtube.com/watch?v=zmvU5Atpc5U)
- [The Interface Class](https://gradio.app/guides/the-interface-class)
- [(1572) Render Arquitectura - ComfyUI Flux Controlnet - YouTube](https://www.youtube.com/watch?v=PAy4dCJoKP0)
- [Nodo de dibujo para ComfyUI (ComfySketch) : r/comfyui](https://www.reddit.com/r/comfyui/comments/1qvo6m7/drawing_node_for_comfyui_comfysketch/?tl=es-419)
- [(1573) Create SEAMLESS AI Timelapse Videos from frames (both cloud and](https://www.youtube.com/watch?v=xVMpO5lX2NA&t=205s)
- [(1573) Create Exploded Site Diagrams in 3 Mins with AI #airilab #aiarc](https://www.youtube.com/watch?v=KthZCHEymEA)
- [cómo hago un croquis con comfyui - Buscar con Google](https://www.google.com/search?q=c%C3%B3mo+hago+un+croquis+con+comfyui&oq=c%C3%B3mo+hago+un+croquis+con+comfyui&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigAdIBCTU1MjBqMGoxNagCCLACAfEFqwzFLyEweiDxBasMxS8hMHog&sourceid=chrome&source=chrome.rb&ie=UTF-8#fpstate=ive&vld=cid:ddaa93ff,vid:LzMS0E72s4c,st:0)

**ArchViz UE-Comfy** (35 bookmarks · software arq)

- [Manual de Tutoriales de la Wiki de ComfyUI \| ComfyUI Wiki](https://comfyui-wiki.com/es)
- [ComfyUI Workflows - ComfyUI](https://www.comfy.org/es/workflows/)
- [ComfyUI – Inteligencia Artificial avanzada para Renders \| 3DCollective](https://3dcollective.es/tutorial/comfyui/)
- [(900) Introducción a ComfyUI - Inteligencia Artificial avanzada para R](https://www.youtube.com/watch?v=aTrapaTRi9A&t=1357s)
- [*Unsaved Workflow (2) - ComfyUI](https://cloud.comfy.org/?utm_source=workflow_hub&utm_medium=site_CTA&utm_campaign=hub_preview&utm_content=site_button&_gl=1*1k9zvx0*_ga*MTM0NjU4MjI3Ni4xNzc3NjQ3NTE1*_ga_C8GM67L51P*czE3Nzc2NDc1MTUkbzEkZzAkdDE3Nzc2NDc1MTUkajYwJGwwJGgw)
- [(901) Unreal Engine para ArchViz - Introducción - Primeros pasos - You](https://www.youtube.com/watch?v=YgnOS0G4UEM)
- [Photon - v1 \| Stable Diffusion 1.x Checkpoint \| Civitai](https://civitai.com/models/84728/photon)
- [Lesson: The WAT Framework - 7 Day AIS Challenge · AI Automation Societ](https://www.skool.com/ai-automation-society/classroom/dda699b7?md=0e095fdae1a3417c8b565c94645a1209)
- [Diagrama en Arquitectura](https://www.i-a.com.ar/participant-page/diagrama-en-arquitectura/step/f6a3d988-ddf5-4716-be10-1632a79a5410)
- [(974) Grabar Pantalla y Webcam al mismo tiempo con OBS (2024) 🎥💻 - You](https://www.youtube.com/watch?v=y14-0aBS1uU&t=288s)
- [Creating a Music Visualizer \| PlayCanvas Developer Site](https://developer.playcanvas.com/tutorials/music-visualizer/)
- [Luma AI - Fields Dashboard](https://lumalabs.ai/dashboard/captures)
- [Creating Splats \| PlayCanvas Developer Site](https://developer.playcanvas.com/user-manual/gaussian-splatting/creating/)
- [Jawset Store](https://www.jawset.com/shop/pricing/)
- [How to Rhino Premium - May 2026 Launch](https://howtorhino.com/premium/launch/#inventory)
- [Workshop Introduction and Schedule 📅 - Premium Workshop \| May 18th - 2](https://www.skool.com/howtorhino/classroom/8c2010fd?md=19162322f42d4bd8af7b85d066429db9)
- [Recursos Gratuitos: Meta Ads, IA y Ventas \| Damián Fiorito](https://damianfiorito.com/recursos/)
- [Generative Session \| Runway AI](https://app.runwayml.com/video-tools/teams/proyectopi31416/ai-tools/generate?tool=video&mode=tools)
- [Crear espacio metaverso educativo](https://chatgpt.com/c/68c1c8cb-ad38-8320-8216-893828edc2ef)
- [La guía definitiva para los estilos de representación arquitectónica -](https://architecturalmodels.net/es/the-definitive-guide-to-architectural-rendering-styles/)
- [The Diffusion Architect – Studio Ismail Seleit \| PAACADEMY](https://paacademy.com/course/the-diffusion-architect)
- [ComfyUI for Architects vol.2 - Workshop #09 - How to Rhino Premium](https://howtorhino.com/premium/workshops/comfyui-vol2/)
- [Rhino and Grasshopper Courses by How to Rhino](https://howtorhino.com/rhino-and-grasshopper-courses/)
- [Unlock Stunning Architecture and Interior Designs with AI-Powered FLUX](https://comfyui.org/en/ai-powered-architecture-and-interior-design)
- [Train Your Own Stable Diffusion LoRA in 2026: Complete Guide \| Sanj](https://sanj.dev/post/train-stable-diffusion-lora-self-portraits/)
- [(1406) Open Lecture "STATE OF AI AT MVRDV" - YouTube](https://www.youtube.com/watch?v=MbfxADJsR0M)
- [Comfy Cloud MCP - ComfyUI](https://docs.comfy.org/agent-tools/cloud#claude-code)
- [Comfy CLI - ComfyUI](https://docs.comfy.org/agent-tools/comfy-cli)
- [The Best Open-Source Image Generation Models in 2026](https://www.bentoml.com/blog/a-guide-to-open-source-image-generation-models)
- [Self-Hosted Commercial License Terms \| Black Forest Labs](https://bfl.ai/legal/self-hosted-commercial-license-terms)
- [How does FLUX licensing work? \| Black Forest Labs Knowledge Base](https://help.bfl.ai/articles/9272590838-self-serve-dev-license-overview-pricing)
- [Model Training & Fine-Tuning \| ModelsLab](https://modelslab.com/models?feature=training)
- [stablediffusionapi (Stable Diffusion API)](https://huggingface.co/stablediffusionapi)
- [Workflow Optimization: 6 Workflow Strategies for Your Team](https://clickup.com/blog/workflow-optimization/?_gl=1*mwvwv2*_up*MQ..*_gs*MQ..&gclid=Cj0KCQjwmK_CBhCEARIsAMKwcD7HUydhMU51mxVXtd265mf2lXBc2uCiqqFY8nVSlk8RYeZdX2X6ORAaAmA2EALw_wcB&gbraid=0AAAAACR5vIIgIY1Srrg_qoEsofTVKcDR9)
- [r/clickup Wiki: Mastering ClickUp Resources](https://www.reddit.com/r/clickup/wiki/clickupresources/)

**apps** (31 bookmarks · sin categoria)

- [Resultados de búsqueda \| Udemy](https://www.udemy.com/courses/search/?src=ukw&q=vibecoding&price=price-free)
- [Tutorial gratuito sobre Desarrollo de software - Vibecoding 101 \| Udem](https://www.udemy.com/course/vibecoding-101/)
- [Course: Vibecoding 101 \| Udemy](https://www.udemy.com/course/vibecoding-101/learn/lecture/50826373#overview)
- [Cursos en línea: aprende de todo y a tu propio ritmo \| Udemy](https://www.udemy.com/personal-plan/)
- [Create Account - FlutterFlow](https://app.flutterflow.io/create-account?plan=free)
- [Kilo Code - Pricing](https://kilocode.ai/pricing)
- [Vercel: Build and deploy the best web experiences with the AI Cloud](https://vercel.com/)
- [Free Text to Speech & AI Voice Generator \| ElevenLabs](https://start.elevenlabs.io/brand/v1?utm_source=google&utm_medium=cpc&utm_campaign=t3_brandsearch_brand_english&utm_id=22864149315&utm_term=elevenlabs&utm_content=brand_-_brand&gad_source=1&gad_campaignid=22864149315&gbraid=0AAAAAp9ksTEZemWvO44bpduUjZJGMDOpI&gclid=Cj0KCQjwuKnGBhD5ARIsAD19RsY8aySUsEkSJPqqSSrh5Yx9Ty5Kt6PtM9pwFCt-P9WjsSMSNCkqnMwaAiaREALw_wcB)
- [ElevenLabs Agents \| ElevenLabs](https://elevenlabs.io/app/agents/new?welcome=true)
- [Wispr Flow \| Effortless Voice Dictation](https://wisprflow.ai/)
- [Bonus Vibe Code Day](https://franconejos.com/bonus-vibe-code-day)
- [Cursos gratis de No-code en español \| NocodeHackers](https://www.nocodehackers.es/cursos)
- [Construction project management app - Claude](https://claude.ai/chat/c2ca55fe-8d29-4ea4-b567-87c6e51959e9)
- [Google Gemini](https://gemini.google.com/app/6e2658e09b934b86?hl=es)
- [cuales son los gremios implicados en una obra - Buscar con Google](https://www.google.com/search?q=cuales+son+los+gremios+implicados+en+una+obra&oq=cuales+son+los+gremios+implicados+en+una+obra&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigAdIBCDcxNDJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)
- [(208) Ver más tarde - YouTube](https://www.youtube.com/playlist?list=WL)
- [Mejores Páginas Web De Cursos Gratuitos (con certificado) - YouTube](https://www.youtube.com/watch?v=IA2pr0kHzd0&list=WL&index=24&t=270s)
- [(211) Las 10 MEJORES aplicaciones n8n lanzadas en 2025 (Ojalá las hubi](https://www.youtube.com/watch?v=hpagfM-r2Bs&list=WL&index=29)
- [(211) Activé los agentes de Perplexity… y esto se descontroló - YouTub](https://www.youtube.com/watch?v=ynx_5uWL1ZM&list=WL&index=34&t=1055s)
- [Whop: Empieza un negocio, aprende una habilidad nueva y construye una](https://whop.com/dashboard/start/)
- [El Test de Turing - Podcast de \| Twitter, TikTok \| Linktree](https://linktr.ee/eltestdeturing)
- [Race to Certification 2025 \| Oracle University](https://education.oracle.com/race-to-certification-2025)
- [Artificial Intelligence \| IBM SkillsBuild](https://skillsbuild.org/adult-learners/explore-learning/artificial-intelligence)
- [User Experience Design \| IBM SkillsBuild](https://skillsbuild.org/adult-learners/explore-learning/user-experience-design)
- [Claude Code: A Highly Agentic Coding Assistant - DeepLearning.AI](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)
- [Best Vibe Coding Tools - September 2025 - Cybernews.com](https://en.cybernews.com/lp/best-ai-app-builders-1/vibe-coding/?campaignId=23020994796&adgroupId=183900030365&adId=774512751326&targetId=kwd-2403793734679&device=c&gunique=Cj0KCQjwuKnGBhD5ARIsAD19RsaGK4Eqaw0wtQwf7yIITe3Y-gE8cTRaPy3kG5J7QTyHlzwF2_QeH9caAsz6EALw_wcB&gad_source=1&gad_campaignid=23020994796&gbraid=0AAAAACyNk23GpiE7DNBeAmva-dLjYpftT&gclid=Cj0KCQjwuKnGBhD5ARIsAD19RsaGK4Eqaw0wtQwf7yIITe3Y-gE8cTRaPy3kG5J7QTyHlzwF2_QeH9caAsz6EALw_wcB)
- [Hostinger \| Horizons](https://horizons.hostinger.com/?was_new_account_created=1&_gl=1%2Ahngov5%2A_ga%2ANjk2OTYxNDQ3LjE3NTgxNTI2Mzc.%2A_ga_73N1QWLEMH%2AczE3NTgxNTI2MzckbzEkZzEkdDE3NTgxNTI5MDAkajYwJGwwJGgxODI4NDAyNjQ1JGRRa0Q4NzNMRWdoQ3hablhtd2NPWE43RUJkVnFxQTQ3cEZ3%2A_gcl_au%2AMTgyODg5NDYwNS4xNzU4MTUyNjM3)
- [Build Apps with AI in Minutes \| Base44](https://base44.com/?utm_campaign=af_3256132&impact_click_id=2PxWbjUGTxycTYBzF3wHB2XyUkp1wo3MNWCA040&experiment_id=25619%5E3256132%5E2477538%5Ehp&irgwc=1)
- [Bolt AI builder: Websites, apps & prototypes](https://bolt.new/)
- [Crea una App con IA en minutos \| Base 44](https://base44.com/es?utm_source=google&utm_medium=cpc&utm_campaign=23024226619^185747690775^search%20-%20lang&experiment_id=vibe%20coding^b^774163626236^&gad_source=1&gad_campaignid=23024226619&gbraid=0AAAAADwEfwXsdq5fM2tTOX98FT0zaSN7W&gclid=Cj0KCQjw267GBhCSARIsAOjVJ4GlULU6L6STnP0877447VW_-_fJio5VvANv7rRVzOy8oSIkj6h3Uz8aAtBzEALw_wcB)
- [Google AI Studio](https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=FY25-global-DR-gsem-SKWS-1710442&utm_content=text-ad-none-any-DEV_c-CRE_771552445641-ADGP_Hybrid%20%7C%20SKWS%20-%20BRO%20%7C%20Txt-Development%20%28Growth%29-Gen%20AI-KWID_1772645501753-kwd-1772645501753&utm_term=KW_ai%20generated%20app-ST_ai%20generated%20app&gclsrc=aw.ds&gad_source=1&gad_campaignid=22948282299&gbraid=0AAAAACn9t66w_1ct8OEDw8f6NWDqrRSvW&gclid=CjwKCAjwlt7GBhAvEiwAKal0cvEhlnUySU009PJQUM2NcX18jQA7Zajgxwuipb3rIwjdnMr1AMJgXBoCVBoQAvD_BwE)

**Apps** (26 bookmarks · sin categoria)

- [Open Broadcaster Software \| OBS](https://obsproject.com/es)
- [Open Collective - Haz que tu comunidad sea sostenible. Recolecta y gas](https://opencollective.com/how-it-works)
- [ClickUp™ \| The everything app for work](https://clickup.com/)
- [Asana](https://app.asana.com/)
- [Studio π - Slack](https://app.slack.com/client/T08AS0X0771/D08BVMB80NL?source=browser)
- [Patreon para artistas visuales — Patreon](https://www.patreon.com/es-ES/creators/visualartists#build-community-around-your-art)
- [IA \| PromeAI](https://www.promeai.pro/es/ai-tools)
- [OpenProject - Open Source Project Management Software](https://www.openproject.org/)
- [⬇️ Flecha Hacia Abajo Emoji](https://emojipedia.org/es/flecha-hacia-abajo)
- [Adobe Acrobat Documents](https://acrobat.adobe.com/link/documents/files/?pdfnow%21verb=split-pdf&x_api_client_id=adobe_com&x_api_client_location=split_pdf&uri=urn%3Aaaid%3Asc%3AUS%3A1237a6bd-23c4-4caa-a609-fbe53a79afb4&scrollToUri=urn%3Aaaid%3Asc%3AUS%3Ae717da85-f7aa-4eca-bf95-c976acb9ac25&sortOrder=descending&orderBy=modified)
- [inline-project-management-what-is-a-flow-chart-IG-2x.png (1800×10080)](https://assets.asana.biz/m/397bc1d973f4719f/original/inline-project-management-what-is-a-flow-chart-IG-2x.png)
- [Mapa de procesos: Transparencia en su arquitectura de procesos](https://www.gbtec.com/es/recursos/mapa-de-procesos/)
- [Lucidchart \|](https://www.lucidchart.com/pages/es)
- [Sign in - Napkin AI](https://app.napkin.ai/signin?login_processing=true)
- [La servilleta de ideas - Miro](https://miro.com/app/board/uXjVIesL-pI=/)
- [My Workspace \| Jotform](https://www.jotform.com/myworkspace/)
- [PDF24 Tools: Herramientas PDF en línea gratuitas y fáciles de usar](https://tools.pdf24.org/es/)
- [Símbolos PI - 𝝿](https://es.piliapp.com/symbol/pi/)
- [Viñetas (•) para copiar y pegar - Herramientas y Utilidades](https://herramientasyutilidades.com/texto/vinetas/)
- [11 Free Customer Journey Map Templates \| ClickUp](https://clickup.com/blog/customer-journey-templates/?utm_source=google-pmax&utm_medium=cpc&utm_campaign=gpm_cpc_ar_nnc_pro_trial_all-devices_tcpa_lp_x_all-departments_x_pmax&utm_content=&utm_creative=_____&gad_source=1&gclid=Cj0KCQjwnui_BhDlARIsAEo9GuvZ0QnV3HxSQunlJxZwTLmBLccLIk88Av3_3dEYXbfZT_mcWzk7KaEaAjHREALw_wcB)
- [Interactive Journey Map (Community) – Figma](https://www.figma.com/design/pVKKoyj4Zhm3PqLMhYwrE3/Interactive-Journey-Map--Community-?node-id=1440-2031&t=9wgilzVhQSEl8T5t-0)
- [LookX AI Cloud](https://www.lookx.ai/)
- [AJM - Software Development](https://andrewmarsh.com/software/)
- [LookX AI Cloud](https://www.lookx.ai/pc/home)
- [Alumni](https://alumni.education/?_gl=1%2aiaoqiy%2a_gcl_aw%2aR0NMLjE3NDQ4NDk0NzAuQ2owS0NRandxdjJfQmhDMEFSSXNBRmI1QWM4TzVKU0lTRHVCWWZxYkhWSktSc1cxSXR2Q3BkUmNGcEFPTVIwSC1sem5JZmtUN2s2ejBxc2FBb1dwRUFMd193Y0I.%2a_gcl_au%2aMTA5MTY1OTgwMi4xNzM5NzE0MjIx%2a_ga%2aMTk2NDI3ODI5MC4xNzM5NzE0MjIx%2a_ga_00635ZCKEM%2aMTc0NDg0OTQ3MC4zLjAuMTc0NDg0OTQ3MC42MC4wLjQ4Mjg5MTYzNA..%2a_ga_5P142BYYT2%2aMTc0NDg0OTQ3MC4zLjAuMTc0NDg0OTQ3MC4wLjAuMjEzMTg3MDY4Mw)
- [asmitools.com](http://ww5.asmitools.com/)

**Presupuestos** (20 bookmarks · construccion)

- [ARQ_Clarin](https://www.kiosco.clarin.com/arq/)
- [COSTOS - CIFRAS ON LINE](https://www.cifrasonline.com.ar/costos/)
- [Calcumat](https://www.calcumat.com.ar/index.php)
- [Costo de la construcción por metro cuadrado - AyC](https://aycrevista.com.ar/precios-la-construccion/costo-metro-cuadrado/)
- [Costos de mano de obra](https://www.electroinstalador.com/costos-mano-obra-a1640)
- [Precios \| Remodelaciones Integ](https://www.remodelacionesintegrales.com.ar/precios)
- [Construction Management Software for Remodeling \| BuildBook](https://www.buildbook.co/remodelers)
- [TrulySmall Invoices - trulysmall.™](https://trulysmall.com/)
- [Modern Project & Work Management Platform \| Smartsheet](https://www.smartsheet.com/)
- [Sheet - General Ledger (01-January) - Smartsheet.com](https://app.smartsheet.com/sheets/JFm3JMFW8c6wP5HWMvJfW9jv4C24fFMmXXMmgvg1?view=grid)
- [Gantt Chart Confirmation](https://www.buildbook.co/gantt-chart-confirmation)
- [Free Construction Estimate and Proposal Template](https://www.buildbook.co/free-construction-estimate-template)
- [Smartsheet](https://app.smartsheet.com/b/home?mt=41&wx=zth1dI0JNCrnNIlYLCAefbiVDHJl8I7N1WItHxFxtsOCO1y9R_HCyC8MX8tyMY_Q&lang=en_US)
- [AAIERIC - Costos Sugeridos de Mano de Obra - Enero 2025](https://aaieric.org.ar/costos-mano-de-obra)
- [Durlock-Rend.](https://euroseco.com.ar/descargas/Consumo-de-materiales-por-m2.pdf)
- [Látex Exterior \| Casablanca](https://casablanca.com.ar/product-category/latex-exterior/?gad_source=1&gclid=CjwKCAiA74G9BhAEEiwA8kNfpbPf6x-1tuOpMQsWSXDniKUV5GfoJCnjaXuBmkO4f-o-_Q9sH1C-WBoCCIMQAvD_BwE)
- [revear.com.ar Disponible y a la venta - Sedo.com](https://sedo.com/search/details/?partnerid=324561&language=es&domain=revear.com.ar&origin=sales_lander_5&utm_medium=Parking&utm_campaign=offerpage)
- [Calculador de consumo](https://arg.sika.com/revear/es/calculador-de-consumo.html?gad_source=1&gclid=CjwKCAiA74G9BhAEEiwA8kNfpeXtt3C0xsiRnX9XKThFEleKKE8CYHnbPJzdjgkQy2MkNRd0WPU0KxoCoWYQAvD_BwE)
- [Recomendamos](https://www.elgalgo.com.ar/recomendamos/#toggle-id-4)
- [Cómputo y presupuesto - Colegio de Arquitectura y Urbanismo de la Prov](https://capsf.ar/computo-y-presupuesto/)

**Other Bookmarks** (19 bookmarks · personal)

- [Pi (π): las rarezas del número con más fans del mundo - BBC News Mundo](https://www.bbc.com/mundo/articles/c84d1lzymrwo#:~:text=Como%20dec%C3%ADamos%20al%20inicio%2C%20el,que%20no%20siguen%20ning%C3%BAn%20patr%C3%B3n.)
- [Número π - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/N%C3%BAmero_%CF%80)
- [Descargar visores de Autodesk \| Visores en línea gratuitos \| Productos](https://www.autodesk.com/latam/viewers?us_oa=dotcom-us&us_si=6f80dbfd-6eaf-42dd-a29f-6b9f1ee92f93&us_st=dwf)
- [Autodesk DWG TrueView \| DWG Viewer](https://www.autodesk.com/products/dwg-trueview/overview)
- [Autodesk Viewer \| Free Online File Viewer](https://viewer.autodesk.com/)
- [The American Institute of Architects: AIA](https://www.aia.org/)
- [Architects' Essential AutoCAD Training \| Autodesk Software](https://archademia.com/lessons/autocad/)
- [Cómo realizar una desinstalación limpia de productos de Autodesk en Wi](https://www.autodesk.com/es/support/technical/article/caas/sfdcarticles/sfdcarticles/ESP/Clean-uninstall.html)
- [Paseando entre árboles de Pitágoras — Cuaderno de Cultura Científica](https://culturacientifica.com/2021/12/01/paseando-entre-arboles-de-pitagoras/)
- [Pythagorean tree generator](https://www.cs.mcgill.ca/~avieth/fractal/)
- [iLoveIMG \| The fastest free web app for easy image modification.](https://www.iloveimg.com/)
- [Aspect Ratio Calculator (16:9, 4:3, Custom & More)](https://calculateaspectratio.com/#google_vignette)
- [Rhinoceros 8.5.24072.13001 (Multilenguaje)](https://aportesingecivil.com/rhinoceros-8-multilenguaje/#comments)
- [Convirtiendo... — Convertio](https://convertio.co/es/download/fd6d3d267d95a712a51c181b928011be30a908/)
- [Convierte JPG al formato AutoCAD DXF gratis - ImageToStl](https://imagetostl.com/es/convertir/archivo/jpg/a/dxf)
- [Convierte cualquier imagen a vector: 6 métodos para vectorizar una ima](https://www.stickermule.com/ar/blog/how-to-convert-any-image-to-vector)
- [Map near Olivos, Buenos Aires, AR \| CADMAPPER](https://cadmapper.com/pro/extracts/3666a7dd-b74f-44c2-a23f-91236c52dcc2)
- [Andrej Karpathy](https://karpathy.ai/)
- [Chat with Orbie — Orbit](https://app.orbitagents.xyz/chat)

**GCBApp** (17 bookmarks · construccion)

- [Un mapa tridimensional de toda la ciudad de Buenos Aires, disponible p](https://www.archdaily.cl/cl/933447/un-mapa-tridimensional-de-toda-la-ciudad-de-buenos-aires-disponible-para-su-descarga-y-visualizacion)
- [datosgcba/Ciudad-3D: Repositorio Frontend Ciudad 3D](https://github.com/datosgcba/Ciudad-3D?tab=readme-ov-file)
- [Documentacion](https://datosabiertos-apis.buenosaires.gob.ar/BA_Root/Documentacion?schema_name=usig_geocoder)
- [Documentacion](https://datosabiertos-apis.buenosaires.gob.ar/BA_Root/Documentacion?schema_name=catastro)
- [Buenos Aires Data - Edificios Públicos en 3D](https://data.buenosaires.gob.ar/dataset/edificios-publicos-3d)
- [Buenos Aires Data - Tejido Urbano](https://data.buenosaires.gob.ar/dataset/tejido-urbano)
- [Buenos Aires Data - Manzanas](https://data.buenosaires.gob.ar/dataset/manzanas)
- [Buenos Aires Data - Planchetas Código de Planeamiento Urbano](https://data.buenosaires.gob.ar/dataset/planchetas-codigo-planeamiento-urbano)
- [Buenos Aires Data - Parcelas.](https://data.buenosaires.gob.ar/dataset/parcelas)
- [Buenos Aires Data - Código Urbanístico](https://data.buenosaires.gob.ar/dataset/codigo-urbanistico)
- [Buenos Aires Data - Franja Edificable: líneas](https://data.buenosaires.gob.ar/dataset/franja-edificable-lineas)
- [Spatial without Compromise · QGIS Web Site](https://qgis.org/)
- [Buenos Aires Data - Servicio de información normativa.](https://data.buenosaires.gob.ar/dataset/servicio-informacion-normativa)
- [Códigos: Toda la información \| CPAU](https://cpau.org/nota/38235)
- [Datos abiertos de edificación de CABA - Communities / Argentina - Open](https://community.openstreetmap.org/t/datos-abiertos-de-edificacion-de-caba/117029/39)
- [Ciudad 3D](https://ciudad3d.buenosaires.gob.ar/)
- [GESTORIA UNO - Consultas](https://www.gestoriauno.com.ar/genen/contacto/)

**CASABLANCA** (16 bookmarks · construccion)

- [Profesional \| Casablanca](https://casablanca.com.ar/product-category/profesional/)
- [Fichas técnicas-Cielo Rasos](https://casablanca.com.ar/wp-content/uploads/2021/02/Fichas-tecnicas-Cielo-Rasos.pdf)
- [PRO LÁTEX INTERIOR \| Casablanca](https://casablanca.com.ar/product/pro-latex-interior/)
- [Fichas técnicas-Pro latex interior](https://casablanca.com.ar/wp-content/uploads/2021/02/Fichas-tecnicas-Pro-latex-interior-1.pdf)
- [PRO MEMBRANA \| Casablanca](https://casablanca.com.ar/product/pro-membrana/)
- [Fichas técnica Casablanca Pro- MEMBRANA](https://casablanca.com.ar/wp-content/uploads/2021/09/Fichas-tecnica-Casablanca-Pro-MEMBRANA-2.pdf)
- [PRO TAPAGOTERAS \| Casablanca](https://casablanca.com.ar/product/pro-tapagoteras/)
- [Fichas técnica Casablanca Pro- TAPAGOTERAS](https://casablanca.com.ar/wp-content/uploads/2021/09/Fichas-tecnica-Casablanca-Pro-TAPAGOTERAS-1.pdf)
- [Fichas técnicas-Fijador](https://casablanca.com.ar/wp-content/uploads/2021/02/16-01-49Fijador.pdf)
- [SELLADOR FIJADOR \| Casablanca](https://casablanca.com.ar/product/sellador-fijador/)
- [MULTIACCIÓN 3 EN 1 \| Casablanca](https://casablanca.com.ar/product/esmaltes-multiaccion/)
- [Fichas técnicas-ESMALTE  SINTETICO MULTIACCION](https://casablanca.com.ar/wp-content/uploads/2022/02/ESMALTE_SINTETICO_MULTIACCION_c.pdf)
- [BARNIZ INTERIOR \| Casablanca](https://casablanca.com.ar/product/barniz-interior/)
- [Ficha tecnica_Barniz interior brillante](https://casablanca.com.ar/wp-content/uploads/2021/02/Ficha-tecnica_Barniz-interior-brillante.pdf)
- [Base para Revestimientos Texturados \| Revear](https://arg.sika.com/revear/es/soluciones-revear/revestimientos-texturados/revear-base-paratexturado.html)
- [Revear Base para texturado](about:invalid#zGuavaz)

**PC's** (15 bookmarks · personal)

- [FullH4rd - La tienda Gamer #1 de Argentina](https://fullh4rd.com.ar/)
- [Comparador de productos \| PcComponentes.com](https://www.pccomponentes.com/comparador)
- [Versus \| Compáralo todo](https://versus.com/es)
- [Página de inicio \| PC Builds](https://pc-builds.com/es/)
- [HardGamers - Buscador de hardware para encontrar tu PC Gamer al mejor](https://www.hardgamers.com.ar/)
- [COMPRA GAMER](https://compragamer.com/armatupc?gad_source=1&gclid=Cj0KCQjwhYS_BhD2ARIsAJTMMQZIp_G1YPlWqndDhjhfUPsgovztxoKqbuXcOymskTO7REjLQotRQa0aAgAJEALw_wcB)
- [PromeAI - Generador de arte AI gratuito: Da vida a la creatividad](https://www.promeai.pro/es/home)
- [Tripo Versión Web \| Diseña libremente, personaliza a tu gusto y crea t](https://www.tripo3d.ai/app/home?utm_source=google&utm_medium=cpc&utm_campaign=ALL&utm_term=tripo3d&gad_source=1&gclid=Cj0KCQjw2N2_BhCAARIsAK4pEkX5Kwampab0pAjzHUi-uHGGhTIlCIDyJ4XbDMV_2xNyEZ8M-hHb3XoaArPNEALw_wcB)
- [Pitch](https://app.pitch.com/app/dashboard/152b5d21-01e4-4ad5-8dbd-130d126ac756)
- [Presentations.AI](https://app.presentations.ai/#/ideatodeck)
- [Rhino Grasshopper Tutorials & Scripts](https://parametrichouse.com/rhino-grasshopper/)
- [cursos.nocodehackers.es/inicio](https://cursos.nocodehackers.es/inicio)
- [NotebookLM](https://notebooklm.google.com/?utm_source=1pnlm&utm_medium=web&utm_campaign=nlm_site_home_cta&utm_smc=1pnlm_web_nlm_site_home_cta&utm_content=&_gl=1*pzrth3*_ga*MjA1MDY2NDg0NC4xNzU3NTM4MDcz*_ga_W0LDH41ZCB*czE3NTkyNjYxMTEkbzQkZzEkdDE3NTkyNjYxMTYkajU1JGwwJGgw)
- [Creación de agentes conversacionales con Copilot Studio](https://platzi.com/cursos/copilot-studio/creacion-de-agentes-conversacionales-con/)
- [Construcción de Marca Personal en la Era Digital](https://platzi.com/cursos/marca-personal/por-que-necesitas-una-marca-personal/)

**busqueda_celular** (12 bookmarks · personal)

- [Selección Tuenti](https://tienda.tuenti.com.ar/seleccion-tuenti.html?movistar_installment_filter=2563&movistar_nfc=286&product_list_order=low_to_high)
- [TCL K70 4G con funda](https://tienda.tuenti.com.ar/tcl-k70-4g-con-funda.html)
- [TCL K70 Power 4GB ram con funda](https://tienda.tuenti.com.ar/tcl-k70-power-4gb-ram-con-funda.html)
- [Catálogo - Tienda Macro](https://www.tiendamacro.com.ar/catalog/tecnologia-celulares?b%5B%5D=149&b%5B%5D=1099&o=price-asc)
- [Celular Tecno Pova 6 (256+8gb) Meteorite Grey](https://www.tiendamacro.com.ar/products/celular-tecno-pova-6-256-8gb-meteorite-grey)
- [Tcl 50 Nxtpaper Pro Blanco 512 Gb](https://www.tiendamacro.com.ar/products/tcl-50-nxtpaper-pro-5g-8gb-512gb-bl)
- [Celular TCL 60R 4+128GB Gris](https://www.tiendamacro.com.ar/products/celular-tcl-60r-4-128gb-gris)
- [Celular Tcl 60R 4G 4 + 4 Gb 128 Gb Nfc Pure White - On City](https://www.oncity.com/celular-tcl-60r-4g-4---4-gb-128-gb-nfc-pure-white-157327/p)
- [Celular Motorola Moto G06 4G 4 Gb 128 Gb Tapestry - On City](https://www.oncity.com/celular-motorola-moto-g06-4g-4-gb-128-gb-tapestry-157231/p)
- [Ofertas Celulares Hasta 24 cuotas - On City](https://www.oncity.com/tecnologia/celulares/celulares/cuotas-sin-interes?initialMap=c,c&initialQuery=tecnologia/celulares&map=category-1,category-2,category-3,envio&order=OrderByPriceASC)
- [P](https://pomofocus.io/)
- [WW](https://web.whatsapp.com/)

**E#** (12 bookmarks · educacion)

- [CH](https://www.coderhouse.com/ar?pipe_source=google&pipe_medium=cpc&pipe_campaign=1&gad_source=1&gclid=CjwKCAiA0rW6BhAcEiwAQH28Ip_A_zp25p1JQYjLaEaeGTq9kPxD3a8BPY0ksb-lH9n89xRTVM1zWRoC0oUQAvD_BwE)
- [Dom](https://www.domestika.org/es/courses/popular)
- [U \|](https://www.udemy.com/)
- [Platzi: Cursos online profesionales de tecnología](https://platzi.com/mis-rutas/)
- [Unity \| Learn](https://learn.unity.com/?signup=true)
- [Architecture & Building Engineering \| Autodesk University](https://www.autodesk.com/autodesk-university/architecture-building-engineering)
- [Ambiente de trabajo BIM - FreeCAD Documentation](https://wiki.freecad.org/BIM_Workbench/es)
- [Π](https://www.patreon.com/c/P31416?fromConcierge=true)
- [1º Escuela de Arte, Animación Y Videojuegos de Latinoamérica](https://www.imagecampus.edu.ar/)
- [Visualización Arquitectónica](https://www.imagecampus.edu.ar/programas-profesionales/visualizacion-disenos-arquitectonicos)
- [Unreal Engine 5 Fundamentals Online - Via Streaming - Image Campus - O](https://www.imagecampus.edu.ar/cursos-software/cursos-software-distancia-online/introduccion-a-unreal-engine-online-via-streaming#none)
- [▷ FREE SHEET MUSIC PDF : Free Piano Sheet Music PDF Download](https://sheetmusic-free.com/)

**VPS's** (12 bookmarks · personal)

- [AWS Console - Signup (6mFREE)](https://signin.aws.amazon.com/signup?request_type=register)
- [Paso 1 de 2 – Prueba gratuita – Consola de Google Cloud (90d)](https://console.cloud.google.com/freetrial/signup/tos?_gl=1*j2kxeg*_up*MQ..&gclid=CjwKCAjwr8LHBhBKEiwAy47uUnmFD1H7hTIgnhh5GYJE0TtcsiXjngvui__IvzVxMc0tx9aHXgzNCBoCG9oQAvD_BwE&gclsrc=aw.ds&facet_utm_source=google&facet_utm_campaign=latam-AR-all-es-dr-BKWS-all-all-trial-b-dr-1710136-LUAC0020851&facet_utm_medium=cpc&facet_url=https:%2F%2Fcloud.google.com%2Flearn%2Fwhat-is-a-virtual-private-server&pli=1)
- [Modo Gratuito de Oracle Cloud \| Oracle América Latina](https://www.oracle.com/latam/cloud/free/#always-free)
- [The AI PaaS for Deploying, Managing, and Scaling Apps](https://www.heroku.com/)
- [Los Mejores Precios De Hosting En Argentina](https://www.hostinger.com/ar/precios/n8n-hosting)
- [Host, run, and code Python in the cloud: PythonAnywhere](https://www.pythonanywhere.com/)
- [Te damos la bienvenida a Colaboratory - Colab](https://colab.research.google.com/)
- [VPS con la mejor relación calidad-precio \| Contabo](https://contabo.com/es/vps/)
- [Easypanel - Modern Server Control Panel](https://easypanel.io/)
- [ClawCloud Run \| Build, Deploy, Manage & Run in Cloud-Native Platform](https://run.claw.cloud/)
- [🖖 3 VPS GRATIS PARA SIEMPRE \| 💯 4CPU y 24GB de RAM - YouTube](https://www.youtube.com/watch?v=ypUFAa6ee7g)
- [Zero2Launch AI Automation](https://www.skool.com/zero2launch-ai-automation-5951)

**COMFYUI** (10 bookmarks · software arq)

- [Miniconda - Anaconda](https://www.anaconda.com/docs/getting-started/miniconda/main#is-miniconda-free-for-me)
- [(203) Install Stable Diffusion on windows in one click! AMD GPU's full](https://www.youtube.com/watch?v=4mcdTwFUxMQ)
- [(203) AMD GPU + Windows + ComfyUI! How to get comfyUI running on windo](https://www.youtube.com/watch?v=8rB7RqKvU5U)
- [Ejecutar ComfyUI en Google Colab \| ComfyUI Wiki](https://comfyui-wiki.com/es/install/install-comfyui/run-comfyui-on-cloud)
- [(203) AMD for ComfyUI - How to Install Stable Diffusion with Radeon GP](https://www.youtube.com/watch?v=RtSNtwjHuYQ)
- [Ayuda para configurar ComfyUI (AMD+Windows) : r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1k4igf2/help_with_setting_up_comfyui_amdwindows/?tl=es-419)
- [(203) How to Install ComfyUI in 4 Minutes For FREE \| Stable Diffusion](https://www.youtube.com/watch?v=E_D7y0YjE88)
- [ComfyUI \| Generate video, images, 3D, audio with AI](https://www.comfy.org/download)
- [ArchitectureRealMix - v1.1 \| Stable Diffusion Checkpoint \| Civitai](https://civitai.com/models/84958/architecturerealmix)
- [Generación de imágenes con Gemini (también conocido como Nano Banana)](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)

**GCBA-INFO-TEC** (9 bookmarks · construccion)

- [Fichas poligonales \| Buenos Aires Ciudad - Gobierno de la Ciudad Autón](https://buenosaires.gob.ar/jefaturadegabinete/desarrollo-urbano/informacion-para-tu-proyecto/fichas-poligonales)
- [FICHA POLI](http://ssplan.buenosaires.gov.ar/ficha_poli/FICHA_POLI_list.php)
- [CROQUIS PARCELA](http://www.ssplan.buenosaires.gov.ar/croquis_parcela/CROQUIS_PARCELA_list.php)
- [(2) Guía para elaborar planos - YouTube](https://www.youtube.com/playlist?list=PLhA9z8qhq0JlCeby4cXuZ6fzzCg1g6XcF)
- [Manzanas Atípicas \| Buenos Aires Ciudad - Gobierno de la Ciudad Autóno](https://buenosaires.gob.ar/jefaturadegabinete/desarrollo-urbano/informacion-para-tu-proyecto/manzanas-atipicas)
- [Medidas perimetrales y ancho de calles \| Buenos Aires Ciudad - Gobiern](https://buenosaires.gob.ar/jefaturadegabinete/desarrollo-urbano/informacion-para-tu-proyecto/medidas-perimetrales-y-ancho-de-calles)
- [PERI MAN](http://ssplan.buenosaires.gob.ar/peri_man/PERI_MAN_list.php)
- [Información técnica \| Buenos Aires Ciudad - Gobierno de la Ciudad Autó](https://buenosaires.gob.ar/jefaturadegabinete/desarrollo-urbano/informacion-para-tu-proyecto/informacion-tecnica)
- [Dataset \| Buenos Aires Ciudad - Gobierno de la Ciudad Autónoma de Buen](https://buenosaires.gob.ar/jefaturadegabinete/desarrollo-urbano/informacion-para-tu-proyecto/dataset)

**Agents** (9 bookmarks · ia)

- [Welcome to Chatwoot Developer Docs - Chatwoot Developer Docs](https://developers.chatwoot.com/introduction)
- [Qdrant Cloud · Clusters](https://cloud.qdrant.io/accounts/ffcacd1b-e47a-4f9e-bb69-24c832f44537/clusters?provider=aws&region=eu-west-2)
- [Redis Cloud Console](https://cloud.redis.io/#/)
- [Self-Hosted Installation Guide - Chatwoot Developer Docs](https://developers.chatwoot.com/self-hosted)
- [Qdrant Cloud · Get Started](https://cloud.qdrant.io/accounts/ffcacd1b-e47a-4f9e-bb69-24c832f44537/get-started)
- [Redis Cloud Console](https://cloud.redis.io/#/login)
- [Local Quickstart - Qdrant](https://qdrant.tech/documentation/quickstart/)
- [redis - Official Image \| Docker Hub](https://hub.docker.com/_/redis)
- [Docker Chatwoot Production deployment guide - Chatwoot Developer Docs](https://developers.chatwoot.com/self-hosted/deployment/docker)

**Nueva carpeta** (9 bookmarks · sin categoria)

- [SOFTWARE ARQ SOLAR - Buscar con Google](https://www.google.com/search?q=SOFTWARE+ARQ+SOLAR&oq=SOFTWARE+ARQ+SOLAR&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCTQ2MTc4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8)
- [Análisis solar: 8 Herramientas gratis y muy útiles - YouTube](https://www.youtube.com/watch?v=cArKuwsb1KU)
- [Decoración con IA: Top 13 Programas para decorar casas](https://ovacen.com/programa-decoracion-ia-inteligencia-artificial/)
- [Programa LookX IA: De boceto a render 3D en 1 minuto ¡Especializado en](https://ovacen.com/render-3d-arquitectura-ia/)
- [IA para hacer planos de arquitectura ¡Crea casas en minutos!](https://ovacen.com/programa-ia-planos-distribucion-vivienda-edifico/)
- [Cómo crear todos los planos y 3D de un edificio en 10 minutos \| OVACEN](https://ovacen.com/programa-automatizacion-dibujo-arquitectura/)
- [Spacio - Design code compliant buildings](https://spacio.ai/)
- [IA para hacer planos de arquitectura ¡Crea casas en minutos!](https://ovacen.com/programa-ia-planos-distribucion-vivienda-edifico/)
- [LookX AI Cloud](https://www.lookx.ai/pc/home)

**LIBROS** (8 bookmarks · libros)

- [Upload as much as you need! Unlimited volume of uploaded files. - PDFC](https://pdfcoffee.com/)
- [Proletarios](https://proletarios.org/)
- [Home Collection Home alacena 3 puertas mas 2 estantes \| Cuotas al mism](https://www.mercadolibre.com.ar/home-collection-home-alacena-3-puertas-mas-2-estantes/p/MLA27411063?pdp_filters=item_id%3AMLA1525209294&from=gshop&matt_tool=55362451&matt_word=&matt_source=google&matt_campaign_id=22107887421&matt_ad_group_id=173357569836&matt_match_type=&matt_network=g&matt_device=c&matt_creative=729634819364&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=710835605&matt_product_id=MLA27411063-product&matt_product_partition_id=2392712829741&matt_target_id=pla-2392712829741&cq_src=google_ads&cq_cmp=22107887421&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gclid=Cj0KCQiA2oW-BhC2ARIsADSIAWrcBq9sgsnCKf1PXzO8r-S2Sy_EVzokxDQMJoi5kT7LFWPJNX_1oKAaAkLDEALw_wcB)
- [Libros Maravillosos - Patricio Barros y Antonio Bravo](http://www.librosmaravillosos.com/nuevocatalogo.html)
- [Libros \| Blackie Books](https://blackiebooks.org/libros//?coleccion=grandes-guias-visuales)
- [Red Fundamentos](https://redfundamentos.com/index.html)
- [Canadian Handbook of Practice for Architects - RAIC](https://chop.raic.ca/)
- [Precios y planes de pago a Creative Cloud \| Adobe Creative Cloud](https://www.adobe.com/ar/creativecloud/plans.html)

**PROGRAMAS** (8 bookmarks · software arq)

- [Autodesk Revit 2026 (Multilenguaje)](https://aportesingecivil.com/autodesk-revit-2026-multilenguaje/)
- [Adobe Photoshop 2025 v26.5 (Multilenguaje)](https://aportesingecivil.com/adobe-photoshop-2025-multilenguaje/)
- [Lumion 2024.4.2 Pro (Multilenguaje)](https://aportesingecivil.com/lumion-2024-pro-multilenguaje/)
- [SketchUp Pro 2026 v26.0.429 (Multilenguaje) - www.links.aportesingeciv](https://www.links.aportesingecivil.com/?v=9d4p-euyrli2a)
- [AutoCAD 2022 3D Modeling – Munir Hamad](https://aportesingecivil.com/autocad-2022-3d-modeling-munir-hamad/)
- [Antigravity + Cloud Code - Vibe Coding · Agentes IA en Acción Legacy](https://www.skool.com/agentes-ia-en-accion-legacy/classroom/fa877fba?md=c9b07090fc8141209539e623db74ff12)
- [Talk to your Google Sheets using ChatGPT-5 \| n8n workflow template](https://n8n.io/workflows/7639-talk-to-your-google-sheets-using-chatgpt-5/)
- [Microsoft account \| Inicio / FORTNITECREW](https://account.microsoft.com/?refd=account.microsoft.com)

**MUEBLES_CARP** (6 bookmarks · construccion)

- [Catálogo completo \| Marketplace Faplac Online](https://www.faplaconline.com.ar/home/c/ar-faplac)
- [EUROHARD](https://euro-hard.com.ar/catalogo)
- [Häfele Argentina - Productos](https://www.hafele.com.ar/es/info/productos/55619/)
- [Diseños Mobiliario e interiorismo \| EGGER](https://www.egger.com/es/mobiliario-e-interiorismo/?country=AR)
- [Piazza \| Grifería Sanitaria](https://piazzagriferia.com/descargas_autocad.html)
- [Piazza \| Grifería Sanitaria](https://www.piazzagriferia.com/?utm_source=google&utm_medium=cpc&utm_campaign=SEARCH+%7C+Piazza+Institucional&utm_content=institucional&gad_source=1&gclid=Cj0KCQiA8q--BhDiARIsAP9tKI1WOB3cUaSGRDBj5j4pqLW1OfCJMqVFaDlku9XyxWjvebxUyO49exsaApUEEALw_wcB)

**ALURA** (6 bookmarks · educacion)

- [Clase 01 \| Alura Cursos Online](https://www.aluracursos.com/inmersion-ia-gemini-y-alura/introduccion-a-gemini-y-sus-capacidades)
- [Clase 02 \| Alura Cursos Online](https://www.aluracursos.com/inmersion-ia-gemini-y-alura/ingenieria-de-prompts-y-aplicaciones-reales)
- [Clase 03 \| Alura Cursos Online](https://www.aluracursos.com/inmersion-ia-gemini-y-alura/gemini-mas-google-workspace-en-la-practica)
- [Inmersión IA [Guía de Jornada]](https://grupoalura.notion.site/Inmersi-n-IA-Gu-a-de-Jornada-24c379bdd09b802cb4adcdf14d2df3a1)
- [(147) Explorando la UI de Gemini #aluramás - YouTube](https://www.youtube.com/watch?v=iKa-vGjYJfk)
- [Inmersión IA [Guía de Jornada]](https://grupoalura.notion.site/Inmersi-n-IA-Gu-a-de-Jornada-24c379bdd09b802cb4adcdf14d2df3a1#24c379bdd09b8049ac39f75535165546)

**#HON** (5 bookmarks · construccion)

- [A-115.pdf](https://mepau.cpau.org/Media/Default/pdf/anexos/A-115.pdf)
- [Te ayudamos a calcular tus honorarios \| CPAU](https://www.cpau.org/nota/33556)
- [C.Urbanístico: charla virtual \| CPAU](https://www.cpau.org/nota/38270)
- [Pin](https://ar.pinterest.com/)
- [ML](https://www.mercadolibre.com.ar/)

**BIM** (5 bookmarks · software arq)

- [Grasshopper Component Index \| Grasshopper Docs](https://grasshopperdocs.com/completeIndex.html)
- [BIM Troublemaker: Ferrari World Abu Dhabi in Revit](https://bimtroublemaker.blogspot.com/2014/11/ferrari-world-abu-dhabi-in-revit.html)
- [Course: Unreal Engine- for Architects and BIM Modelers \| Udemy](https://www.udemy.com/course/unreal-engine-for-architects-and-bim-modelers/learn/lecture/43679538?components=add_to_cart%2Cbase_purchase_section%2Cbuy_button%2Ccacheable_buy_button%2Cdeal_badge%2Cdiscount_expiration%2Cgift_this_course%2Clifetime_access_context%2Cprice_text%2Cpurchase%2Cpurchase_tabs_context%2Crecommendation%2Credeem_coupon%2Cone_click_checkout#overview)
- [Tutorial gratuito sobre ARCHICAD - Introducción al BIM con ArchiCAD \|](https://www.udemy.com/course/introduccion-al-bim-con-archicad/)
- [Cursos en línea: Aprende de todo y a tu propio ritmo \| Udemy](https://www.udemy.com/cart/subscribe/course/5305564/)

**CAD-Bloques3D** (4 bookmarks · software arq)

- [Bibliocad — Bloques AutoCAD Gratis, descarga +120k bloques](https://www.bibliocad.com/)
- [Descarga Bloques DWG Gratis: El Mejor Recurso de Bloques AutoCAD y Blo](https://recursoscad.com/)
- [Bloques dinámicos gratis AutoCAD formato DWG - RecursosCAD](https://recursoscad.com/bloques-dinamicos-gratis-autocad-formato-dwg/)
- [Catálogo Arquitectura \| Productos de Arquitectura, Construcción y BIM](https://www.catalogoarquitectura.cl/cl/)

**ANCAFLEX** (4 bookmarks · construccion)

- [SECO](https://www.anclaflex.com.ar/construccion-en-seco)
- [MASILLAPlus](https://www.anclaflex.com.ar/construccion-en-seco/masilla-plus)
- [PREVIEW_HT_Masilla_Plus_0824](https://www.anclaflex.com.ar/fichas/PREVIEW_HT_Masilla_Plus_0824.pdf)
- [Anclaflex](https://www.anclaflex.com.ar/pinturas-y-enduidos)

**REVEAR** (4 bookmarks · construccion)

- [Productos \| Revear](https://www.revear-apps.com.ar/productos-para-particulares.html)
- [Base para texturados \| Revear](https://www.revear-apps.com.ar/productos-para-particulares/base-para-texturados.html)
- [Revex: Revestimiento Acrílico Texturado Medio](https://arg.sika.com/revear/es/soluciones-revear/revestimientos-texturados/revear-revex-medio.html)
- [Anclaflex](https://www.anclaflex.com.ar/calculadora-resultado)

**WEBER** (4 bookmarks · construccion)

- [FICHAS WEBER basic ceramicos AR](https://www.ar.weber/files/ar/2024-07/12_I_F.P_Weber_basic_ceramicos_-_pdf.pdf)
- [FICHAS WEBER  classic AR](https://www.ar.weber/files/ar/2024-09/F.P_Weber_Pastina_Classic_-18M.pdf)
- [Cerámica San Lorenzo Argentina – Porcelanato, pisos y revestimientos \|](https://ceramicasanlorenzo.com.ar/?roomvoStartVisualizer=true&utm_campaign=626754278332&utm_medium=PaidSocial&utm_source=Pinterest&utm_content=2680083962708&pp=0&epik=dj0yJnU9dEdnSTJLMjZWS2plTlByZjQ1cnc0TzBYaUxOUTQ4X04mcD0xJm49MFNoUDlqd3BJQUhBYTBOSHVZNWVfQSZ0PUFBQUFBR2VkQWZ3)
- [Precio en Argentina de m² de Losa unidireccional con vigas planas, vig](https://argentina.generadordeprecios.info/obra_nueva/calculaprecio.asp?Valor=1|0_2|1|EHU020|ehu_forjado%20vig_p_pref_sop:c9_0_4_0_11c8_0_2_2|hor_p_forjado%20unid:_0_0_0_0_0_1_2_0_0_0_2_1_1_0_5|ehu_cuvo_con_pilares%20forj_pref:_0_0_10000_4000|acero%20forjado_unid:_0_0_0_0_0_0_0_3|mallazo_estructuras:_0_0_1_0_0|enc_ehu_encof_todos:c5_0_10_0_100_0_30_100c4_0_10|hor_curado%20hormigon:_1_0_0_0)

**aldershot** (3 bookmarks · software arq)

- [sergison-bates-el-croquis.pdf](https://www.coam.org/media/Default%20Files/fundacion/biblioteca/donativo%20instituciones%20editoriales/sergison-bates-el-croquis.pdf)
- [Sergison Bates architects](https://sergisonbates.com/en/projects/housing-aldershot)
- [El Croquis 187 - Sergison Bates 2004-2016 \| TOAZ.INFO](https://toaz.info/doc-view-4)

**CAD-Bloques2D** (2 bookmarks · software arq)

- [Saco De Boxeo - Planos CAD](https://planoscadgratis.com/saco-de-boxeo/)
- [Home - Planos CAD](https://planoscadgratis.com/)

**SINTEPLAST** (2 bookmarks · construccion)

- [Sinteplast - Producto](https://www.sinteplast.com.ar/arquitectonica/hidroesmaltes/hidroesmalte-epoxi-pisos-y-paredes)
- [producto-sinteplast-ficha-tecnica-543-20210721161411.pdf](https://www.sinteplast.com.ar/admin/uploaded/fichas-tecnicas/producto-sinteplast-ficha-tecnica-543-20210721161411.pdf)

**IA.RQ** (2 bookmarks · ia)

- [Finch – Optimizing Architecture](https://www.finch3d.com/)
- [Architechtures - IA para Arquitectura. Diseña edificios con IA](https://architechtures.com/es?srsltid=AfmBOopz-Y8vLOLVcfhLTexahGFK4hJOfVHcxmkJjo_t0q_ESP8y_WHQ)

**DURLOCK** (1 bookmarks · construccion)

- [Calculador Durlock® - Calculá tus materiales Durlock online](https://durlock.com/calculador/)

**KEKOL** (1 bookmarks · construccion)

- [K-50 N HTWL.pdf](https://kekol.com.ar/wp-content/uploads/documents/K-50%20N%20HTWL.pdf)

**G#** (1 bookmarks · educacion)

- [Login miBA](https://login.buenosaires.gob.ar/auth/realms/miba/protocol/openid-connect/auth?client_id=tad&response_type=code&scope=profile&redirect_uri=https://tad.buenosaires.gob.ar/tramitesadistancia/miba/ServletLogin)

**AVISO_OBRA** (1 bookmarks · construccion)

- [Unidad Fija (UF) \| Instituto de Estadística y Censos de la Ciudad Autó](https://www.estadisticaciudad.gob.ar/eyc/?page_id=127327)

**A#** (1 bookmarks · educacion)

- [CPAU-Incumbencias](https://static.cpau.org/publicaciones/uya/doc/3_app.pdf)

---
