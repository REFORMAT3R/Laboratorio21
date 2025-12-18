def copiar_archivo_binario(origen, destino):
    try:
        with open(origen, "rb") as archivo_origen:
            contenido = archivo_origen.read()

        with open(destino, "wb") as archivo_destino:
            archivo_destino.write(contenido)

        print("Archivo binario copiado correctamente")

    except FileNotFoundError:
        print("Error: el archivo origen no existe")

    except PermissionError:
        print("Error: no tienes permisos para acceder al archivo")

    except Exception as e:
        print("Error inesperado:", e)

copiar_archivo_binario("imagen.jpg", "copia_imagen.jpg")