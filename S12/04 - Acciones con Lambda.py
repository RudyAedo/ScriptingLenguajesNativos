cmds.window(window_name, title="Ejecutar Múltiples Comandos", widthHeight=(300, 120))

# Crear un layout principal
cmds.columnLayout(adjustableColumn = True)

# Comandos múltiples en un solo botón
cmds.button(
    label="Crear Geometrías",h=50,
    command=lambda *args: exec(
        'cmds.polyCube();\n'
        'cmds.polySphere();\n'
        'cmds.polyCone();\n'
        'cmds.polyCylinder();'
    )
)

cmds.showWindow(window_name)
