# Curso introductorio: Python y programación competitiva

Curso para principiantes (pensado para niños de 10 a 14 años, sin experiencia previa). Son 14 cuadernos (`.ipynb`) con explicaciones, código que se ejecuta ahí mismo, ejercicios y retos.

Objetivo: que pierdan el miedo, se diviertan y terminen sabiendo usar el template del repositorio para resolver problemas por su cuenta.

## Índice

| # | Cuaderno | Qué aprenden |
|---|---|---|
| 1 | [Tu primer programa](01_primer_programa.ipynb) | `print`, comentarios, errores |
| 2 | [Variables](02_variables.ipynb) | variables, tipos, `input`, f-strings |
| 3 | [Operadores](03_operadores.ipynb) | `//`, `%`, `**`, par/impar, dígitos |
| 4 | [Condicionales](04_condicionales.ipynb) | `if`, `elif`, `else`, `and`/`or`/`not` |
| 5 | [Bucles](05_bucles.ipynb) | `for`, `range`, `while`, acumuladores |
| 6 | [Listas](06_listas.ipynb) | listas, slices, matrices, comprensión |
| 7 | [Textos, sets y dicts](07_texto_sets_dicts.ipynb) | strings, tuplas, `set`, `dict`, contar |
| 8 | [Funciones](08_funciones.ipynb) | `def`, `return`, recursión |
| 9 | [¿Qué es la programación competitiva?](09_que_es_cp.ipynb) | problemas, veredictos AC/WA/TLE/RE |
| 10 | [Entrada y salida](10_entrada_salida.ipynb) | recetas para leer datos y mostrar la salida |
| 11 | [Pensar y rapidez](11_pensar_y_rapidez.ipynb) | método de 6 pasos, complejidad, `set` vs lista |
| 12 | [Problemas guiados I](12_problemas_I.ipynb) | 6 problemas sencillos resueltos paso a paso |
| 13 | [Problemas guiados II](13_problemas_II.ipynb) | 6 problemas con textos, `set`, `dict`, matrices |
| 14 | [El template](14_el_template.ipynb) | cómo usar el template y el debugger |

Módulos: **Python** (1-8), **intro a CP** (9-11), **problemas sencillos** (12-13), **el template** (14).

## Cómo abrir los cuadernos

1. Instala [Python 3.9 o superior](https://www.python.org/downloads/).
2. Instala [VS Code](https://code.visualstudio.com/) y las extensiones **Python** y **Jupyter** (VS Code las recomienda al abrir la carpeta).
3. Instala el paquete que ejecuta los cuadernos (una sola vez):
   ```
   python -m pip install ipykernel
   ```
4. Abre la carpeta `cp-python` en VS Code (File → Open Folder).
5. Abre un cuaderno de `course/`. Arriba a la derecha, pulsa **Select Kernel** y elige tu Python.
6. Ejecuta una celda con **Shift + Enter**.

Este es el único paquete externo, y solo se usa para los cuadernos. Las soluciones del repositorio (`*.py`) usan solo la librería estándar.

## Cómo trabajar cada lección

1. Lee la explicación y ejecuta cada celda. Cambia el código y vuelve a ejecutar.
2. Haz la sección **🎯 Tu turno** antes de pasar a la siguiente lección.
3. En las lecciones 12 y 13, intenta el problema **antes** de mirar la solución.
4. Las respuestas están en bloques desplegables (`Respuestas` o `Soluciones`).

## Sugerencia de ritmo

- Una lección por sesión de 60 a 90 minutos.
- Lección 14 y primeros problemas del repositorio: una sesión completa, con acompañamiento.
- Cuando terminen la 14, pasan a resolver problemas reales con el template (`cp` + Tab).

## Notas para quien enseña

- Los cuadernos se entregan sin salidas guardadas, así que los alumnos ven el resultado al ejecutar.
- Si un alumno rompe un cuaderno, restáuralo desde git.
- Antes de hacer commit de un cuaderno que ejecutaste, borra las salidas (menú `Clear All Outputs`) para mantener limpio el repositorio.
- Las lecciones 10, 12 y 13 definen la función `con_entrada`, que simula `data/input.txt`. Hay que ejecutar su primera celda antes que las demás.
- Todas las celdas de código se ejecutaron de principio a fin sin errores al preparar el curso (con Python 3.12). Las celdas con `input()` piden datos al ejecutarse.

## Problemas comunes

| Síntoma | Solución |
|---|---|
| No aparece el botón de ejecutar | Falta la extensión **Jupyter**. |
| "Select Kernel" no lista Python | Instala `ipykernel` (paso 3) y reinicia VS Code. |
| `NameError: name 'con_entrada' is not defined` | Ejecuta primero la celda que define `con_entrada`. |
| La celda con `input()` parece colgada | Espera el cuadro de texto en la parte superior de VS Code y escribe ahí. |
| `FileNotFoundError` en la lección 14 | Abre la carpeta `cp-python` como raíz; los cuadernos buscan `../lib/`. |
