import maya.cmds as cmds

window_name = "ventanaRenombrar"

# Si la ventana ya existe, eliminarla
if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name, window=True)

# Procedimiento que evaluará y renombrara los objetos
def renombrar():
    nombre=cmds.textField(val,q=True,text=True)
    objetos=cmds.ls(sl=True)
    cantidad=len(objetos)
    if len(nombre)==0 or cantidad==0:
        cmds.confirmDialog(t="Advertencia",m="Ingrese un nombre o seleccione un objeto",b="Ok",icn='warning')
    else:
        for x in range(cantidad):
            cmds.select(objetos[x])
            cmds.rename(nombre+"_"+str(x))
            cmds.select(cl=True)
        cmds.textField(val,edit=True, text='Ingrese un nombre')
        cmds.inViewMessage(amg='Nombres cambiados', pos='topCenter', fade=True)

vent=cmds.window(window_name,t="Rename",w=300,h=100,s=False,mnb=False,mxb=False)
cmds.columnLayout(nch=5,adj=True,rs=6)
cmds.text(l="Ingresa el prefijo que usarán los objetos seleccionados.",h=40)
cmds.separator(h=10)
val=cmds.textField(w=100,pht="Nombre",h=40)
cmds.iconTextButton(c="renombrar()",st="iconAndTextVertical",l="Renombrar",i="renamePreset",h=40,bgc=(.1,.1,.1))
cmds.separator(h=20)

cmds.showWindow(vent)
