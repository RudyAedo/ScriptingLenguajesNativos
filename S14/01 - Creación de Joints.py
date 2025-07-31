import maya.cmds as cmds

def crear_ventana():
    window_name = "ventanaCrearCadenaJoints"
    
    # Si la ventana ya existe, eliminarla
    if cmds.window(window_name,ex=True):
        cmds.deleteUI(window_name)
    
    # Crear la ventana
    cmds.window(window_name, t="Crear Cadena de Joints", wh=(300,210),s=False,mxb=False)
    cmds.columnLayout(adj=True,mar=5,rs=8)
    
    cmds.text(l="Nombre de la cadena de joints:",al="left")
    nombre_cadena_text = cmds.textField (pht="Ingrese el nombre aquí")

    cmds.text(l="Cantidad de joints:",al="left")
    cantidad_joints_int = cmds.intField(min=1,max=999, v=2)
    
    cmds.text(l="Tamaño de los joints:",al="left")
    tamano_joints_int = cmds.floatField(min=1,max=999,pre=2,v=4)
    
    cmds.iconTextButton(bgc=(0.11,0.11,0.11),l="Crear Cadena de Joints",i="kinConnect",st="iconAndTextVertical",c=lambda *x: crear_cadena_joints(nombre_cadena_text, cantidad_joints_int, tamano_joints_int))

    cmds.showWindow(window_name)


def crear_cadena_joints(nombre_cadena_text, cantidad_joints_int, tamano_joints_int):
    # Obtener los valores ingresados por el usuario
    nombre_cadena = cmds.textField(nombre_cadena_text, query=True, text=True)
    cantidad_joints = cmds.intField(cantidad_joints_int, query=True, value=True)
    tamano_joints = cmds.floatField(tamano_joints_int, query=True, value=True)
    
    # Validar que el nombre de la cadena no esté vacío
    if not nombre_cadena:
        cmds.confirmDialog(t="Advertencia",m="Debe ingresar un nombre para la cadena de joints.",b="Ok",icn='warning')
        return
    
    # Crear la cadena de joints
    joints = []
    for i in range(cantidad_joints):

        joint_name = f"{nombre_cadena}_joint{i+1}"
        joint = cmds.joint(name=joint_name, position=(i*tamano_joints, 0, 0))
        joints.append(joint)
    
    # Crear el controlador principal
    controlador_nombre = f"{nombre_cadena}_ctrl"
    controlador = cmds.circle(n=controlador_nombre, nr=(1, 0, 0))[0]
    
    # Alinear el controlador al primer joint
    cmds.delete(cmds.parentConstraint(joints[0], controlador))
    
    # Parentar el primer joint al controlador
    cmds.parent(joints[0], controlador)
    
    print(f"Cadena de {cantidad_joints} joints y controlador '{controlador_nombre}' creados.")

# Ejecutar la función para crear la ventana
crear_ventana()
