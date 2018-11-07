# -*- coding: utf-8 -*-

def Segmentation_Personalisee(liste,separateur):
    segmentation = []
    mark = -1

    for nbrliste in range(len(liste)):
        
        mark = -1 # indice du dernier séparateur trouvé
        
        for i in range(len(liste[nbrliste])): # représente chq elts de la liste
            
            if liste[nbrliste][i] == separateur: # test si le separateur se trouve a cette indice
                segmentation.append(liste[nbrliste][mark+1:i]) # ajoute la partie entre le séparateur trouve et le dernier separateur enregistrer
                mark = i # separateur actuelle enregistre
                
        segmentation.append(liste[nbrliste][mark+1:]) # ajoute la partie du dernier separateu a la fin 
                
       
    return segmentation # retour le resultat final