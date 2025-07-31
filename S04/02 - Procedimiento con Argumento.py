#Importamos las librerias de Maya
import maya.cmds as cmds

#Creamos el procedimiento
#Este recibe un argumento llamado "nombre"

def ejemplo(nombre):
    
    #El argumento se usa como una variable
    #Se concatena para crear un nombre dinámico
  
    cmds.polySphere (n=(nombre+'_cabeza'),r=0.5)
    cmds.move (0,2.3,0)
    
    cmds.polySphere (n=(nombre+'_cuerpo'),r=1)
    cmds.move (0,1,0)
    
    cmds.polyCone (n=(nombre+'_nariz'),r=0.08,h=0.32)
    cmds.move (0,2.343,0.63)
    cmds.rotate (90,0,0)

#Se llama al procedimiento
#Se envia el valor que recibirá el argumento

ejemplo('Amica_2000')
