def copiar_archivo_texto(origen, destino):
    try:
        with open(origen, "r", encoding="utf-8") as archivo_origen:
            contenido = archivo_origen.read()

        with open(destino, "w", encoding="utf-8") as archivo_destino:
            archivo_destino.write(contenido)

        print("Archivo de texto copiado correctamente")

    except FileNotFoundError:
        print("Error: el archivo origen no existe")

    except PermissionError:
        print("Error: no tienes permisos para acceder al archivo")

    except Exception as e:
        print("Error inesperado:", e)

copiar_archivo_texto("origen.txt", "destino.txt")