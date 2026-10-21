---
tipo: indice
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [indice, pdf, raw, fuentes, hitl]
---

# raw/pdf — Crudo de PDFs, fichas de extracción y transcripciones

> Espejo de [[raw/yt/00-index|raw/yt]] para documentos. Cada PDF deja **dos archivos**: una ficha (metadata, índice, stats, figuras con página) y la transcripción completa (texto por página, con marcadores `## [p. N]`).
> Texto completo con copyright: queda en `raw/` (zona de trabajo interna, con aviso de uso) y **no se redistribuye**. A la wiki entran extractos breves con atribución (fair use), vía @contenidos. Los binarios viven en `activos/fuentes/` (gitignored).

## Estructura

```
raw/pdf/
├── 00-index.md                              ← este archivo
├── YYYY-MM-DD-<slug>-ficha.md               ← metadata + TOC + stats + figuras
└── YYYY-MM-DD-<slug>-transcripcion.md       ← texto completo, página por página
```

## Reglas

- Binario original → `activos/fuentes/<slug>/` (gitignored, no entra a git). El `.md` solo referencia ruta.
- **Imágenes: no se extraen** (decisión 2026-10-20). La ficha lista los pies de figura con su página y remite al PDF.
- Texto completo → `raw/pdf/*-transcripcion.md` (decisión 2026-10-20: versionado, con aviso de copyright en el frontmatter).
- Extracción: **Ghostscript `txtwrite` página por página** (acentos correctos + abre el PDF cifrado AES); `pypdf` para metadata y marcadores; **OCR tesseract** solo si la cobertura de texto < 40 %.
- Reporte legible siempre en `raw/contenidos/` vía @contenidos. A `wiki/fuentes` solo con tu `s`.
- Los PDF de origen (`G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography`) se abren **en solo lectura**: nunca se modifican.

## Fichas

