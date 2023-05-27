N=50
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

    ListPos[Emplacement]=1+max(ListPos[(L+Emplacement+i)%L] for i in range (-k,k+1))

    for i in range (-k,k+1):
        ListPos[(L+Emplacement+i)%L]=ListPos[Emplacement]
        M[Hp-1-ListPos[Emplacement]][(L+Emplacement+i)%L]=20

H=0
for h in ListPos:
    if h>H:
        H=h

Mf=M[Hp-H:Hp-1][:]

plt.matshow(Mf,None)
plt.show()