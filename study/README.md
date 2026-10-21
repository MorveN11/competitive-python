# Material de estudio: Nivel 2 (Algoritmos)

Material para preparar la competencia **Nivel 2: Algoritmos**, a partir de la introducción de `course/`.

## Sobre la competencia

- **Para quién:** estudiantes de 5.º de primaria a 3.º de secundaria con conocimientos básicos de programación.
- **Se evalúa:** razonamiento lógico, uso correcto del lenguaje y capacidad de escribir algoritmos claros y estructurados.
- **Lenguajes:** C++17, C++20 o Python 3.11, en el juez CMS.
- **Formato:** todos los problemas son **con grader**: se implementa una función y el juez la llama.

## Temario → cuaderno

| # | Tópico | Cuaderno |
|---|---|---|
| 00 | Cómo funciona el grader, Python para quien viene de C++, complejidad, checklist | [00_el_juez_y_python](00_el_juez_y_python.ipynb) |
| 01 | Estructuras de control, funciones y arreglos (incluso multidimensionales) | [01_control_funciones_arreglos](01_control_funciones_arreglos.ipynb) |
| 02 | Números: divisibilidad, primos, MCD y mcm, aritmética modular | [02_numeros](02_numeros.ipynb) |
| 03 | Cadenas: recorridos, palíndromos y búsqueda de patrones | [03_cadenas](03_cadenas.ipynb) |
| 04 | Técnicas sobre arreglos: sumas de prefijos, dos punteros y ventana deslizante | [04_tecnicas_arreglos](04_tecnicas_arreglos.ipynb) |
| 05 | Simulación y búsqueda completa: matrices, subconjuntos y permutaciones | [05_simulacion_busqueda_completa](05_simulacion_busqueda_completa.ipynb) |
| 06 | Búsqueda binaria, ordenamiento, golosos, pilas, colas, conjuntos y mapas | [06_estructuras_y_algoritmos](06_estructuras_y_algoritmos.ipynb) |

Resumen de una página: [hoja_de_trucos.md](hoja_de_trucos.md).

## Cómo usar el material

1. Lee el cuaderno y ejecuta las celdas. Casi todas terminan en `assert`: si no hay error, el código es correcto.
2. Cambia los ejemplos, rómpelos y arréglalos.
3. Resuelve la sección **Para practicar** de cada cuaderno antes de pasar al siguiente tema.
4. Crea un problema real en `problems/` y resuélvelo con el grader local (ver `problems/README.md`).

Los cuadernos asumen que ya hiciste el curso `course/` (sobre todo las lecciones 5 a 8). Si algo no se entiende, vuelve a la lección correspondiente.

## Orden sugerido

| Sesión | Contenido |
|---|---|
| 1 | 00 + 01 |
| 2 | 02 |
| 3 | 03 |
| 4 | 04 |
| 5 | 05 |
| 6 | 06 (ordenamiento, búsqueda binaria, golosos) |
| 7 | 06 (pilas, colas, conjuntos y mapas) |
| 8+ | problemas de años anteriores (`problems/`) |

Cada tema tiene problemas tipo para resolver **antes** de pasar a los problemas reales.

## Qué falta (pendiente)

El detalle exacto del grader del juez (nombres de módulos, firma de las funciones, formato de los tipos) depende del enunciado real. Cuando se agregue el primer problema real, hay que revisar que `problems/_plantilla/grader.py` se parezca al del juez.
