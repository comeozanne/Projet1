def simulation2(L,n):

    ListPos=[0 for k in range (L)]     #Stock la hauteur du dernier Ã©lÃ©ment de chaque colonne
    M=np.zeros((n,L))                 #ReprÃ©sentation matricielle de la modÃ©lisation

    for tirage in range (n+1):
        Emplacement=random.randint(0,L-1)
        Empl1=(Emplacement+1)%L

        ListPos[Emplacement]=1+max(ListPos[Emplacement],ListPos[Empl1])

        M[n-ListPos[Emplacement]][Emplacement]=20
        M[n-ListPos[Emplacement]][Empl1]=20
    H=max(ListPos)
    return M,H

L=50
n=100
N=500

import matplotlib.pyplot as plt
import numpy as np
import random


LH=[]
LH_sur_n=[]
for n2 in range (1,n):                      #On rÃ©alise la simulation pour chaque entier entre 1 et n
    Hmoy=0
    for i in range(N):
        H=simulation2(L,n2)[1]
        Hmoy+=H
    Hmoy=Hmoy/N
    print (Hmoy)                                        #Moy moyenne de H sur N expÃ©riences Ã  n2 test blocs

    LH.append(Hmoy)
    LH_sur_n.append(Hmoy/n2)                    #LH liste des Hmoy pour tous les test de 1 Ã  n blocs

plt.subplot(1,2,1)
plt.plot(LH)
plt.title("Hn moyen en fonction de n")
plt.subplot(1,2,2)
plt.plot(LH_sur_n)
plt.title("Hn/n moyen en fonction de n")
plt.show()