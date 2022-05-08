#########################################
# groupe MI 02
# Asmaa ILIASSY
# Alexis BERTHOME-LAURENT
# Mohammed CHENNIG
# https://github.com/uvsq22106122/taquin.git
#########################################

import tkinter as tk
import random


import tkinter as tk
import random

class Taquin:
    def __init__(self):
        # Constantes-----------------------------#
        self.LARGEUR = 500
        self.HAUTEUR = 500
        self.CASES = 4
        self.LARG_CASES = self.LARGEUR // self.CASES
        self.HAUT_CASES = self.HAUTEUR // self.CASES

        self.taquin_win = [[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12],
                           [13, 14, 15, 0]]

        # Variables Global------------------------#
        self.tab = self.generer()
        self.history = []

        ##################################################
        # ---------------Fenetre------------------#
        racine = tk.Tk()
        racine.title("Taquin")

        # ---Canvas---#
        self.canvas = tk.Canvas(racine, bg="black", width=self.LARGEUR, height=self.HAUTEUR)
        self.canvas.grid()
        self.dessiner_tableau()

        # -------- Definition des Widgets------------------#
        self.bouton_sauvegarder = tk.Button(racine, text="Sauvegarder", command=self.sauvegarde)
        self.bouton_recharger = tk.Button(racine, text="Charger", command=self.recharger)
        self.bouton_annuler = tk.Button(racine, text="Annuler deplacement", command=self.annuler)

        # --------- Placement des widgets---------#
        self.bouton_sauvegarder.grid(row=5, column=0)
        self.bouton_recharger.grid(row=6, column=0)
        self.bouton_annuler.grid(row=7, column=0)

        # --------liaison d'evenement--------#
        self.canvas.bind("<Button-1>", self.clic)

        # ----Menu----#
        racine.mainloop()

    def dessiner_tableau(self):
        self.canvas.delete("all")
        for i in range(self.CASES):
            for j in range(self.CASES):
                if self.tab[j][i] != 0:
                    self.canvas.create_rectangle((i * self.LARG_CASES), (j * self.HAUT_CASES),
                                                 ((i + 1) * self.LARG_CASES),
                                                 ((j + 1) * self.HAUT_CASES), fill='grey', outline='white')
                    self.canvas.create_text(((2 * i + 1) * self.LARG_CASES / 2), ((2 * j + 1) * self.HAUT_CASES / 2),
                                            text=self.tab[j][i],
                                            fill='black', font=('Helvetica', '32'))
        self.victoire()

    def generer(self):
        t = [i for i in range(1, self.CASES ** 2)]
        random.shuffle(t)
        t.append(0)
        t1 = [[t[i + j * self.CASES] for i in range(self.CASES)] for j in range(self.CASES)]
        return t1

    def get_position(self, num):
        for i in range(len(self.tab)):
            if num in self.tab[i]:
                for j in range(len(self.tab[i])):
                    if self.tab[i][j] == num:
                        return i, j

    def permuter(self, ligne, x, y, i, j):
        while (x if ligne else y) != (j if ligne else i):
            self.tab[y][x], self.tab[i][j] = self.tab[i][j], self.tab[y][x]
            if ligne:
                x += 1 if x <= j else -1
            else:
                y += 1 if y <= i else -1

    def clic(self, event):
        x = event.x // self.LARG_CASES
        y = event.y // self.HAUT_CASES
        i, j = self.get_position(0)

        if (y != i and x != j) or (y == i and x == j):
            return

        self.permuter(y == i, x, y, i, j)

        self.dessiner_tableau()
        self.history.append((i, j))

    def sauvegarde(self):
        with open("sauvegarde", "w") as fic:
            for i in range(self.CASES):
                for j in range(self.CASES):
                    fic.write(str(self.tab[i][j]) + "\n")

    def recharger(self):
        with open("sauvegarde", "r") as fic:
            ligne = fic.readlines()
            for i in range(self.CASES):
                for j in range(self.CASES):
                    self.tab[i][j] = int(ligne[self.CASES * i + j])
        self.history = []
        self.dessiner_tableau()

    def annuler(self):
        if self.history:
            y, x = self.history[-1]
            i, j = self.get_position(0)

            self.permuter(y == i, x, y, i, j)

            del self.history[-1]

            self.dessiner_tableau()

    def victoire(self):
        if self.tab == self.taquin_win:
            print("You Win !")
            exit()


Taquin()
