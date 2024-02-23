import os
import modulo.archivo as ar


def existeCarpeta(nombre, ruta):
    return nombre in ar.lsArch(ruta)


def crearCarpeta(nombre,ruta):
    if(not existeCarpeta(nombre, ruta)):
        try:
            os.mkdir(nombre)
            print("Se crea carpeta " , nombre)
        except:
            pass



if __name__ == "__main__":
    ruta = os.getcwd()
    print("ruta", ruta)
    print(existeCarpeta("nombre", ruta))
    crearCarpeta("imagenes", ruta)
    crearCarpeta( ar.nombreArchivo( 'IMG_20230922_183952426_HDR - copia.jpg') , ruta )