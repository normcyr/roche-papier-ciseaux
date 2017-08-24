#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Version québécoise de pierre-papier-ciseaux.
'''

import random
from sys import argv
import argparse

def enregistrerChoixHumain(argv):

    choixHumain = argv[1]

    return(choixHumain)

def mainOrdi(possibilites):

    choixOrdi = random.choice(possibilites)

    return(choixOrdi)

def trouverGagnant(choixHumain, choixOrdi):

    if choixHumain == choixOrdi:
        gagnant = 'C\'est égal. Recommence!'

    else:
        if choixHumain == 'roche':
            if choixOrdi == 'papier':
                gagnant = False
            elif choixOrdi == 'ciseaux':
                gagnant = True

        elif choixHumain == 'papier':
            if choixOrdi == 'ciseaux':
                gagnant = False
            elif choixOrdi == 'roche':
                gagnant = True

        elif choixHumain == 'ciseaux':
            if choixOrdi == 'roche':
                gagnant = False
            elif choixOrdi == 'papier':
                gagnant = True

    return(gagnant)

def resultats(choixHumain, choixOrdi, gagnant):

    print('Ton choix est: {}'.format(choixHumain))
    print('Le choix de l\'ordinateur est: {}'.format(choixOrdi))

    if type(gagnant) == str:
        print(gagnant)

    elif type(gagnant) == bool:
        if gagnant == True:
            print('Tu as gagné, bravo!')
        elif gagnant == False:
            print('Tu as perdu!')

def main():

    possibilites = ['roche', 'papier', 'ciseaux']

    parser = argparse.ArgumentParser(description = 'Essaie de gagner à roche-papier-ciseaux contre l\'ordinateur')
    parser.add_argument('choix', help = 'inscris une option: roche OU papier OU ciseaux')
    args = parser.parse_args()

    if args.choix is not None:

        if args.choix in possibilites:
            choixHumain = enregistrerChoixHumain(argv)
            choixOrdi = mainOrdi(possibilites)
            gagnant = trouverGagnant(choixHumain, choixOrdi)
            resultats(choixHumain, choixOrdi, gagnant)

        else:
            print('Choix impossible')

if __name__ == '__main__':
    main()
