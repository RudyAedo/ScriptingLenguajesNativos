import maya.cmds as cmds

def cadenaCubos(limiteX,sizeCubo,nomCubo):

   for x in range(limiteX):
      cmds.polyCube (name=(nomCubo+'_'+str(x)),depth=sizeCubo,height=sizeCubo,width=sizeCubo)
      cmds.move(0,(x*sizeCubo),0)

      if x>0:
         cmds.parent(nomCubo+'_'+str(x),nomCubo+'_'+str(x-1))

cadenaCubos(10,1,"cubo")
