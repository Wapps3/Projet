#--------------------------------FONCTION import stopword
#Besoin des packages :
from nltk.tokenize import word_tokenize #pour tokeniser le text par mot
# + la liste txt des stop word (4 txt)

def import_stopword():
    stop_word = []
    #Import des sw classiques
    sw = open('stop_word_classic.txt', 'r')
    stop_word_classic = sw.read()
    stop_word_classic = word_tokenize(stop_word_classic, language ='french')
    #Import des sw lemmatisés
    sw = open('stop_word_lem.txt', 'r')
    stop_word_lem = sw.read()
    stop_word_lem = word_tokenize(stop_word_lem, language ='french') 
    #Import des sw stemmatisés / racinisés
    sw = open('stop_word_stem.txt', 'r')
    stop_word_stem = sw.read()
    stop_word_stem = word_tokenize(stop_word_stem, language ='french')
    #Import de la ponctuation
    sw = open('stop_word_ponctuation.txt', 'r')
    stop_word_ponctuation = sw.read()
    stop_word_ponctuation = word_tokenize(stop_word_ponctuation, language ='french') 
    #On retourn les 3 listes dans une liste 
    stop_word.append(stop_word_classic)
    stop_word.append(stop_word_lem)
    stop_word.append(stop_word_stem)
    stop_word.append(stop_word_ponctuation)
    return stop_word # liste de liste de stopwords

#stop_word[0] = classic, 1 = lemmatisé, 2 = stemmisé, 3 = ponctuation 