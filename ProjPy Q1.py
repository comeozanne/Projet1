N=5000
L=50


import matplotlib.pyplot as plt
import numpy as np
import random

ListPos=[0 for k in range (L)]

for tirage in range (N):
    Emplacement=random.randint(0,L-1)   #On tire au sort pour chaque éléments sa colonne d'arrivée
    ListPos[Emplacement]+=1                #On compte le nombre d'élément de chaque colonne

H=0
for h in ListPos:
    if h>H:
        H=h                             #Calcul de la hauteur max H

M=np.zeros((H,L))

for k in range (len(ListPos)):
    for i in range (ListPos[k]):
        M[H-i-1][k]=20                  #On rempli le tableau en fonction du nombre d'éléments par colonne

plt.matshow(M,None)
plt.show()