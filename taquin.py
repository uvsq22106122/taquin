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


def affichage(self,event):
    global LARG_CASES, HAUT_CASES, tab
    if(self.i==0):self.x,self.y=event.x,event.y
    elif(self.i==1 or self.i==2):self.x1,self.y1=event.x,event.y


#### suite deplacement à venir######


def generer(tab):
    t = [i for i in range(1, CASES**2)]
    random.shuffle(t)
    t.append(0)
    t1 = [[t[i+j*4] for i in range(4)] for j in range(4)]
    return t1







#------Victoire----#



taquin_win= [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]

###print (taquin_gagner == "melanger")####




#-------Sauvegarde et recharge-------#
def sauvegarde():
    fic=open("sauvegarde", "w")
    for i in range(4):
        for j in range(4):
            fic.write(str(generer[i][j]) + "\n")
    fic.close()
    

def recharger():
    global LARG_CASES, HAUT_CASES, tab
    fic=open("sauvegarde", "r")
    ligne=fic.readlines() 
    l=0 
    for i in range(4): 
        for j in range(4):
            generer[i][j]=int(ligne[l]) 
            l+=1 
    fic.close()
    return init()

def annuler():
    deplacement = deplacement - 1
    pass

#Main-----------------------------------#


##################################################
#---------------Fenetre------------------#
racine = tk.Tk()
racine.title ("Taquin")

#---Canvas---#
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
tableau = init(canvas)

#-------- Definition des Widgets------------------#

bouton_sauvegarder= tk.Button(racine, text="Sauvegarder", command=sauvegarde)
bouton_recharger = tk.Button(racine, text="Charger",command=recharger)
bouton_annuler = tk.Button(racine, text="Annuler deplacement",command=annuler)

#--------- Placement des widgets---------#
bouton_sauvegarder.grid(row=5,column=0)
bouton_recharger.grid(row=6,column=0)
bouton_annuler.grid(row=7, column=0) 

#--------liaison d'evenement--------#

canvas.bind ("<Button-1>", affichage)


#----Menu----#

racine.mainloop()