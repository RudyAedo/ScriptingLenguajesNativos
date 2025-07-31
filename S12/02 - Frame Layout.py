import maya.cmds as cmds

win='miVentana'

if cmds.window(win, exists=True):
    cmds.deleteUI(win, window=True)

cmds.window(win,t='Frame Layout',w=400,h=500,s=True,mxb=False,bgc=(0.6,0.6,0.6))

cmds.frameLayout(l='Frame 1',cll=True) #-----------------
cmds.button(l='Botón 1',bgc=[0.3,0.3,0.3],h=50)
cmds.button(l='Botón 2',bgc=[0.3,0.3,0.3],h=50)
cmds.button(l='Botón 3',bgc=[0.3,0.3,0.3],h=50)
cmds.button(l='Botón 4',bgc=[0.3,0.3,0.3],h=50)
cmds.button(l='Botón 5',bgc=[0.3,0.3,0.3],h=50)
cmds.button(l='Botón 6',bgc=[0.3,0.3,0.3],h=50)
cmds.setParent('..') #----------------------------------

cmds.showWindow(win)
