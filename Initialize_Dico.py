# -*- coding: utf-8 -*-
import xlrd

def Initialize_Dico():
    
    path = "G:\\M1\\S1\\Projet\\Lexique382.xlsx"
    tableau = xlrd.open_workbook(path)
    
    feuille = tableau.sheet_by_name(tableau.sheet_names()[0])

    mot = feuille.col_values(0)
    lemme = feuille.col_values(2)
    dico = {}
    
    for i in range(len(mot)):       
        dico[ mot[i] ] = lemme[i]

    return dico
