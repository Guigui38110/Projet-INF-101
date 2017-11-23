#PROJET INFO 

from random import *

paquet_melange = []
paquet_range= []
i = 1

while i < 109 :
    paquet_range.append(i)
    i += 1

def initialisation(liste) :
    i = 0
    
    while i < 109 :
        liste.insert(randint(0,len(liste)), i)
        i += 1

def couleur(indice) :
    if 1 <= indice <= 25 :
        return "Rouge"
    if 26 <= indice <= 50 :
        return "Bleu"
    if 51 <= indice <= 75 :
        return "Jaune"
    if 76 <= indice <= 100 :
        return "Vert"
    if 101 <= indice <= 108 :
        return "Multicolore"

def numero(indice) :
    if couleur(indice) == "Multicolore" :
        if 101 <= indice <= 104 :
            return "Joker"
        else :
            return "+4"
    if couleur(indice) == "Vert" :
        indice = indice - 75
    if couleur(indice) == "Jaune" :
        indice = indice - 50
    if couleur(indice) == "Bleu" :
        indice = indice - 25
    if couleur(indice) == "Rouge" :
        if indice == 1 :
            return 0
        if 2 <= indice <= 3 :
            return  1
        if 4 <= indice <= 5 :
            return 2
        if 6 <= indice <= 7 :
            return 3
        if 8 <= indice <= 9 :
            return 4
        if 10 <= indice <= 11 :
            return 5
        if 12 <= indice <= 13:
            return 6
        if 14 <= indice <= 15 :
            return 7
        if 16 <= indice <= 17 :
            return 8
        if 18 <= indice <= 19 :
            return 9
        if 20 <= indice <= 21 :
            return "+2"
        if 22 <= indice <= 23 :
            return "Change de sens"
        if 24 <= indice <= 25 :
            return "Passe le tour"

def texte(indice) :
    a = numero(indice)
    b = couleur(indice)
    if a == "Joker" :
        return a
    if a == "+4" :
        return a
    if a == "+2" :
        x = a, b
    if a == "Change de sens" :
        x = a, b
    if a == "Passe le tour" :
        x = a, b
    if 0 <= a <= 9 :
        x = a, b
    return x

def pioche(liste) :
    carte_pioche = randint(1, 108)
    liste.remove(carte_pioche)
    carte_pioche = texte(carte_pioche)
    return carte_pioche
