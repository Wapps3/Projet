# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:07:22 2018

@author: bmchl
"""

#Besoin des packages :
from nltk.tokenize import word_tokenize #pour tokeniser le text par mot
# + la liste txt des stop word (4 txt)
#importer import_stopword et retrait_stopword
import re
#pour les expressions regulieres


#On va retirer les personnages et les lieux du textes en les plaçant dans un dictionnaire
#triés selon leurs parties

def retrait_Lieu_Perso(texte):
    texte=retrait_stopword(texte,1)
    texte=retrait_stopword(texte,2)
    dicoPerso = dict()
    taille = len(texte)
    for i in range (0,taille):
        perso = list()
        token_bel_ami = word_tokenize(texte[i], language ='french')
        taille2=len(token_bel_ami)
        j=0
        while (j!=taille2):
            if(token_bel_ami[j]=="rue" or token_bel_ami[j]=="impasse" or token_bel_ami[j]=="avenue" or 
               token_bel_ami[j]=="boulevard" or token_bel_ami[j]=="gare"):
                perso.append(token_bel_ami[j])
            elif(re.match('[A-Z]+|É',token_bel_ami[j])):
                    perso.append(token_bel_ami[j])
            j=j+1
        if(len(perso)>0):
            dicoPerso[i]=perso
        
    return dicoPerso
