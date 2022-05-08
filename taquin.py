#########################################
# groupe MI 02
# Asmaa ILIASSY
# Alexis BERTHOME-LAURENT
# Mohammed CHENNIG
# https://github.com/uvsq22106122/taquin.git
#########################################

import tkinter as tk
import random

# Constantes-----------------------------#
LARGEUR = 500
HAUTEUR = 500
CASES = 4
LARG_CASES = LARGEUR // CASES
HAUT_CASES = HAUTEUR // CASES

taquin_win = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 0]]


# Fonctions ------------------------------#

def victoire(tableau):
    global taquin_win

    if tableau == taquin_win:
        print("You Win !")
        exit()


def dessiner_tableau(canvas, tableau):
    global CASES, LARG_CASES, HAUT_CASES

    canvas.delete("all")
    for i in range(CASES):
        for j in range(CASES):
            if tableau[j][i] != 0:
                canvas.create_rectangle((i * LARG_CASES), (j * HAUT_CASES),
                                        ((i + 1) * LARG_CASES),
                                        ((j + 1) * HAUT_CASES), fill='grey', outline='white')
                canvas.create_text(((2 * i + 1) * LARG_CASES / 2), ((2 * j + 1) * HAUT_CASES / 2),
                                   text=tableau[j][i],
                                   fill='black', font=('Helvetica', '32'))
    victoire(tableau)


def position(tableau, nombre):
    global CASES

    for i in range(CASES):
        for j in range(CASES):
            if tableau[i][j] == nombre:
                return i, j


def permuter(tableau, ligne, x, y, i, j):
    while (x if ligne else y) != (j if ligne else i):
        tableau[y][x], tableau[i][j] = tableau[i][j], tableau[y][x]
        if ligne:
            x += 1 if x <= j else -1
        else:
            y += 1 if y <= i else -1
    return tableau


def clic(event):
    global LARG_CASES, HAUT_CASES
    global tab, historique, tableau_canvas

    x = event.x // LARG_CASES
    y = event.y // HAUT_CASES
    i, j = position(tab, 0)

    if (y != i and x != j) or (y == i and x == j):
        return

    tableau = permuter(tab, y == i, x, y, i, j)

    dessiner_tableau(tableau_canvas, tableau)
    historique.append((i, j))


def generer():
    global CASES

    t = [i for i in range(1, CASES ** 2)]
    random.shuffle(t)
    t.append(0)
    t1 = [[t[i + j * CASES] for i in range(CASES)] for j in range(CASES)]
    return t1


def sauvegarder():
    global CASES
    global tab

    with open("sauvegarde", "w") as fic:
        for i in range(CASES):
            for j in range(CASES):
                fic.write(str(tab[i][j]) + "\n")


def recharger():
    global CASES
    global tab, tableau_canvas

    with open("sauvegarde", "r") as fic:
        lignes = fic.readlines()
        for i in range(CASES):
            for j in range(CASES):
                tab[i][j] = int(lignes[CASES * i + j])
    dessiner_tableau(tableau_canvas, tab)


def annuler():
    global historique, tab, tableau_canvas

    if historique:
        y, x = historique[-1]
        i, j = position(tab, 0)

        tab = permuter(tab, y == i, x, y, i, j)

        del historique[-1]

        dessiner_tableau(tableau_canvas, tab)


##################################################

# Variables Globales---------------------#
tab = generer()
historique = []

# ---------------Fenetre------------------#
racine = tk.Tk()
racine.title("Taquin")

# ---Canvas---#
tableau_canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
tableau_canvas.grid()
dessiner_tableau(tableau_canvas, tab)


# -------- Definition des Widgets------------------#
bouton_sauvegarder = tk.Button(racine, text="Sauvegarder", command=sauvegarder)
bouton_recharger = tk.Button(racine, text="Charger", command=recharger)
bouton_annuler = tk.Button(racine, text="Annuler deplacement", command=annuler)

# --------- Placement des widgets---------#
bouton_sauvegarder.grid(row=5, column=0)
bouton_recharger.grid(row=6, column=0)
bouton_annuler.grid(row=7, column=0)

# --------liaison d'evenement--------#
tableau_canvas.bind("<Button-1>", clic)

# ----Menu----#
racine.mainloop()

