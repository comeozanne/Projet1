
L=50
n=100
nombIte=1000

import matplotlib.pyplot as plt
import numpy as np
import random


LH=[]
for test in range (n):
    Ln=[]
    for zz in range(nombIte):


        N=test
        ListPos=[0 for k in range (L)]

        for tirage in range (N):
            Emplacement=random.randint(0,L-1)   #On tire au sort pour chaque éléments sa colonne d'arrivée
            ListPos[Emplacement]+=1                #On compte le nombre d'élément de chaque colonne

        H=0
        for h in ListPos:
            if h>H:
                H=h                             #Calcul de la hauteur max H

        Ln.append(H)

    Hmoy=0
    for gh in Ln:
        Hmoy+=gh
    Hmoy=Hmoy/len(Ln)                       #Moy moyenne de H sur nombIte expériences à test blocs



    LH.append(Hmoy)                         #LH liste des Hmoy pour tous les test de 0 à n

plt.plot(LH)
plt.show()