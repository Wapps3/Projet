#--------------------------------FONCTION retrait stopword
#Besoin des packages :
from nltk.tokenize import word_tokenize #pour tokeniser le text par mot
# + avoir lancé la fonction import_stopword

#la liste en entrée correspond à la liste des stopword obtenue après avoir alncé la fonction import
#stop_word[0] = classic, 1 = lemmatisé, 2 = stemmisé, 3 = ponctuation 
def retrait_stopword(liste, text):
    final = []
    sep = ' '
    for nText in range(len(text)):
        text_sans_sw=[]
        text_token = word_tokenize(text[nText], language ='french')
        for word in text_token:
            if word not in liste:
                text_sans_sw.append(word)
        final.append(sep.join(text_sans_sw))
    return final

retrait_stopword(sw[0], l_bel_ami)
#sw[0] = liste 1 (stop_word classic) obtenue lors de l'import des listes