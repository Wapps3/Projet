#--------------------------------FONCTION retrait stopword
#Besoin des packages :
#from nltk.tokenize import word_tokenize #pour tokeniser le text par mot 
# + Avoir la liste des stopword et eventuellement changer le chemin dans la fonction

# text --> liste de text
# stopword -->  1 = stop_word classic, 2 = stop_word lemmatisé, 3 = stop_word stemmisé, 4 = stop_word ponctuation 
def retrait_stopword(text, stopword):
    final = []
    sep = ' '
    #Import des listes de stopword en fonction du choix de l'utilisateur
    if stopword == 1 :
        #Import des sw classiques
        sw = open('stop_word_classic.txt', 'r')
        stop_word = sw.read()
        stop_word = word_tokenize(stop_word, language ='french')
    elif stopword == 2:
        #Import des sw lemmatisés
        sw = open('stop_word_lem.txt', 'r')
        stop_word = sw.read()
        stop_word = word_tokenize(stop_word, language ='french') 
    elif stopword == 3:
        #Import des sw stemmatisés / racinisés
        sw = open('stop_word_stem.txt', 'r')
        stop_word = sw.read()
        stop_word = word_tokenize(stop_word, language ='french')
    elif stopword == 4:
        #Import de la ponctuation
        sw = open('stop_word_ponctuation.txt', 'r')
        stop_word = sw.read()
        stop_word = word_tokenize(stop_word, language ='french')
    #Si la liste choisie est entre 1 et 4 c'est correct donc on retire, sinon afficher erreur
    if 0 < stopword < 5:
        for nText in range(0,len(text)):
            text_sans_sw=[]
            text_token = word_tokenize(text[nText], language ='french')
            for word in text_token:
                if word not in stop_word:
                    text_sans_sw.append(word)
            final.append(sep.join(text_sans_sw))
    else :
        print("Veuillez saisir une liste de stopword valide (1, 2, 3 ou 4 )")
    return final
