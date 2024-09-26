"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Jeu de devinettes
"""

import random

print("TP2 - Jeu de Devinettes\n")


def jeu_devinettes():

    print("J’ai choisi un nombre au hasard entre 0 et 1000, à vous de le deviner...")
    randNum = random.randint(0, 1000)

    win = False
    nb_essais = 0

    while not win:

        essai = -1

        while essai != randNum:

            try:
                essai = int(input("\nEntrez votre essai:\n"))

                if essai == randNum:
                    nb_essais += 1
                    print("\nBravo! Bonne réponse")
                    print("\nVous avez réussi en", nb_essais, "essai(s)")
                    win = True

                elif essai < randNum:
                    nb_essais += 1
                    print("\nMauvais choix, le nombre est plus petit que", essai)

                elif essai > randNum:
                    nb_essais += 1
                    print("\nMauvais choix, le nombre est plus grand que", essai)

            except ValueError:
                nb_essais += 1
                print("\nEntrez un nombre! Je compterais ceci comme un essai")


jeu_devinettes()


while True:

    rejouer = input("\nVoulez vous rejouer? (o/n):\n")
    rejouer = rejouer.strip()
    rejouer = rejouer.lower()

    if rejouer == "oui" or rejouer == "o":
        jeu_devinettes()

    elif rejouer == "non" or rejouer == "n":
        exit("\nMerci et au revoir!")

    else:
        print("\nEntrer oui ou non")