| Fecha | PDF | Págs | Palabras | Texto | Figuras | Transcripción | Ficha | Binario | Estado |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-20 | 0. INDEX | 7 | 913 | 100% | 0 | [[raw/pdf/2026-10-20-0_index-transcripcion\|2026-10-20-0_index-transcripcion]] | [[raw/pdf/2026-10-20-0_index-ficha\|2026-10-20-0_index-ficha]] | `activos/fuentes/0_index/0. INDEX.pdf` | texto-extraible |
| 2026-10-20 | An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design | 203 | 45223 | 93% | 2 | [[raw/pdf/2026-10-20-an_exploration_into_biomimicry_and_its_application_into_digi-transcripcion\|2026-10-20-an_exploration_into_biomimicry_and_its_application_into_digi-transcripcion]] | [[raw/pdf/2026-10-20-an_exploration_into_biomimicry_and_its_application_into_digi-ficha\|2026-10-20-an_exploration_into_biomimicry_and_its_application_into_digi-ficha]] | `activos/fuentes/an_exploration_into_biomimicry_and_its_application_into_digi/An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design .pdf` | texto-extraible |
| 2026-10-20 | Antoni Gaudí and Frei Otto: Essential Precursors to the Parametricism Manifesto | 6 | 2110 | 100% | 0 | [[raw/pdf/2026-10-20-burry_m_antoni_gaudi_and_frei_otto_essential_precursors_to_t-transcripcion\|2026-10-20-burry_m_antoni_gaudi_and_frei_otto_essential_precursors_to_t-transcripcion]] | [[raw/pdf/2026-10-20-burry_m_antoni_gaudi_and_frei_otto_essential_precursors_to_t-ficha\|2026-10-20-burry_m_antoni_gaudi_and_frei_otto_essential_precursors_to_t-ficha]] | `activos/fuentes/burry_m_antoni_gaudi_and_frei_otto_essential_precursors_to_t/BURRY, M.-Antoni Gaudi and Frei Otto-Essential-precursors-to-the-Parametricism-Manifesto.pdf` | texto-extraible |
| 2026-10-20 | Antonio Gaudi Precursor de la Sostenibilidad en la Arquitectura CARLOS_JOSE_SALAS_MIRAT | 396 | 79374 | 97% | 0 | [[raw/pdf/2026-10-20-antonio_gaudi_precursor_de_la_sostenibilidad_en_la_arquitect-transcripcion\|2026-10-20-antonio_gaudi_precursor_de_la_sostenibilidad_en_la_arquitect-transcripcion]] | [[raw/pdf/2026-10-20-antonio_gaudi_precursor_de_la_sostenibilidad_en_la_arquitect-ficha\|2026-10-20-antonio_gaudi_precursor_de_la_sostenibilidad_en_la_arquitect-ficha]] | `activos/fuentes/antonio_gaudi_precursor_de_la_sostenibilidad_en_la_arquitect/Antonio Gaudi Precursor de la Sostenibilidad en la Arquitectura CARLOS_JOSE_SALAS_MIRAT.pdf` | texto-extraible |
| 2026-10-20 | Anuario1923 | 21 | 6680 | 100% | 0 | [[raw/pdf/2026-10-20-anuario1923-transcripcion\|2026-10-20-anuario1923-transcripcion]] | [[raw/pdf/2026-10-20-anuario1923-ficha\|2026-10-20-anuario1923-ficha]] | `activos/fuentes/anuario1923/Anuario1923.pdf` | texto-extraible |
| 2026-10-20 | Back to the Basics Return to the Origin, Gaudí and Nature | 14 | 5821 | 100% | 13 | [[raw/pdf/2026-10-20-back_to_the_basics_return_to_the_origin_gaudi_and_nature-transcripcion\|2026-10-20-back_to_the_basics_return_to_the_origin_gaudi_and_nature-transcripcion]] | [[raw/pdf/2026-10-20-back_to_the_basics_return_to_the_origin_gaudi_and_nature-ficha\|2026-10-20-back_to_the_basics_return_to_the_origin_gaudi_and_nature-ficha]] | `activos/fuentes/back_to_the_basics_return_to_the_origin_gaudi_and_nature/Back to the Basics Return to the Origin, Gaudí and Nature.pdf` | texto-extraible |
| 2026-10-13 | Baudrillard 1994 Simulacra and Simulation (prueba de extracción) | 108 | 57294 | 100% | 1 | — | [[raw/pdf/2026-10-13-baudrillard-1994-ficha\|2026-10-13-baudrillard-1994-ficha]] | `activos/fuentes/baudrillard-1994/Jean_baudrillard-simulacra-and-simulation.pdf` | — |
| 2026-10-20 | Between Designer and Design: Parametric Design and Prototyping Considerations on Gaudí’s Sagrada Familia | 5 | 3154 | 100% | 3 | [[raw/pdf/2026-10-20-between_designer_and_design-transcripcion\|2026-10-20-between_designer_and_design-transcripcion]] | [[raw/pdf/2026-10-20-between_designer_and_design-ficha\|2026-10-20-between_designer_and_design-ficha]] | `activos/fuentes/between_designer_and_design/Between Designer and Design.pdf` | texto-extraible |
| 2026-10-20 | Beyond Aesthetics: Antoni Gaudí's Revolutionary Use of Biomimicry, Biomorphism, and Biosynchronization in Architectural Design | 92 | 19709 | 98% | 98 | [[raw/pdf/2026-10-20-sung_y_beyond_aesthetics_antoni_gaudis_revolutionary_use_of_-transcripcion\|2026-10-20-sung_y_beyond_aesthetics_antoni_gaudis_revolutionary_use_of_-transcripcion]] | [[raw/pdf/2026-10-20-sung_y_beyond_aesthetics_antoni_gaudis_revolutionary_use_of_-ficha\|2026-10-20-sung_y_beyond_aesthetics_antoni_gaudis_revolutionary_use_of_-ficha]] | `activos/fuentes/sung_y_beyond_aesthetics_antoni_gaudis_revolutionary_use_of_/SUNG, Y. - Beyond Aesthetics_ Antoni Gaudís Revolutionary Use of Biomimicry.pdf` | texto-extraible |
| 2026-10-20 | Bio-Inspired Design Approach Analysis: A Case Study of Antoni Gaudi and Santiago Calatrava | 7 | 3626 | 100% | 0 | [[raw/pdf/2026-10-20-bio_insipred_design_approach_analysis-transcripcion\|2026-10-20-bio_insipred_design_approach_analysis-transcripcion]] | [[raw/pdf/2026-10-20-bio_insipred_design_approach_analysis-ficha\|2026-10-20-bio_insipred_design_approach_analysis-ficha]] | `activos/fuentes/bio_insipred_design_approach_analysis/Bio Insipred Design Approach Analysis.pdf` | texto-extraible |
| 2026-10-20 | Challenges in teaching architectural morphogenesis | 16 | 593 | 94% | 0 | [[raw/pdf/2026-10-20-challenges_in_teaching_architectural_morphogenesis-transcripcion\|2026-10-20-challenges_in_teaching_architectural_morphogenesis-transcripcion]] | [[raw/pdf/2026-10-20-challenges_in_teaching_architectural_morphogenesis-ficha\|2026-10-20-challenges_in_teaching_architectural_morphogenesis-ficha]] | `activos/fuentes/challenges_in_teaching_architectural_morphogenesis/Challenges in teaching architectural morphogenesis.pdf` | texto-extraible |
| 2026-10-20 | Dynamical structural modeling A collaborative design exploration | 16 | 3746 | 94% | 1 | [[raw/pdf/2026-10-20-dynamical_structural_modelling-transcripcion\|2026-10-20-dynamical_structural_modelling-transcripcion]] | [[raw/pdf/2026-10-20-dynamical_structural_modelling-ficha\|2026-10-20-dynamical_structural_modelling-ficha]] | `activos/fuentes/dynamical_structural_modelling/Dynamical structural modelling.pdf` | texto-extraible |
| 2026-10-20 | el park guell i els seus origens 1894 1926 | 123 | 98708 | 96% | 0 | [[raw/pdf/2026-10-20-el_park_guell_i_els_seus_origens_1894_1926-transcripcion\|2026-10-20-el_park_guell_i_els_seus_origens_1894_1926-transcripcion]] | [[raw/pdf/2026-10-20-el_park_guell_i_els_seus_origens_1894_1926-ficha\|2026-10-20-el_park_guell_i_els_seus_origens_1894_1926-ficha]] | `activos/fuentes/el_park_guell_i_els_seus_origens_1894_1926/El Park Güell i els seus orígens, 1894-1926.pdf` | texto-extraible |
| 2026-10-20 | gaudi and cad | 10 | 5512 | 100% | 10 | [[raw/pdf/2026-10-20-gaudi_and_cad-transcripcion\|2026-10-20-gaudi_and_cad-transcripcion]] | [[raw/pdf/2026-10-20-gaudi_and_cad-ficha\|2026-10-20-gaudi_and_cad-ficha]] | `activos/fuentes/gaudi_and_cad/Gaudi_and_CAD.pdf` | texto-extraible |
| 2026-10-20 | gaudi morphogenesis pdf | 49 | 16078 | 96% | 0 | [[raw/pdf/2026-10-20-gaudi_morphogenesis_pdf-transcripcion\|2026-10-20-gaudi_morphogenesis_pdf-transcripcion]] | [[raw/pdf/2026-10-20-gaudi_morphogenesis_pdf-ficha\|2026-10-20-gaudi_morphogenesis_pdf-ficha]] | `activos/fuentes/gaudi_morphogenesis_pdf/Gaudi_Morphogenesis_pdf.pdf` | texto-extraible |
| 2026-10-20 | gaudi s approach to building | 10 | 4978 | 100% | 13 | [[raw/pdf/2026-10-20-gaudi_s_approach_to_building-transcripcion\|2026-10-20-gaudi_s_approach_to_building-transcripcion]] | [[raw/pdf/2026-10-20-gaudi_s_approach_to_building-ficha\|2026-10-20-gaudi_s_approach_to_building-ficha]] | `activos/fuentes/gaudi_s_approach_to_building/Gaudí_s approach to building.pdf` | texto-extraible |
| 2026-10-20 | gaudi und natur | 8 | 4739 | 100% | 0 | [[raw/pdf/2026-10-20-gaudi_und_natur-transcripcion\|2026-10-20-gaudi_und_natur-transcripcion]] | [[raw/pdf/2026-10-20-gaudi_und_natur-ficha\|2026-10-20-gaudi_und_natur-ficha]] | `activos/fuentes/gaudi_und_natur/Gaudi_und_Natur.pdf` | texto-extraible |
| 2026-10-20 | Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century | 8 | 3882 | 100% | 6 | [[raw/pdf/2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-transcripcion\|2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-transcripcion]] | [[raw/pdf/2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-ficha\|2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-ficha]] | `activos/fuentes/gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg/Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century.pdf` | texto-extraible |
| 2026-10-20 | huerta s the mechanics of timbrel vaults a historical outlin | 2 | 780 | 100% | 1 | [[raw/pdf/2026-10-20-huerta_s_the_mechanics_of_timbrel_vaults_a_historical_outlin-transcripcion\|2026-10-20-huerta_s_the_mechanics_of_timbrel_vaults_a_historical_outlin-transcripcion]] | [[raw/pdf/2026-10-20-huerta_s_the_mechanics_of_timbrel_vaults_a_historical_outlin-ficha\|2026-10-20-huerta_s_the_mechanics_of_timbrel_vaults_a_historical_outlin-ficha]] | `activos/fuentes/huerta_s_the_mechanics_of_timbrel_vaults_a_historical_outlin/HUERTA, S.-The mechanics of timbrel vaults. a historical outline.pdf` | texto-extraible |
| 2026-10-20 | La arquitectura escultórica de Antonio Gaudí | 6 | 2777 | 100% | 5 | [[raw/pdf/2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-transcripcion\|2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-transcripcion]] | [[raw/pdf/2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-ficha\|2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-ficha]] | `activos/fuentes/la_arquitectura_escultorica_de_antonio_gaudi/LA ARQUITECTURA ESCULTORICA DE ANTONIO GAUDI.pdf` | texto-extraible |
| 2026-10-20 | La arquitectura y la naturaleza compleja | 218 | 77466 | 96% | 0 | [[raw/pdf/2026-10-20-la_arquitectura_y_la_naturaleza_compleja-transcripcion\|2026-10-20-la_arquitectura_y_la_naturaleza_compleja-transcripcion]] | [[raw/pdf/2026-10-20-la_arquitectura_y_la_naturaleza_compleja-ficha\|2026-10-20-la_arquitectura_y_la_naturaleza_compleja-ficha]] | `activos/fuentes/la_arquitectura_y_la_naturaleza_compleja/La arquitectura y la naturaleza compleja.pdf` | texto-extraible |
| 2026-10-20 | Linking Hanging Chain Models to Fabrication | 17 | 5775 | 100% | 14 | [[raw/pdf/2026-10-20-linking_hanging_chain_models_to_fabrication-transcripcion\|2026-10-20-linking_hanging_chain_models_to_fabrication-transcripcion]] | [[raw/pdf/2026-10-20-linking_hanging_chain_models_to_fabrication-ficha\|2026-10-20-linking_hanging_chain_models_to_fabrication-ficha]] | `activos/fuentes/linking_hanging_chain_models_to_fabrication/Linking Hanging Chain Models to Fabrication.pdf` | texto-extraible |
| 2026-10-20 | lopez 2018 ijah the combination of tile vaults with reinforc | 18 | 8506 | 100% | 19 | [[raw/pdf/2026-10-20-lopez_2018_ijah_the_combination_of_tile_vaults_with_reinforc-transcripcion\|2026-10-20-lopez_2018_ijah_the_combination_of_tile_vaults_with_reinforc-transcripcion]] | [[raw/pdf/2026-10-20-lopez_2018_ijah_the_combination_of_tile_vaults_with_reinforc-ficha\|2026-10-20-lopez_2018_ijah_the_combination_of_tile_vaults_with_reinforc-ficha]] | `activos/fuentes/lopez_2018_ijah_the_combination_of_tile_vaults_with_reinforc/LOPEZ_2018_IJAH_the-combination-of-tile-vaults-with-reinforcement-and-concrete_1528446178.pdf` | texto-extraible |
| 2026-10-20 | Matching nature with ‘Complex Geometry’ | 10 | 3847 | 100% | 5 | [[raw/pdf/2026-10-20-matching_nature_with_complex_geometry-transcripcion\|2026-10-20-matching_nature_with_complex_geometry-transcripcion]] | [[raw/pdf/2026-10-20-matching_nature_with_complex_geometry-ficha\|2026-10-20-matching_nature_with_complex_geometry-ficha]] | `activos/fuentes/matching_nature_with_complex_geometry/Matching nature with ‘Complex Geometry’.pdf` | texto-extraible |
| 2026-10-20 | morphogenesis | 29 | 6079 | 0% | 0 | [[raw/pdf/2026-10-20-morphogenesis-transcripcion\|2026-10-20-morphogenesis-transcripcion]] | [[raw/pdf/2026-10-20-morphogenesis-ficha\|2026-10-20-morphogenesis-ficha]] | `activos/fuentes/morphogenesis/Morphogenesis.pdf` | requiere-ocr |
| 2026-10-20 | READING GAUDÍ’S GREAT BOOK OF NATURE | 33 | 8707 | 94% | 8 | [[raw/pdf/2026-10-20-reading_gaudi_s_great_book_of_nature-transcripcion\|2026-10-20-reading_gaudi_s_great_book_of_nature-transcripcion]] | [[raw/pdf/2026-10-20-reading_gaudi_s_great_book_of_nature-ficha\|2026-10-20-reading_gaudi_s_great_book_of_nature-ficha]] | `activos/fuentes/reading_gaudi_s_great_book_of_nature/READING GAUDÍ’S GREAT BOOK OF NATURE.pdf` | texto-extraible |
| 2026-10-20 | Structural Analysis of Historical Constructions | 42 | 13069 | 93% | 30 | [[raw/pdf/2026-10-20-structural_analysis_of_masonry_historical_constructions_clas-transcripcion\|2026-10-20-structural_analysis_of_masonry_historical_constructions_clas-transcripcion]] | [[raw/pdf/2026-10-20-structural_analysis_of_masonry_historical_constructions_clas-ficha\|2026-10-20-structural_analysis_of_masonry_historical_constructions_clas-ficha]] | `activos/fuentes/structural_analysis_of_masonry_historical_constructions_clas/Structural Analysis of Masonry Historical Constructions. Classical and Advanced Approaches.pdf` | texto-extraible |
| 2026-10-20 | structural design in the work of gaudi | 16 | 7673 | 94% | 13 | [[raw/pdf/2026-10-20-structural_design_in_the_work_of_gaudi-transcripcion\|2026-10-20-structural_design_in_the_work_of_gaudi-transcripcion]] | [[raw/pdf/2026-10-20-structural_design_in_the_work_of_gaudi-ficha\|2026-10-20-structural_design_in_the_work_of_gaudi-ficha]] | `activos/fuentes/structural_design_in_the_work_of_gaudi/Structural Design in the Work of Gaudi.pdf` | texto-extraible |
| 2026-10-20 | tomlow j gaudi s reluctant attitude towa | 15 | 6866 | 0% | 23 | [[raw/pdf/2026-10-20-tomlow_j_gaudi_s_reluctant_attitude_towa-transcripcion\|2026-10-20-tomlow_j_gaudi_s_reluctant_attitude_towa-transcripcion]] | [[raw/pdf/2026-10-20-tomlow_j_gaudi_s_reluctant_attitude_towa-ficha\|2026-10-20-tomlow_j_gaudi_s_reluctant_attitude_towa-ficha]] | `activos/fuentes/tomlow_j_gaudi_s_reluctant_attitude_towa/Tomlow_J_Gaudi_s_reluctant_attitude_towa.pdf` | requiere-ocr |
| 2026-10-20 | Towards Morphogenesis in Architecture | 30 | 9566 | 97% | 4 | [[raw/pdf/2026-10-20-towards_morphogenesis_in_architecture-transcripcion\|2026-10-20-towards_morphogenesis_in_architecture-transcripcion]] | [[raw/pdf/2026-10-20-towards_morphogenesis_in_architecture-ficha\|2026-10-20-towards_morphogenesis_in_architecture-ficha]] | `activos/fuentes/towards_morphogenesis_in_architecture/Towards Morphogenesis in Architecture.pdf` | texto-extraible |
| 2026-10-20 | tree inspired dendriforms and fractal like | 26 | 12176 | 100% | 31 | [[raw/pdf/2026-10-20-tree_inspired_dendriforms_and_fractal_like-transcripcion\|2026-10-20-tree_inspired_dendriforms_and_fractal_like-transcripcion]] | [[raw/pdf/2026-10-20-tree_inspired_dendriforms_and_fractal_like-ficha\|2026-10-20-tree_inspired_dendriforms_and_fractal_like-ficha]] | `activos/fuentes/tree_inspired_dendriforms_and_fractal_like/Tree-inspired dendriforms and fractal-like.pdf` | texto-extraible |
| 2026-10-20 | using nature in architecture a perspecti | 5 | 2685 | 100% | 6 | [[raw/pdf/2026-10-20-using_nature_in_architecture_a_perspecti-transcripcion\|2026-10-20-using_nature_in_architecture_a_perspecti-transcripcion]] | [[raw/pdf/2026-10-20-using_nature_in_architecture_a_perspecti-ficha\|2026-10-20-using_nature_in_architecture_a_perspecti-ficha]] | `activos/fuentes/using_nature_in_architecture_a_perspecti/Using_Nature_in_Architecture_A_perspecti.pdf` | texto-extraible |





















































































































> `2026-10-19-gaudi_and_cad-ficha.md` quedó sustituida por la re-extracción v2 del 2026-10-20 (mismo PDF, ahora con transcripción y figuras). Baudrillard mantiene su ficha v1: pendiente de re-extracción con el extractor nuevo.
