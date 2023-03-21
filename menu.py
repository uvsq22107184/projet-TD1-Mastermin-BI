import tkinter as tk
from mastermind import *

class MastermindGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mastermind")

        # Création des widgets pour la fenêtre principale
        self.label_titre = tk.Label(master, text="Mastermind", font=("Arial", 24))
        self.label_titre.pack()

        self.label_mode_jeu = tk.Label(master, text="Mode de jeu :")
        self.label_mode_jeu.pack()

        self.var_mode_jeu = tk.StringVar(value="1 joueur")

        self.radio_mode_1_joueur = tk.Radiobutton(master, text="1 joueur", variable=self.var_mode_jeu, value="1 joueur")
        self.radio_mode_1_joueur.pack()

        self.radio_mode_2_joueurs = tk.Radiobutton(master, text="2 joueurs", variable=self.var_mode_jeu, value="2 joueurs")
        self.radio_mode_2_joueurs.pack()

        self.label_nb_essais = tk.Label(master, text="Nombre d'essais :")
        self.label_nb_essais.pack()

        self.var_nb_essais = tk.IntVar(value=10)

        self.spin_nb_essais = tk.Spinbox(master, from_=1, to=20, increment=1, textvariable=self.var_nb_essais)
        self.spin_nb_essais.pack()

        self.label_nb_pions = tk.Label(master, text="Nombre de pions :")
        self.label_nb_pions.pack()

        self.var_nb_pions = tk.IntVar(value=4)

        self.spin_nb_pions = tk.Spinbox(master, from_=2, to=8, increment=1, textvariable=self.var_nb_pions)
        self.spin_nb_pions.pack()

        self.label_nb_couleurs = tk.Label(master, text="Nombre de couleurs :")
        self.label_nb_couleurs.pack()

        self.var_nb_couleurs = tk.IntVar(value=8)

        self.spin_nb_couleurs = tk.Spinbox(master, from_=2, to=10, increment=1, textvariable=self.var_nb_couleurs)
        self.spin_nb_couleurs.pack()

        self.button_demarrer = tk.Button(master, text="Démarrer", command=self.demarrer_jeu)
        self.button_demarrer.pack()

    def demarrer_jeu(self):
        mode_jeu = self.var_mode_jeu.get()
        nb_essais = self.var_nb_essais.get()
        nb_pions = self.var_nb_pions.get()
        nb_couleurs = self.var_nb_couleurs.get()

        if mode_jeu == "1 joueur":
            jeu = Mastermind(nb_essais, nb_pions, nb_couleurs)
        else:
            # TODO: implémenter le choix du code secret par le joueur 1
            pass

        # TODO: afficher l'interface de jeu pour le joueur 2 ou l'IA

root = tk.Tk()
gui = MastermindGUI(root)
root.mainloop()
