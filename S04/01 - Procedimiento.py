#Importamos las librerias de Maya
import maya.cmds as cmds

#Creamos el procedimiento
def ejemplo():

#El espacio a la derecha se llama identación y es muy importante en Python
    cmds.polySphere (n='cabeza',r=0.5)
    cmds.move (0,2.3,0)
    
    cmds.polySphere (n='cuerpo',r=1)
    cmds.move (0,1,0)
    
    cmds.polyCone (n='nariz',r=0.08,h=0.32)
    cmds.move (0,2.343,0.63)
    cmds.rotate (90,0,0)

#Realizamos el llamado del procedimiento
ejemplo()
