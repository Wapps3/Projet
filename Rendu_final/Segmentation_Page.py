# -*- coding: utf-8 -*-
import io
import numpy as np 



def identify_pages(texte): # identifier tous les pages dans le texte
    ls =('0','1','2','3','4','5','6','7','8','9')
    tableau = np.array([]) # stocker tous les pages et ses adresses dans array
    page_next = 0;
    for i, line in enumerate(texte):
        numWords =len(line.split())
        if numWords == 1: # un mot dans la ligne
            if line[0] in ls: #  un mot est numerique
                page_ = int(line)
                if len(tableau) == 0:
                    tableau = np.array([page_,i])
                    page_next = page_+1
                else:
                    if page_ == page_next:
                        tableau = np.vstack((tableau,[page_,i]))#Join a sequence of arrays along a new axis- trier
                        page_next = page_+1
                    else:
                        print('Page {} est pas continue'.format(page_next))# si la liste n'est pas continue- afficher ce message- check le texte
    return tableau
    
def segmentation_page(texte,*page): # texte / page soit 1 argurment or 2 arguments
    ltext = texte[0].split('\n')
    idPage = identify_pages(ltext)
    if page is not None:
        if len(page) ==1: # argurment : 1 page
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
        if len(page) ==2:# argurment à partir de 1 page à autre page
            page_start = page[0] # à partir de quelle page
            page_end = page[1]
            if page_start in idPage[:,0] and page_end in idPage[:,0]:
                if page_start == idPage[0,0]:
                    id_page_start = 0
                    id_page_end   = idPage[page_end-idPage[0,0],1]
                else:
                    id_page_start = idPage[page_start-idPage[0,0]-1,1]+1
                    id_page_end   = idPage[page_end-idPage[0,0],1]+1
                    #print (id_page_start)
                    #print(id_page_end )

            else:
                print('Page exist pas !')
                return False
        for n in range(id_page_start,id_page_end):
                print(ltext[n])
        return True
    else:
        print('Identifier la page du texte')
        return False


        
# =============================================================================
# =============================================================================
t = open('E:/EDUCATION/MASTER1/PROJECT-MANAGEMENT/Code/bel_Ami.txt', 'r',encoding='utf8')
bel_Ami=t.read()

bel=list()              
bel.append(bel_Ami)#met le texte dans une liste de string
segmentation_page(bel,12)
print('######################################')
segmentation_page(bel,5,8)
# =============================================================================

