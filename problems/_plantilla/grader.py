"""Grader local: llama a tu función con cada caso de casos/ y compara con la salida esperada.

Uso: python grader.py   (o la tarea "Probar problema (grader)" de VS Code)

Formato de casos/:
    N.in   un argumento por línea, escrito como literal de Python (10, "hola", [1, 2, 3])
    N.out  respuesta esperada (opcional); se compara con str(resultado)
"""
import ast
import builtins
import importlib.util
import sys
from pathlib import Path

FUNCION = "resolver"  # nombre de la función que pide el enunciado

AQUI = Path(__file__).resolve().parent


def cargar_dbg():
    """Busca lib/cp_helper.py hacia arriba y expone dbg (los dbg salen por stderr)."""
    for carpeta in AQUI.parents:
        if (carpeta / "lib" / "cp_helper.py").exists():
            sys.path.insert(0, str(carpeta / "lib"))
            from cp_helper import dbg
            builtins.dbg = dbg
            return


def cargar_solucion():
    spec = importlib.util.spec_from_file_location("solucion", AQUI / "solucion.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return getattr(modulo, FUNCION)


def leer_argumentos(archivo):
    lineas = [l for l in archivo.read_text(encoding="utf-8").splitlines() if l.strip()]
    return [ast.literal_eval(l) for l in lineas]


def main():
    cargar_dbg()
    funcion = cargar_solucion()
    entradas = sorted((AQUI / "casos").glob("*.in"))
    if not entradas:
        sys.exit("No hay casos en casos/*.in")
    fallos = 0
    for entrada in entradas:
        resultado = str(funcion(*leer_argumentos(entrada)))
        salida = entrada.with_suffix(".out")
        if salida.exists():
            esperado = salida.read_text(encoding="utf-8").strip()
            ok = resultado.strip() == esperado
            fallos += not ok
            print(f"{entrada.stem}: {'OK' if ok else 'FALLA'}  obtuve={resultado!r} esperado={esperado!r}")
        else:
            print(f"{entrada.stem}: (sin .out) obtuve={resultado!r}")
    print("TODO OK" if not fallos else f"{fallos} caso(s) fallaron")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
