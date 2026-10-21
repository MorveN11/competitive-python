# Problemas de años anteriores

Aquí se resuelven, de a poco, los problemas de olimpiadas pasadas. Los problemas del Nivel 2 son **con grader**: se implementa una función y el juez la llama.

## Estructura

```
problems/
├── progreso.md          ← tabla de problemas y su estado
├── nuevo.py             ← crea un problema nuevo desde la plantilla
├── _plantilla/          ← molde (no se edita para resolver)
└── <año>/<problema>/
    ├── enunciado.md     ← texto, restricciones, idea y notas
    ├── solucion.py      ← la función que pide el enunciado
    ├── grader.py        ← grader local para probar
    └── casos/           ← N.in (entrada) y N.out (respuesta esperada)
```

## Flujo para cada problema

1. Crear la carpeta:
   ```
   python problems/nuevo.py 2023 nombre_del_problema
   ```
2. Pegar el enunciado en `enunciado.md` (con restricciones y ejemplos).
3. En `grader.py` poner el nombre de la función en `FUNCION` (como lo pide el enunciado) y escribir esa función en `solucion.py`.
4. Convertir los ejemplos en casos: `casos/1.in` con un argumento por línea (literales de Python) y `casos/1.out` con la respuesta.
5. Probar:
   ```
   python problems/2023/nombre_del_problema/grader.py
   ```
   o en VS Code: `Ctrl+Shift+P` → `Tasks: Run Task` → **Probar problema (grader)** con `solucion.py` o `grader.py` abierto.
6. Agregar casos extremos (mínimo, máximo, vacío, todo igual) y volver a probar.
7. Anotar en `enunciado.md` qué aprendimos, y actualizar `progreso.md`.

## Ejemplo de caso

Para una función `resolver(arr, k)`:

`casos/1.in`
```
[3, 1, 4, 1, 5]
2
```

`casos/1.out`
```
True
```

El grader lee cada línea como un literal de Python (`ast.literal_eval`), llama `resolver(*argumentos)` y compara `str(resultado)` con `.out`.

## Depurar

En `solucion.py` puedes usar `dbg(...)` (la misma función del debugger del repositorio). El grader local la carga automáticamente y muestra los mensajes por la consola. En el juez `dbg` no existe y el archivo ya trae una definición vacía, así que se puede enviar sin quitarlos.

## Al enviar al juez

- Sube solo la función (y lo que necesite). Sin `input()` ni `print()`.
- La firma debe ser **idéntica** a la del enunciado.
- Revisa la lista de `study/hoja_de_trucos.md`.

## Importante: el grader local es una aproximación

El grader real del juez (CMS) puede tener otros nombres, tipos o forma de llamar a la función. Cuando agreguen el primer problema real, comparen con el archivo de ejemplo del enunciado y ajusten `grader.py` y `_plantilla/` para que se parezcan.

La carpeta `_plantilla/` es el molde: no escribas soluciones ahí.
