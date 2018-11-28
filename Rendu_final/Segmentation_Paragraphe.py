

import re
#--------------------------------Import du TXT
t = open('C:/Users/bmchl/Desktop/Cours/bel_ami.txt', 'r')
bel_ami=t.read()

text=list()              
text.append(bel_ami)#met le texte dans une liste de string


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
    
    newTexte=re.sub("[\n]+[0-9]+"," ",newTexte) #supprime les numeros de pages
    newTexte=re.sub("[\n\n]+"," ",newTexte) #supprime les sauts de lignes inutiles
    
    listeParagraphe=newTexte.split("@") #Separe le texte au niveau des @ mis precedemment
    return listeParagraphe
    
def afficher_paragraphe(listePara): #permet d'afficher la liste des paragraphes
    taille = len(listePara)
    print (taille)
    for i in range(0,taille):
        print("paragraphe :" )
        print (i)
        print (listePara[i])
        print (" ")

nouveau = segmentation_paragraphe(text)
afficher_paragraphe(nouveau)