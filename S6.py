On recherche le zéro le plus petit de la fonction ( ... LAteX vie ...). Cette fonction est st. croissante sur [0,L], f(0) = -l'infini et f(L) = ln(3). On a donc que la fonction ne s'annule qu'une fois sur l'intervalle et on cherche la valeur a0 du zéro de f.
On va donc procéder par dichotomie et on obtient pour une précision à 10^(-6) près la valeur de a0 = 7.061362 avec le code suivant



import math as ma
L=50
a=0
b=L
while (b-a)>10**(-6):
    x=(a+b)/2
    if (L-x)/L<-ma.log(3*x/L):
        a=x
    else:
        b=x

