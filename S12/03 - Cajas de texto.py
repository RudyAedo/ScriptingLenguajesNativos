import maya.cmds as cmds

win='miVentana'

if cmds.window(win, exists=True):
    cmds.deleteUI(win, window=True)

cmds.window(win,t='Frame Layout',w=400,h=500,s=True,mxb=False,bgc=(0.6,0.6,0.6))

cmds.frameLayout(l='Cajas de texto',cll=True) #-----------------

cmds.rowLayout(nc=2) #---------<
# Campo de texto
cmds.text(label="Nombre:")
cmds.textField(pht="Ingresa tu nombre aquí",w=200)
cmds.setParent('..') #---------<

cmds.rowLayout(nc=2) #--------->
# Campo de entero
cmds.text(label="Edad:")
cmds.intField(value=25,w=215)
cmds.setParent('..') #--------->

cmds.rowLayout(nc=2) #---------<
# Campo de flotante
cmds.text(label="Altura (metros):")
cmds.floatField(value=1.75,w=165)
cmds.setParent('..') #---------<

cmds.setParent('..') #----------------------------------
