#LISTAR ARCHIVOS
import os
import shutil
import modulo.carpeta as c

def lsArch(ruta):
    # Devuelve una lista con los archivos de la ruta
    return [archivo.name for archivo in os.scandir(ruta) if archivo.is_file()]

def ext(archivo):
    # Devuelve la extensión del archivo SIN el punto
    return os.path.splitext(archivo)[1][1::]

def esImagen(archivo):
    extensiones = ['jpg', 'jpeg', 'png']
    return ext(archivo) in extensiones

def nombreArchivo(archivo):
    #IMG_20230922_183952426_HDR - copia
    anio = archivo[4:8]
    mes = archivo[8:10]
    try:
        anio = int(anio)
        mes = int(mes)
        return str(anio) + '-' + str(mes)
    except:
        print("el nombre no es una fecha")
        return 'SIN_COINCIDENCIA'

def moverArchivo(archivo, destino):
    nombreCarpeta = nombreArchivo(archivo)
    if(c.existeCarpeta(nombreCarpeta, destino)):
        shutil.move(archivo, nombreCarpeta)
    else:
        try:
            c.crearCarpeta(nombreCarpeta, destino)
            shutil.move(archivo, nombreCarpeta)
        except:
            pass


if __name__ == "__main__":
    print("Direccion: " + os.getcwd())
    print("Listar archivos " , lsArch(os.getcwd()))
    print("Son imagenes?")
    for i in lsArch(os.getcwd()):
        print(i, '->', esImagen(i))
    print('-------------------')
    arch = 'IMG_20230922_183952426_HDR - copia'
    print('archivo -> IMG_20230922_183952426_HDR - copia')
    print(nombreArchivo(arch))
    