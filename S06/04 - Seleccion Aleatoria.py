# Falta reconocer cuando no hay objetos en escena

import maya.cmds as cmds
import random

cmds.select(ado=True) #selecciona todos los objetos
objetos = cmds.ls(sl=True) #guarda los objetos seleccionados en el array
cmds.select(clear=True) #limpia la selección
inicio = 0
seleccion = 2

while inicio < seleccion:
    aleatorio = random.randint(0,len(objetos)-1)
    cmds.select (objetos[aleatorio],add=True)
    inicio=inicio+1 #Control para terminar el while
