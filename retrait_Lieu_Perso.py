# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:07:22 2018

@author: bmchl
"""
import os
os.chdir('C:/Users/bmchl/Desktop/Cours/Projet/Projet-Pr-Traitement-master')
#----------------------ATTENTION-----------------------
#REMPLACER LE CHEMIN CI DESSUS PAR LE CHEMIN OU SE TROUVE LE FICHIER RETRAIT_STOPWORD


#Besoin des packages :
from nltk.tokenize import word_tokenize #pour tokeniser le text par mot
# + la liste txt des stop word (4 txt)
from retrait_stopword import retrait_stopword
import re
#pour les expressions regulieres


#On va retirer les personnages et les lieux du textes en les plaçant dans un dictionnaire
#triés selon leurs parties

def retrait_Lieu_Perso(texte):
    texte=retrait_stopword(texte,1)     #retire les stopword
    texte=retrait_stopword(texte,2)
    dicoPerso = dict()          #On créé un dico ou on va mettre les valeurs
    taille = len(texte)
    for i in range (0,taille):      #pour chaque partie du texte
        perso = list()              #On va mettre les differents perso et lieux de chaque partie
        token_bel_ami = word_tokenize(texte[i], language ='french')     #on tokenise pour avoir qu'une liste de mot
        taille2=len(token_bel_ami)
        j=0
        while (j!=taille2):     #Pour chaque mot
            if(token_bel_ami[j]=="rue" or token_bel_ami[j]=="impasse" or token_bel_ami[j]=="avenue" or 
               token_bel_ami[j]=="boulevard" or token_bel_ami[j]=="gare"):  #Indique que c'est un lieu
                perso.append(token_bel_ami[j])      #Si oui on l'ajoute à la liste
            elif(re.match('[A-Z]+|É',token_bel_ami[j])):    #Si le mot commence par une majuscule (nom ou ville ou erreur des fois)
                    perso.append(token_bel_ami[j])
            j=j+1
        if(len(perso)>0):   #Si la liste n'est pas nulle on ajoute au dico qui affiche le numero de partie et la liste
            dicoPerso[i]=perso
        
    return dicoPerso
