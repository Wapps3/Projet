# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 08:28:05 2018

@author: bmchl
"""
import os
os.chdir('C:/Users/bmchl/Desktop/Cours/Projet/Projet-Pr-Traitement-master')
            #REMPLACER ICI PAR LE CHEMIN OU SE TROUVE LE FICHIER A IMPORTER CI DESSOUS
from find_Words import find_Words


def find_Part(text,mot): #prend une liste de String et un mot
    dico=find_Words(text,mot)   #on effectue la fonction precedente
    taille = len(dico)  #taille du dictionnaire(donc nombre de partie)
    retour=list() #on initialise une liste qui portera le numero de chaque partie contenant le mot
    for i in range(0,taille):
        if(dico[i]!=[]):    #si la partie du dico ne contient rien
            retour.append(i)#on l'ajoute car elle ne contient pas le mot
    return retour


