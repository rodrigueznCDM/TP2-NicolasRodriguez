print("TP2 - Jeu de Devinettes\n")

import random

print("J’ai choisi un nombre au hasard entre 0 et 1000, à vous de le deviner...")
randNum = random.randint(0,1000)

essai = int(input("Entrez votre essai:\n"))
nbEssais = 0

while essai != randNum:

    if essai < randNum:
        nbEssais = nbEssais + 1
        print("\nMauvais choix, le nombre est plus petit que", essai)

    elif essai > randNum:
        nbEssais = nbEssais + 1
        print("\nMauvais choix, le nombre est plus grand que", essai)