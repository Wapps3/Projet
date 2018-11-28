# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import os
os.chdir('G:\\Rendu_Interface')
from Initialize_Dico import Initialize_Dico

def Lemmatisation(liste,dico):
    
    lemmatisation = []
    
    for nliste in range(len(liste)):
        
        texte_lemmatized = ""
        
        texte_tokenized = word_tokenize(liste[nliste], language ='french')
      
        
        for nmot in range( len(texte_tokenized) ):
            texte_lemmatized = texte_lemmatized + str(dico.get(texte_tokenized[nmot],texte_tokenized[nmot])) + " "
        
        lemmatisation.append(texte_lemmatized)
    
    return lemmatisation
        

t=open('G:\\Projet-Pr-Traitement-master\\Bel_Ami.txt', 'r')
bel_ami = t.read()
dico = Initialize_Dico()
liste=list()
liste.append(bel_ami)
Lemmatisation(liste,dico)




