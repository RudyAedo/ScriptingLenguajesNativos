import maya.cmds as cmds

#Se definen las variables que usara el modelo
nombre='pepito'
tamanho=1

#Creo el personaje
#Uso la concatenación para generar un nombre dinámico
cmds.polySphere(n=(nombre+'_cabeza'),r=0.5)
cmds.move(0,2.3,0)

cmds.polySphere(n=(nombre+'_cuerpo'),r=1)
cmds.move(0,1,0)

cmds.polyCone(n=(nombre+'_nariz'),r=0.08,h=0.32)
cmds.move(0,2.343,0.63)
cmds.rotate(90,0,0)

#El parent permitira tener un objeto padre
cmds.parent((nombre+'_cabeza'),(nombre+'_nariz'),(nombre+'_cuerpo'))
#Establesco la selección del objeto padre
cmds.select(nombre+'_cuerpo')

#Se usa la variable tamanho para controla la escala
cmds.scale(tamanho,tamanho,tamanho)
