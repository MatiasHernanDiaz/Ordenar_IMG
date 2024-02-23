import modulo.archivo as a
import os
import sys


if __name__ == '__main__':
    if(len(sys.argv) == 1):
        ruta = os.getcwd()
        destino = os.getcwd()
    else:
        ruta = sys.argv[1]
        destino = sys.argv[2]
    
    for archivo in a.lsArch(ruta):
        a.moverArchivo(archivo, destino)
    
