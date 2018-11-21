

import re

def segmentation_paragraphe(text):  #text est une liste de string
    taille=len(text)            #taille du texte coupe en liste
    texte=text[0]               #on initialise le texte non coupe en liste avec le text[0]
    if taille>0 :               
        for i in range(1,taille):
            texte=texte + text[i]   #on regroupe tout dans un string comme si il n'etait plus coupe
    newTexte = texte.replace(".\n",". @")   #remplace les differentes fin de paragraphe par un @
    newTexte=newTexte.replace("?\n",". @")
    newTexte=newTexte.replace("!\n",". @")
    newTexte=newTexte.replace(". »\n",". » @")
    newTexte=newTexte.replace("? »\n","? » @")
    newTexte=newTexte.replace("! »\n","! » @")
    
    newTexte=re.sub("[0-9]+","",newTexte) #supprime les numeros de pages
    newTexte=re.sub("[\n\n]+","",newTexte) #supprime les sauts de lignes inutiles
    
    listeParagraphe=newTexte.split("@") #Separe le texte au niveau des @ mis precedemment
    return listeParagraphe

