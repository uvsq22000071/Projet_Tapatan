#########################################
# groupe MPCI 2
# Zachary MARIANI
# Jeremy ZORIC
# Baptiste PARIS
# Mohamed AKARKACH
# Pascal CHRISTOPHE
# El guehoudi Wacil

# https://github.com/uvsq22004748/Projet-incendie
#########################################

# On importe tkinter

import tkinter as tk

racine = tk.Tk()

X = 100
Y = 100
COLORS = ['blue', 'rouge']
nombre_de_jetons = []

def lancement():
    ''' On definit une fonction qui va permettre de lancer le schéma du jeu du tapatan '''
    carre = canvas.create_rectangle(X, Y, 600 - X, 600 - Y, outline='white')
    ligne_verticale = canvas.create_line(3 * X, Y, 3 * X, 5 * Y, fill='white')
    ligne_horizontale = canvas.create_line(X, 3 * Y, 5 * X, 3 * Y, fill='white')
    diagonale1 = canvas.create_line(X, Y, 5 * X, 5 * Y, fill='white')
    diagonale2 = canvas.create_line(X, 5 * Y, 5 * X, Y, fill='white')

def clique(event):
    ''' Cette fonction va permettre de générer les jetons sur le schéma du jeu '''
    global nombre_de_jetons
    if (50 <= event.x <= 150) and (50 <= event.y <= 150):
        cercle1 = canvas.create_oval(X, Y, X, Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(1)
    if (250 <= event.x <= 350) and (50 <= event.y <= 150):
        cercle2 = canvas.create_oval(3 * X, Y, 3 * X, Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(2)
    if (450 <= event.x <= 550) and (50 <= event.y <= 150):
        cercle3 = canvas.create_oval(5 * X, Y, 5 * X, Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(3)
    if (50 <= event.x <= 150) and (250 <= event.y <= 350):
        cercle4 = canvas.create_oval(X, 3 * Y, X, 3 * Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(4)
    if (250 <= event.x <= 350) and (250 <= event.y <= 350):
        cercle5 = canvas.create_oval(3 * X, 3 * Y, 3 * X, 3 * Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(5)
    if (450 <= event.x <= 550) and (250 <= event.y <= 350):
        cercle6 = canvas.create_oval(5 * X, 3 * Y, 5 * X, 3 * Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(6)
    if (50 <= event.x <= 150) and (450 <= event.y <= 550):
        cercle7 = canvas.create_oval(X, 5 * Y, X, 5 * Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(7)
    if (250 <= event.x <= 350) and (450 <= event.y <= 550):
        cercle8 = canvas.create_oval(3 * X, 5 * Y, 3 * X, 5 * Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(8)
    if (450 <= event.x <= 550) and (450 <= event.y <= 550):
        cercle9 = canvas.create_oval(5 * X, 5 * Y, 5 * X, 5 * Y, fill='blue', outline='blue', width=20)
        nombre_de_jetons.append(9)
    print(nombre_de_jetons)
    if len(nombre_de_jetons) == 6:
        return none

def arreter():
    ''' Cette fonction va arreter le programme en cours '''
    racine.destroy()


SCORE = tk.Canvas(racine, width=100, height=200, bg="darkgrey")
SCORE.grid(row=1, column=2)
SCORE.create_line(0, 100, 100, 100, fill="black", width=2)
    
canvas = tk.Canvas(racine, width=600, height=600, bg='black')
lancement = tk.Button(racine, text='Lancement', bg='grey', command=lancement)
arreter = tk.Button(racine, text='Arrêter', bg='grey', command=arreter)
canvas.bind('<Button-1>', clique)

canvas.grid(row=0, column=0, columnspan=3)
lancement.grid(row=1, column=0)
arreter.grid(row=1, column=2)


racine.mainloop()
