# -*- coding: utf-8 -*-
import numpy as np 

def identify_pages(texte): # identifier tous les pages dans le texte
    ls =('0','1','2','3','4','5','6','7','8','9')
    tableau = np.array([]) # stocker tous les pages et son adresse dans array
    page_next = 0;
    for i, line in enumerate(texte):
        numWords =len(line.split())
        if numWords == 1:
            if line[0] in ls: 
                page_ = int(line)
                if len(tableau) == 0:
                    tableau = np.array([page_,i])
                    page_next = page_+1
                else:
                    if page_ == page_next:
                        tableau = np.vstack((tableau,[page_,i]))
                        page_next = page_+1
                    else:
                        print('Page {} pas continue'.format(page_next))
    return tableau
    
def segmentation_page(texte,*page): 
    idPage = identify_pages(texte)
    if page is not None:
        if len(page) ==1: # si l'utilisateur veux trouver 1 page
            page_to_read = page[0]
            if page_to_read in idPage[:,0]:
                if page_to_read == idPage[0,0]:
                    id_page_start = 0
                    id_page_end   = idPage[page_to_read-idPage[0,0],1]+1

                else:
                    id_page_start = idPage[page_to_read-idPage[0,0]-1,1]+1
                    id_page_end   = idPage[page_to_read-idPage[0,0],1]+1
            else:
                print('Page est pas identifié!')
                return False
        if len(page) ==2:# si l'utilisateur veux trouver plusieur page. 
            page_start = page[0] # à partir de quelle page
            page_end = page[1]
            if page_start in idPage[:,0] and page_end in idPage[:,0]:
                if page_start == idPage[0,0]:
                    id_page_start = 0
                    id_page_end   = idPage[page_end-idPage[0,0],1]
                else:
                    id_page_start = idPage[page_start-idPage[0,0]-1,1]+1
                    id_page_end   = idPage[page_end-idPage[0,0],1]+1

            else:
                print('Page exist pas !')
                return False
        for n in range(id_page_start,id_page_end):
            
                print(texte[n])
        return True
    else:
        print('Identifier la page du texte')
        return False
        
# =============================================================================
t = open('E:/EDUCATION/MASTER1/PROJECT-MANAGEMENT/Code/bel_ami.txt', 'r',encoding='utf8')
# =============================================================================
bel_ami=t.readlines()# str => list
# 
# =============================================================================
segmentation_page(bel_ami,12) #: 1 page
#print('######################################')
segmentation_page(bel_ami,5,8)#: 2 - 2 argurements
#=============================================================================

