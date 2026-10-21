"""Crea problems/<anio>/<nombre> a partir de _plantilla.

Uso: python problems/nuevo.py 2023 suma_k
"""
import shutil
import sys
from pathlib import Path

if len(sys.argv) != 3:
    sys.exit(__doc__)

raiz = Path(__file__).resolve().parent
destino = raiz / sys.argv[1] / sys.argv[2]
if destino.exists():
    sys.exit(f"Ya existe: {destino}")

shutil.copytree(raiz / "_plantilla", destino, ignore=shutil.ignore_patterns("__pycache__"))
print(f"Creado: {destino}")
print("Siguiente: pega el enunciado en enunciado.md, agrega casos en casos/ y escribe solucion.py")
