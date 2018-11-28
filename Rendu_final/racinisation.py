#import os
#os.chdir("C:\\Users\\emeri\\Desktop\\PROJET\\projet python test")

t = open('bel_ami.txt', 'r', encoding='utf-8')
text=t.read()
text=[text] # Bel ami est désormais dans une liste de 1 élément

#-------------------------------- FONCTION STEMMING - RACINISATION (Mettre les mots à la racine)
#Besoin des packages :
from nltk.tokenize import word_tokenize #pour tokeniser le text par mot
from nltk.stem.snowball import FrenchStemmer

def racinisation(text): #Liste de texte
    racinisation=[] #Rendu final
    for nText in range(len(text)): # Pour chaque élément de la liste :
        stemmer = FrenchStemmer() #Met dans "stemmer" les terminaisons fr à enlever
        text_token = word_tokenize(text[nText], language ='french') #On tokenize le texte pour avoir mot par mot
        text_stem = [] #Initialisation du texte racinisé
        sep = ' ' # le séparateur
        for word in text_token: #Pour chaque mot du texte tokenisé, on retire la terminainson
            w=stemmer.stem(word)
            text_stem.append(w)
        racinisation.append(sep.join(text_stem)) # On joint tout les mots racinisés en un seul élément
    return  racinisation

racinisation(text)
