import maya.cmds as cmds

# Ruta al archivo de Python en otro disco duro
ruta_archivo = "D:/ejemplo.py"

# Abrir el archivo en modo lectura
with open(ruta_archivo, "r") as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()

# Imprimir el contenido del archivo
print(contenido)
exec(contenido)

'''
Debe existir un documento con el nombre y en la ruta que se guarda en la línea 4

import maya.cmds as cmds
cmds.polyCube(w=1,h=1,d=1,n='SI')

'''
