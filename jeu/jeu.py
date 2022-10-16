from tkinter import *
import time
from random import randint
import keyboard


class MenuBar(Frame):
    "Barre de menus"

    def __init__(self):
        BarreMenu = MenuBar(Frame)
        # Création du sous-menu "Fichier":
        menuFichier = Menubutton(BarreMenu)
        # Créer une nouvelle instance du jeu en parallèle des autres
        menuFichier.add_command(text="Nouvelle fenêtre", command=Application())
        menuFichier.add_command(text="Quitter le jeu",
                                command=Application.destroy)            # Quitter le jeu
        # Raccourci pour créer une nouvelle fenêtre
        keyboard.add_hotkey("Ctrl + N", Application())
        # Raccourci pour quitter le jeu
        keyboard.add_hotkey("Ctrl + Q", Application.destroy)
        menuFichier.pack(side=LEFT)

        # Création du sous-menu "Commandes" :
        menuCommandes = Menubutton(BarreMenu)
        menuCommandes.add_command(text="Changer la direction vers la droite", command=Héros.right(
            1, 1))  # orienter le héros vers la droite en utilsant les positions y et x comme argument
        # orienter le héros vers la gauche avec les positions y et x
        menuCommandes.add_command(
            text="Changer la direction vers la droite", command=Héros.left(-1, 1))
        # Raccourci pour déplacer le héros vers la gauche en utilisant y et x
        keyboard.add_hotkey("q", Héros.left(-1, 1))
        # Raccourci pour déplacer le héros vers la droite en utilisant y et x
        keyboard.add_hotkey("d", Héros.right(1, 1))
        # Faire avancer le héros en utilisant positionX - 1
        menuCommandes.add_command(text="Avancer", command=Héros.avancer(1))
        # Faire reculer le héros en faisant positionX + 1
        menuCommandes.add_command(text="Reculer", command=Héros.reculer(1))
        # Raccouci pour faire avancer le héros
        keyboard.add_hotkey("keyright", Héros.avancer(1))
        # Raccouci pour faire reculer le héros
        keyboard.add_hotkey("keyleft", Héros.reculer(1))
        menuCommandes.pack(side=LEFT)

        # Création du sous-menu "Difficulté":
        menuDifficulté = Menubutton(BarreMenu)
        AugmenterTemps = menuDifficulté.add_command(
            text="Augmenter le temps d'1 minute", command=Temps.augmenter(1))  # Bouton pour augmenter le temps d'1 minute

        ReduireTemps = menuDifficulté.add_command(text="Réduire le temps d'1 minute", command=Temps.reduire(
            1))  # Bouton pour réduire le temps d'1 minute
        menuDifficulté.pack(side=LEFT)

        Frame.__init__(self)


class Héros(object):
    "Personnage contrôlé par le joueur"

    def __init__(self):
        # Image représentant le joueur
        self.image = PhotoImage(File="pacman.jpg")
        self.positionX = 0      # Position x du joueur
        self.positionY = 0      # Position y du joueur
        self.x = 0              # Orientation x donnée au départ au joueur
        self.y = 0              # Orientation y donnée au départ au joueur

    def avancer(self, x):
        "Mettre à jour la position positionX du héros pour le faire avancer"
        self.positionX -= x
        # Boules.position est la somme de positionX et positionY pour les boules
        if self.positionX and self.positionY == Boules.position:
            Boules.effacer()

    def reculer(self, x):
        "Mettre à jour la position positionX du héros pour le faire reculer"
        self.positionX += x
        if self.positionX and self.positionY == Boules.position:
            Boules.effacer()

    def positionner(self):
        "Donner la position initiale du joueur"
        # Charger l'image du joueur
        PhotoImage.load(self.image, position=self.x + self.y)
