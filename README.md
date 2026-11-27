# S.A.M. - Sistema Pedagógico de Asistencia Tecnológica

Copiloto pedagógico interactivo a nivel de sistema operativo móvil diseñado para reducir la brecha digital mediante **andamiaje visual** y **Edge Computing** bajo el principio de *Privacidad por Diseño*.

## Arquitectura del Repositorio

* **`/backend`**: Motor de inferencia y visión por computadora desarrollado en Python (**FastAPI** + **OpenCV**) para el análisis espacial y cálculo de coordenadas $(X, Y)$ en red local.

* **`/android`**: Cliente nativo basado en `AccessibilityService` y `WindowManager` para lectura de jerarquía UI y superposición de guías visuales no bloqueantes.

* **`/docs`**: Especificación de Requerimientos de Software (SRS), diagramas UML y documentación de validación conceptual.
