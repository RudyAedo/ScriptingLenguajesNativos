//Creación de Objetos en PYTHON
import maya.cmds as cmds
cmds.sphere(n='Esfera',r=0.5)
cmds.move(0,1,0)
cmds.polyCube(n='Cubo',h=1,w=1,d=1)
