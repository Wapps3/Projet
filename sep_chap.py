# -*- coding: utf-8 -*-

def sep_chap(text_l):
    Chap=["\nI\n","\nII\n","\nIII\n","\nIV\n","\nV\n","\nVI\n","\nVII\n","\nVIII\n","\nIX\n","\nX\n"]#Liste des numéros de chapitres de Bel Ami
    text_c=' '.join(text_l)
    for ch in Chap:
        text_c=text_c.replace(ch,'*')
    print("Nombre de chapitres : ",text_c.count("*"))#18 occurences qui remplace les 18 chapitres
    list_chap=text_c.split("*")[1:len(text_c.split("*"))]#On ignore le début du fichier qui ne correspond pas à un chapitre
    return (list_chap)