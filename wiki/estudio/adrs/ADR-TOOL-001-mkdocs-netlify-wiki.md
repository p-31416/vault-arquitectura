---
tipo: adr
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [adr, tool, wiki, mkdocs, netlify, static-site, auth]
estado: aceptado
categoria: tool
numero: 001
---

# ADR-TOOL-001: Wiki Estática con MkDocs Material + Netlify Identity

## Contexto

El estudio necesita publicar su vault Obsidian (`wiki/`, `proyectos/`) como **wiki web privada** accesible para todo el equipo (4-5 personas), con:
- Autenticación obligatoria (login)
- Búsqueda full-text
- Wikilinks `[[...]]` resueltos
- Backlinks, graph view, tags
- Versionado vía Git
- **Costo $0/mes**
- Mantenimiento mínimo

**Restricciones:**
- No hay servidor propio 24/7 para app dinámica
- Equipo no tiene presupuesto SaaS ($8-15/user/mes)
- Contenido sensible (legales, finanzas, playbooks) → **privado obligatorio**
- Fuente de verdad = archivos `.md` en Git (Obsidian-compatible)

## Decisión

**Usar [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) como generador de sitio estático + [Netlify](https://netlify.com) para hosting + [Netlify Identity](https://docs.netlify.com/visitor-access/identity/) para autenticación.**

Pipeline:
```
Obsidian (vault local) → Git push → Netlify build (mkdocs build) → Netlify CDN + Identity widget → Equipo accede con magic link email
```

## Alternativas Consideradas

| Alternativa | Pros | Contras | Por qué no |
|-------------|------|---------|------------|
| **Quartz + Netlify Identity** | Wikilinks/graph view nativos, hecho para Obsidian | **Sin auth nativo** → requiere Cloudflare Workers custom o Netlify Functions complejas | Reinventar auth en static site = deuda técnica |
| **GitHub Pages + Netlify Identity** | Gratis, simple | GitHub Pages no soporta Netlify Identity (solo Netlify) | Requiere mover hosting a Netlify |
| **GitLab Pages + GitLab Auth** | Integrado | Repo en GitHub, migración coste | No vale la pena mover repo |
| **Wiki.js self-hosted** | Auth nativo, wiki real, DB | Requiere VPS/DB, mantenimiento, no static | Viola $0 + no server |
| **Obsidian Publish** | Zero config, wikilinks, graph | **$8/user/mes**, **público o auth básico**, no self-hosted | $40-48/mes = fuera de presupuesto |
| **Notion/Confluence/GitBook** | SaaS completo | Per-seat cost, vendor lock-in, datos fuera | Fuera de presupuesto |

## Consecuencias

### Positivas
- **$0/mes** para siempre (Netlify Identity gratis hasta 1,000 MAU)
- **Auth real**: Magic link email (sin passwords), opcional Google/GitHub OAuth
- **Static site**: CDN global, rápido en Argentina, sin backend que mantener
- **MkDocs Material**: Mejor tema técnico (tabs, admonitions, mermaid, pdf export, git-revision-date, search, i18n)
- **Wikilinks**: Plugin `mkdocs-wikilinks-plugin` resuelve `[[...]]` correctamente
- **Git-backed**: Cada cambio = commit = historia + rollback trivial
- **Netlify Identity Widget**: Embebido en 2 líneas JS, UX decente
- **Preview deploys**: Cada PR genera URL temporal para review

### Negativas / Riesgos / Deuda Técnica
- **No hay graph view interactivo** (Quartz sí lo tiene)
  - *Mitigación*: Backlinks + tags + search cubren 90% navegación; graph es "nice to have"
- **No hay edición web** (solo lectura)
  - *Mitigación*: Edición en Obsidian local → git push → auto-deploy (2 min)
- **Netlify Identity en "maintenance mode"** (no nuevas features)
  - *Mitigación*: Funciona estable; si muere → migrar a Cloudflare Pages + Workers Auth o auth proxy
- **Build time** crece con vault grande (>1000 páginas)
  - *Mitigación*: `mkdocs-minify-plugin`, incremental builds Netlify, dividir vault si necesario
- **Plugins MkDocs ≠ Plugins Obsidian** (Dataview, Tasks, Kanban **no funcionan**)
  - *Mitigación*: Esos son para **PM/dashboards** → van en **Leantime/GitHub Projects** (ADR-INFRA-001), no en wiki

## Trabajo Futuro / Seguimiento
- [ ] Configurar `mkdocs.yml` con plugins: mermaid2, git-revision-date, print-site, wikilinks, minify
- [ ] Conectar repo GitHub → Netlify → Build command: `mkdocs build`, Publish: `site`
- [ ] Activar Netlify Identity → Invitar 5 emails del equipo
- [ ] Añadir widget login en `theme/custom.html` (head)
- [ ] Probar auth en preview deploy y producción
- [ ] Documentar flujo: "Editar en Obsidian → Commit → Push → 2 min → Live"
- [ ] Evaluar Cloudflare Pages + Access si Netlify Identity falla

## Referencias

- Análisis completo: [[analisis-despliegue-wiki-quartz]]
- MkDocs Material: https://squidfunk.github.io/mkdocs-material/
- Netlify Identity: https://docs.netlify.com/visitor-access/identity/
- mkdocs-wikilinks-plugin: https://github.com/johanneswilm/mkdocs-wikilinks-plugin
- ADR relacionado: [ADR-INFRA-001 Leantime Self-Hosted](../ADR-INFRA-001-leantime-selfhosted.md)