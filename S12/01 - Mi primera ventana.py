import maya.cmds as cmds

# Este será el nombre que usará la ventana que crearemos
win='miVentana'

# Valida si la ventana existe para tener una sola instancia de la misma
if cmds.window(win, exists= True):
    cmds.deleteUI(win, window= True)

# El flag 's' permite que la ventana se pueda redimensionar
cmds.window(win,t='Ventana',w=300,h=150,s= False,mxb=False,bgc=(0.6,0.6,0.6))

#cmds.columnLayout(w=150,h=150)  # Esto es lo que hace que Maya respete el tamaño

cmds.showWindow(win)

#Para elegir los colores de la interfaz pueden ir a:
# https://www.tydac.ch/color/
