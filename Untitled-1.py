# taquin

#########################################
# groupe MI 02
# Asmaa ILIASSY
# Alexis BERTHOME-LAURENT
# Mohammed CHENNIG
# https://github.com/uvsq22106122/taquin.git
#########################################

import tkinter as tk
import random

#Constantes-----------------------------#
LARGEUR = 500
HAUTEUR = 500
CASES = 4
LARG_CASES = LARGEUR//CASES
HAUT_CASES = HAUTEUR//CASES

#Variable Global------------------------#
tab=[]

#Fonction-------------------------------#

def init(canvas):
    global LARG_CASES, HAUT_CASES, tab
    L=generer(tab)
    print(L)
    for i in range(CASES):
        for j in range(CASES):
            if L[j][i] != 0 : 
                canvas.create_rectangle((i*LARG_CASES), (j*HAUT_CASES), ((i+1)*LARG_CASES), ((j+1)*HAUT_CASES), fill='grey', outline = 'white')
                canvas.create_text(((2*i+1)*LARG_CASES/2), ((2*j+1)*HAUT_CASES/2), text=L[j][i], fill='black', font=('Helvetica', '32'))
    




# def affichage(event):
#     print("clic aux coordonnées ", event.x , event.y)
    


def generer(tab):
    t = [i for i in range(1, CASES**2)]
    random.shuffle(t)
    t.append(0)
    t1 = [[t[i+j*4] for i in range(4)] for j in range(4)]
    return t1




#Main-----------------------------------#


#---------------Fenetre------------------#
racine = tk.Tk()
#----------------Widget------------------#

#---Canvas---#
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
tableau = init(canvas)
# canvas.bind("<Button-1>", affichage)

#----Menu----#



racine.mainloop()


