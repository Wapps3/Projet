# -*- coding: utf-8 -*-

def sep_chap(text):
    Chap=["\nI\n","\nII\n","\nIII\n","\nIV\n","\nV\n","\nVI\n","\nVII\n","\nVIII\n","\nIX\n","\nX\n"]
    for i in Chap:
        text=text.replace(i,'*')
    print("Nombre de chapitres : ",text.count("*"))#18 occurences qui remplace les 18 chapitres
    list_chap=text.split("*")[1:len(text.split("*"))]
    return (list_chap)
