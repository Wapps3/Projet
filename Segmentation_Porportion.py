from nltk.tokenize import sent_tokenize #pour tokeniser le text par phrase
import numpy #PACKAGE OBLIGATOIRE pour la fonction segentation porportion


#Divise le texte en n parties compos�es de phrases (PACKAGE numpy et sent_tokenize OBLIGATOIRE) 
#Package numpy sert a additionner les termes d'une liste avec une autre (m�me taille)
# A besoin en entr�e du text et du nombre de parties voulu (n). Retourne une liste de taille n compos�es des phrases du texte
def Segmentation_Proportion(text, n):
    segmentation=list() #liste finale compos�e de n �l�ments comportants chacun plusieurs phrases
    sep=' ' # s�parateur en chaque phrase (correspond � l'espace qu'il y a entre la fin d'une pharse et le d�but d'une autre)
    liste=numpy.array([0])*n #liste qui va nous indiquer le nombre de phrases qu'il y a doit y avoir par partie (liste[0] = nb phrases en premi�re partie)
    a , p = 0,0 # des compteurs
    t = sent_tokenize(text, language ='french') #t devient une liste dont chaque �l�ments est une phrase
    l = len(t)  #nb phrases dans t
    if n > l: #si on demande plus de parties qu'il y a de phrase, �a ne sert a rien
        return print("Vous ne pouvez pas choisir un nombre de partie sup�rieur � ", l)
    else:
        while l != 0 : #Creation de listes de 1 qui vont �tre additionn�es pour connaitre le nombre de phrases necessaires par partie
            if l>n: #tant qu'il y a plus de phrases que de parties, on creer une liste de taille n remplis de 1
                l1=numpy.array([1]*n)
                i=n
            else: #Si il ne reste plus que quelques phrases � repartir (moins de n), alors on creer une liste de taille n remplie de 0
                l1=numpy.array([0]*n)
                i=l
                for y in range(0,l): #Si il ne reste que 3 phrases mais 5 parties, les 3 premiers �l�ments de la liste recoivent +1, et les autres 0
                    l1[y]=l1[y]+1
            liste=liste+l1 #On additionne chaque terme de la liste finale avec les liste l1 remplis de 1 ou de 1 et 0
            l=l-i #on soustrait � l (nombre de phrase qu'il reste � placer) le nombre de phrases qu'on vient de placer
        for y in range(0,n): # on sait d�sormais combien de phrases il doit y avoir dans chaque parties, il ne reste plus qu'� r�partir les phrases dans une liste de n �l�ments
            a=a+liste[y]
            segmentation.append(sep.join(t[p:a])) #sep.join sert a concatener toutes les phrases en 1 seul �l�ment avec comme s�parateur : sep
            p=a
    return segmentation # on retourne notre liste � n �l�ments compos�es de liste[0] phrases en premier �l�ments puis liste[1] phrases en deuxi�me �l�ments jusqu'� n
