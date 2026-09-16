---
tipo: manifiesto
fecha_creacion: 2026-06-30
tags: [filosofia, framework, dibujo-ia, manifiesto]
---

# Manifiesto del Framework de Dibujo Asistido por IA

> **`filo`** marca el principio y el fin del *por qué*. Es el archivo global del MVP, no por nivel. Cada nivel demuestra este manifiesto a través de su `spec`.

## Origen

Este framework nace de una convicción: **la importancia de documentar los procesos**. Arrancamos en AutoCAD porque 10 años de práctica docente me habilitan a pensar más rápido y mejor ahí. Conozco sus límites, sus atajos, su lógica. Pero la filosofía más que pertenecer a AutoCAD — es de **cómo pienso y dibujo arquitectura**. El objetivo final es que esta forma de trabajar se convierta en una **metodología** replicable en cualquier herramienta BIM, RHINO, GRASSHOPPER,BLENDER,COMFYUI, etc..
uno tiene un set de herramientas potenciadas con IA que usa si quiere documentar archivos, planos, imagenes, videos, tiene a disposición herramientas a medida. según necesidad del usuario. (niveles de acceso, proteccion de la información sensible,filtrado de imagenes)

## Principio rector

> Lograr lo que necesito con el **menor esfuerzo posible**, usando **lenguaje natural** como interfaz principal. primero apunto al metahuman-101 que sería que me simplifique el dibujar a mano, y siempre pensandolo escalable a que despues lo pueda entender la maquina en lenguaje natural

Cada línea de código AutoLISP, cada especificación en el vault (van los procesos de MVP terminados, recien cuando se termina ingresa al vault-debería poder compartir en el futurio unicamente el Vault y NO la información en proceso), cada nivel de progresión existe para reducir la fricción entre **lo que pienso** y **lo que aparece en pantalla**.

## Qué aporta al estudio

No se trata de reemplazar AutoCAD ni de competir con herramientas existentes. Se trata de **capturar el know-how constructivo del estudio en código ejecutable por IA**, formando una biblioteca viva de decisiones de dibujo que:

- Documenta **cómo dibuja este estudio** (convenciones, tolerancias, defaults)
- Permite **progresión natural**: de lo simple (una línea) a lo complejo (una planta completa)
- Es **revisable por humanos** antes de ejecutarse (el spec primero, el ft después)
- Genera **scripts AutoLISP** que se cargan directamente en AutoCAD
- Se traslada a Revit con los mismos principios
- Evoluciona hacia **MCP server** cuando la lógica madure

## Principios

1. **Primero spec, después ft, después código** — cada nivel se diseña en .md antes de escribir .lsp
2. **Defaults opinados** — el estudio define valores por defecto (muro 0.15m, puertas 0.80m, apertura interior) que reflejan su práctica
3. **Jerarquía de niveles** — cada nivel incorpora el anterior y añade complejidad
4. **Documentación viva** — el .md es el source of truth; el .lsp es la implementación
5. **Software-agnóstico en espíritu** — la metodología trasciende AutoCAD; Revit es el siguiente destino

## Lo que NO es esto

- ❌ No es un competidor de AutoCAD ni Revit
- ❌ No es un plugin comercial
- ❌ No es un reemplazo del criterio arquitectónico
- ✅ Es una **biblioteca viva de decisiones de dibujo** del estudio
- ✅ Es un **traductor** entre lenguaje natural y geometría construible
- ✅ Es un **registro** de cómo dibujamos, para que la IA aprenda a dibujar como nosotros

## Hoja de ruta

1. **AutoCAD** — donde validamos la lógica constructiva y de dibujo
2. **Revit** — la misma filosofía, trasladada a un entorno BIM
3. **Metodología** — el framework se convierte en una forma de trabajar, independiente del software

## La progresión como filosofía

No se salta de 0 a 100. Cada nivel:
- Incorpora el anterior
- Añade una capa de complejidad real
- Se prueba en obra/plano real antes de avanzar
- Se documenta en .md antes de escribir .lsp

Esto asegura que el framework **crece con el estudio**, no al revés.

## Sobre el MCP (futuro)

El MCP server no es un fin en sí mismo. Es la envoltura que permite que la IA converse con AutoCAD (y después con Revit, comfyuiMCP, etc.), dándole la capacidad de ejecutar comandos, leer datos y modificar dibujos en tiempo real. Cuando la lógica AutoLISP esté madura, el MCP la vuelve accesible desde lenguaje natural puro. en antigravity puedo seleccionar el MCP que quiero trabajar sin salir del entorno y siempre con la misma metodología de trabajo detrás
