from random import *

#Création du paquet rangé avec les chiffres ordonnés
paquet_melange = []
paquet_range= []
main_joueur1=[]
pile_de_jeu = [5, 8, 9, 10]
i = 1

while i < 109 :
    paquet_range.append(i)
    i += 1

def initialisation(liste) :  #Mélange de la liste de chiffres rangés pour y placer dans un nouvelle liste mélangée
    i = 1
    
    while i < 109 :
        liste.insert(randint(0,len(liste)), i)
        i += 1

def couleur(indice) : #Détermine la couleur en fonction du numéro de la carte piochée
    if 1 <= indice <= 25 :
        return " Rouge"
    if 26 <= indice <= 50 :
        return " Bleu"
    if 51 <= indice <= 75 :
        return " Jaune"
    if 76 <= indice <= 100 :
        return " Vert"
    if 101 <= indice <= 108 :
        return " Multicolore"

def numero(indice) : # Permet de renvoyer le numéro (correspondance) "physique" de la carte par rapport au numéro pioché 
    if couleur(indice) == " Multicolore" :
        if 101 <= indice <= 104 :
            return 13
        else :
            return 14
    if couleur(indice) == " Vert" :
        indice = indice - 75
    if couleur(indice) == " Jaune" :
        indice = indice - 50
    if couleur(indice) == " Bleu" :
        indice = indice - 25
    if couleur(indice) == " Rouge" :
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
            return 10
        if 22 <= indice <= 23 :
            return 11
        if 24 <= indice <= 25 :
            return 12

def texte(indice) : #Fait la correspondance entre le numéro de la carte piochée et la "vraie" carte 
    a = numero(indice)
    b = couleur(indice)
    if a == 13 :
        a = "Joker"
        return a
    if a == 14 :
        a = "+4"
        return a
    if a == 10 :
        a = "+2"
        x = a + b
    if a == 11 :
        a = "Change de sens"
        x = a + b
    if a == 12 :
        a = "Passe le tour"
        x = a + b
    else :
        a = str(a)
        x = a + b
    return x

def pioche(liste) : #Permet de piocher une carte et la retire de la liste pour ne pas piocher 2 fois la même
    carte_pioche = 200
    while not(carte_pioche in liste) :
        carte_pioche = randint(0, len(liste)-1)
    print(carte_pioche)
    liste.remove(carte_pioche)
    carte_pioche = texte(carte_pioche) #Passe dans le convertisseur 
    return carte_pioche #Carte piochée

def piocher(paquet, main_joueur, carte_a_piocher): #Tant que n est inférieure au nombre de carte à piocher, on pioche et on rempli la main du joueur en s'aidant de la fonction "pioche"
	n=0
	
	while n < carte_a_piocher:
		carte = pioche(paquet_melange)
		main_joueur.append(carte)
		n=n+1

def pioche_vide(paquet, pilejeu) :
    while len(pilejeu) != 1 :
        paquet.append(pilejeu[0])
        pilejeu.pop(0)
    shuffle(paquet)    

initialisation(paquet_melange)
pioche_vide(paquet_melange, pile_de_jeu)
print(pile_de_jeu)
print(len(paquet_melange))

