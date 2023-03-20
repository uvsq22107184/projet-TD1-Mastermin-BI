Mastermind en Python
Ce projet est une implémentation du jeu de plateau Mastermind en Python avec une interface graphique. Le joueur doit deviner un code secret formé de 4 pions de couleur alignés en au plus 10 essais de code. Les règles et les fonctionnalités du jeu sont décrites ci-dessous.

Fonctionnalités
Mode 2 joueurs : le premier joueur choisit le code secret, puis celui-ci est caché et l’autre joueur doit le trouver ;
Mode 1 joueur : idem sauf que le code secret est choisi au hasard au début du jeu ;
Sauvegarde et rechargement d'une partie en cours ;
Retour en arrière pour annuler des essais qui ont été faits ;
Aide proposant un code compatible avec les informations obtenues aux essais précédents ;
Modification des paramètres du jeu : le nombre de pions constituant le code secret, le nombre de couleurs et le nombre d’essais maximum ;
Mode sans joueur : le code à chercher est choisi au hasard et une intelligence artificielle (IA) joue à la place du joueur qui décode.
Règles du jeu
Il s’agit d’un jeu à 2 joueurs dans lequel un des joueurs choisit un code secret formé de 4 pions de couleur alignés et l’autre joueur doit deviner ce code en au plus 10 essais de code.
À chaque essai, le joueur qui décode acquiert l’information suivante :
Le nombre de pions bien placés (mais il ne sait pas lesquels) ; un pion est bien placé s’il a la même couleur que le pion qui est à la même position dans le code secret.
Le nombre de pions mal placés; un pion est mal placé s’il a la même couleur qu’un pion du code secret qui n’est pas à une position d’un pion bien placé ; de plus chaque pion du code secret peut compter pour au plus un pion mal placé.
Cette information peut être matérialisée par deux nombres accolés au code essayé ou bien, comme sur le jeu de plateau, par des petits pions dont le nombre indique en rouge (resp. en blanc) le nombre de pions bien (resp. mal) placés.
Prérequis
Python 3
Pygame
Comment jouer
Cloner ce dépôt en local.
Installer les prérequis en exécutant la commande suivante : pip install pygame
Lancer le jeu en exécutant la commande suivante : python main.py
Suivre les instructions affichées à l'écran pour jouer.
Auteur
Ce projet a été réalisé par [votre nom].
