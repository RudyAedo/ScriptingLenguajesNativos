import maya.cmds as cmds
window_name = "ventanaGeometria"

cmds.window(window_name, title="Crear Geometría", widthHeight=(300, 200))

cmds.gridLayout(numberOfColumns=2, cellWidthHeight=(140, 60))

# El flag 'command' o 'c' ejecuta una instrucción
# Este flag puede llamar a un procedimiento
cmds.button(label="Crear Cubo", command="cmds.polyCube()")
cmds.button(label="Crear Esfera", command="cmds.polySphere()")
cmds.button(label="Crear Cono", command="cmds.polyCone()")
cmds.button(label="Crear Cilindro", command="cmds.polyCylinder()")

cmds.showWindow(window_name)
