import maya.mel as mel

# Ruta al archivo de MEL
ruta_archivo_mel = "D:/ejemplo.mel"

# Abrir y ejecutar el archivo de MEL
mel.eval('source "{}";'.format(ruta_archivo_mel))

'''
Archivo Mel:
polyCube -n "Mel";
'''
