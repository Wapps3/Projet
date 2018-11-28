# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def frequence_min(texte_l,n):
    #texte_l est une liste de texte
    #n est le nombre de mots que l'utilisateur souhaite afficher
    texte_c=' '.join(texte_l)
    token=word_tokenize(texte_c, language ='french')#Tokenise le texte
    freq=FreqDist(token)#Fréquence de chaque token dans la liste
    res=freq.most_common()[-n:len(freq)]#Affiche les n token les moins fréquents dans le texte
    return res

#import os
#os.chdir('E:/Cours/Projet')

fichier=open("Bel_Ami.txt","r")
t=fichier.read()
fichier.close

texte=[t]
freq_min=frequence_min(texte,10)
#print(freq_min)
