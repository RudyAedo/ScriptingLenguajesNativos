import maya.cmds as cmds

def ctrlCuadrado(nombre):

    # Cada () con coordenadas indica la posición donde se crea un nodo nuevo
    cmds.curve(n=(nombre+"_grp"), p=[(-1, -1, 0), (-1, 1, 0), (1, 1, 0), (1, -1, 0), (-1, -1, 0)], d=1)
    
    cmds.circle(n=(nombre+"_ctrl"),r=0.2)
    
    # Se crea el texto que se mostrará
    cmds.textCurves(n=(nombre+"_txt"),t=nombre,f="Arial")
    cmds.move(-1.5,-2,0)
    
    cmds.parent((nombre+"_ctrl"),(nombre+"_txtShape"),(nombre+"_grp"))

    # Coloca los límites del deslizador
    cmds.transformLimits((nombre+"_ctrl"), tx=(-1, 1), etx=(1, 1))
    cmds.transformLimits((nombre+"_ctrl"), ty=(-1, 1), ety=(1, 1))
    cmds.transformLimits((nombre+"_ctrl"), tz=(0, 0), etz=(1, 1))
    
ctrlCuadrado("OjoIzq")

'''
Implementar tamaños personalizados
Hacer que el nombre que muestra sea diferente al nombre del objeto
'''
