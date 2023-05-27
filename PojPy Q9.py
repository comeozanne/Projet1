N=4
L=50
Hp=N

import matplotlib.pyplot as plt
import numpy as np
import random

ListPos=[0 for k in range (L)]      #Stock la hauteur du dernier élément de chaque colonne
M=np.zeros((Hp,L))                  #Représentation matricielle de la modélisation

for tirage in range (N+1):
    Emplacement=random.randint(0,L-1)
    k=random.randint(0,3)
    if Emplacement !=0 and Emplacement!=L-1:
        ListPos[Emplacement]=1+max(ListPos[Emplacement-1],ListPos[Emplacement],ListPos[Emplacement+1])
        ListPos[Emplacement-1]=ListPos[Emplacement]
        ListPos[Emplacement+1]=ListPos[Emplacement]

        M[Hp-1-ListPos[Emplacement]][Emplacement-1]=20
        M[Hp-1-ListPos[Emplacement]][Emplacement]=20
        M[Hp-1-ListPos[Emplacement]][Emplacement+1]=20

    elif (Emplacement==0):
        ListPos[0]=1+max(ListPos[L-1],ListPos[0],ListPos[1])
        ListPos[L-1]=ListPos[0]
        ListPos[1]=ListPos[0]

        M[Hp-1-ListPos[0]][L-1]=20
        M[Hp-1-ListPos[0]][0]=20
        M[Hp-1-ListPos[0]][1]=20

    else:
        ListPos[L-1]=1+max(ListPos[L-1],ListPos[L-2],ListPos[0])
        ListPos[L-2]=ListPos[L-1]
        ListPos[0]=ListPos[L-1]

        M[Hp-1-ListPos[L-1]][L-2]=20
        M[Hp-1-ListPos[L-1]][0]=20
        M[Hp-1-ListPos[L-1]][L-1]=20

H=0
for h in ListPos:
    if h>H:
        H=h

Mf=M[Hp-H:Hp-1][:]

plt.matshow(Mf,None)
plt.show()