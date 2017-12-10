from random import *

#Création du paquet rangé avec les chiffres ordonnés
paquet_melange = []
paquet_range= []
pile_de_jeu = [10]
sens = 1 #Sens de rotation positif
liste_joueur=[]
dico_joueur = {}
dico_cache_joueur = {}
i = 1

while i < 109 :
    paquet_range.append(i)
    i += 1

def initialisation(liste) :  #Mélange de la liste de chiffres rangés pour y placer dans un nouvelle liste mélangée
    i = 1 
    
    while i < 109 :
        liste.insert(randint(0,len(liste)), i)
        i += 1

#======================================================================CONVERTISSEUR======================================================================

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

#Principe de ce convertisseur : assigner un numéro réel à la carte (0, 1, 2, 3, Joker, Passe le tour...) puis une couleur, et concaténer le tout pour obtenir la carte.
#================================================================================================================================================================

#Fonctions concernant la pioche. Elles permettent de piocher, de désigner le paquet dans lequel piocher et de re-remplir la pioche quand celle-ci est vide.
def pioche(paquet, main_cache_joueur) : #Permet de piocher une carte et la retire de la liste pour ne pas piocher 2 fois la même
    carte_pioche = 200
    while not(carte_pioche in paquet) :
        carte_pioche = randint(0, len(paquet)-1)
    paquet.remove(carte_pioche)
    main_cache_joueur.append(carte_pioche)
    carte_pioche = texte(carte_pioche) #Passe dans le convertisseur 
    return carte_pioche #Carte piochée

def piocher(paquet, main_joueur, main_cache_joueur, carte_a_piocher): #Tant que n est inférieure au nombre de carte à piocher, on pioche et on rempli la main du joueur en s'aidant de la fonction "pioche"
	n=0
	
	while n < carte_a_piocher:
		carte = pioche(paquet, main_cache_joueur)
		main_joueur.append(carte)
		n=n+1

def pioche_vide(paquet, pilejeu) : #Rempli à nouveau la pioche quand celle-ci est vide.
    while len(pilejeu) != 1 :
        paquet.append(pilejeu[0])
        pilejeu.pop(0)
    shuffle(paquet)    

========================================================================================================================================================================

def verification(carte) : #Vérifie si la carte désignée est jouable sur la pile de jeu et renvoie un booléen
    derniere = pile_de_jeu[-1]
    if couleur(derniere) == couleur(carte) :
        return True
    if numero(derniere) == numero(carte) :
        return True
    if texte(derniere) == texte(carte) :
        return True
    if texte(carte) == "+4" :
        return True
    if texte(carte) == "Joker" :
        return True
    return False

def jouable(main) : #Vérifie si le joueur possède au moins une carte jouable dans sa main chiffré
    i = 0
    drapeau = False
    while i < len(main) :
        carte = main[i]
        if verification(carte) :
            drapeau = True
        i += 1
    if drapeau :
        return True
    else :
        return False

def choix(main, main_cache) :
    print(main)
    x = int(input("Quelle est l'indice de la carte que vous voulez jouer ? "))
    while not verification(main_cache[x]) :
        x = int(input("Quelle est l'indice de la carte que vous voulez jouer ? "))
    pile_de_jeu.append(main_cache[x])
    main.remove(main[x])
    main_cache.remove(main_cache[x])

def gestionjoueur (): #Fonction de gestion des joueurs, permet de connaitre le nombre de joueurs, le nombre de cartes qu'ils vont avoir et place le tout dans un dico.
	i = 0
	j = 0
	nb_joueur=int(input("Entrez le nombre de joueurs s'il vous plaît."))
	nb_carte=int(input("Entrez le nombre de cartes par joueurs s'il vous plaît."))
	liste_liste_joueur = []
	liste_liste_cache_joueur = []
	while i < nb_joueur: 
		liste_vide = []
		liste_vide_cache = []
		piocher(paquet_melange, liste_vide, liste_vide_cache, nb_carte)
		liste_liste_joueur.append(liste_vide)
		liste_liste_cache_joueur.append(liste_vide_cache)
		i = i+1

	i = 1
	while i <= nb_joueur:
		nom=input("Entrez le nom du joueur n°"+str(i))
		liste_joueur.append(nom)
		i=i+1

	while j < nb_joueur: #Place les joueurs et leur main correspondante dans un dictionnaire qui sera utilisé tout au long de la partie.
		dico_joueur[liste_joueur[j]] = liste_liste_joueur[j]
		dico_cache_joueur[liste_joueur[j]] = liste_liste_cache_joueur[j]
		j=j+1

def sens_rotation(liste_des_joueurs, liste_pile, dernier_joueur, sens) :
    derniere_carte = liste_pile[-1]
    i = -1 #indice du dernier joueur
    x = ",,"
    while x != dernier_joueur :
            i += 1
            x = liste_des_joueurs[i]
    if sens == 1 :#Sens POSITIF
        if numero(derniere_carte) == 11 : #Cas du change de sens
            sens = sens * (-1) #On multiplie par l'inverse pour inverser le pas et donc inverser le sens de rotation.
            if i == 0 :
                i = len(liste_des_joueurs) - 1
                prochain_joueur = liste_des_joueurs[i]
            else :
                prochain_joueur = liste_des_joueurs[i-1]
        elif numero(derniere_carte) == 12 : #Cas du passe ton tour
            i += 2 # On augmente le pas d'un "cran" temporairement pour sauter un joueur dans la liste
            if i == len(liste_des_joueurs) +1 :
                i = 1
                prochain_joueur = liste_des_joueurs[i]
            elif i == len(liste_des_joueurs) :
                i = 0
                prochain_joueur = liste_des_joueurs[i]
            else :
                prochain_joueur = liste_des_joueurs[i]
        else :
            if i == len(liste_des_joueurs) - 1 :
                i = 0
                prochain_joueur = liste_des_joueurs[i]
            else :
                prochain_joueur = liste_des_joueurs[i+1]
    if sens == -1 : #Sens NÉGATIF
        if numero(derniere_carte) == 11 :
            sens = sens * (-1)
            if i == len(liste_des_joueurs) - 1 :
                i = 0
                prochain_joueur = liste_des_joueurs[i]
            else :
                prochain_joueur = liste_des_joueurs[i+1]
        elif numero(derniere_carte) == 12 :
            i += -2
            if i == -2 :
                i = len(liste_des_joueurs) - 2
                prochain_joueur = liste_des_joueurs[i]
            elif i == -1 :
                i = len(liste_des_joueurs) - 1
                prochain_joueur = liste_des_joueurs[i]
        else :
            if i == 0 :
                i = len(liste_des_joueurs) - 1
                prochain_joueur = liste_des_joueurs[i]
            else :
                prochain_joueur = liste_des_joueurs[i-1]
    return prochain_joueur
    

def testvictoire (joueur_courant): #Évalue la main du joueur, si celle-ci correspond à une liste vide, le joueur a gagné la partie
	main = dico_joueur[joueur_courant]
	mainvide = []
	if main == mainvide:
		return True
	else:
		return False

def recuperateurnum (liste_joueur, joueur_courant): #Récupère le numéro du joueur courant et retourne ce numéro (place dans la liste)
	i=0
	while i < len(liste_joueur):
		nomjoueur=liste_joueur[i]
		i=i+1
		if nomjoueur == joueur_courant:
			return i 

def tourDeJeu (num_joueur, dico_des_joueurs, dico_cache_des_joueurs):
	main = dico_joueur[liste_joueur[num_joueur]]
	main_cache = dico_cache_joueur[liste_joueur[num_joueur]]
	if not jouable(main_cache): #Cas où aucune carte n'est jouable
		print("Aucune carte jouable")
		derniere_carte_joue = pile_de_jeu[-1]
		if numero(derniere_carte_joue)== 14:
			if len(paquet_melange)< 4: #Cas de la pioche si +4
				pioche_vide(paquet_melange, pile_de_jeu)
				piocher(paquet_melange, main, main_cache, 4)
			else:
				piocher(paquet_melange, main, main_cache, 4)
		
		if numero(derniere_carte_joue)== 10:
			if len(paquet_melange)< 2: #Cas de la pioche si +2
				pioche_vide(paquet_melange, pile_de_jeu)
				piocher(paquet_melange, main, main_cache, 2)
			else:
				piocher(paquet_melange, main, 2)
		else : 	
			piocher(paquet_melange, main, main_cache, 1)

	elif jouable(main_cache) : #Si au moins une carte est jouable, on lui demande quelle carte il souhaite jouer
		choix (main, main_cache)

	if testvictoire(liste_joueur[num_joueur]):
		nom=liste_joueur[num_joueur]
		print("Victoire de:" +str(nom))
		return True
	 

#========================================================================PROGRAMME PRINCIPAL========================================================================
initialisation(paquet_melange) #Création des paquets et des cartes
gestionjoueur() #Création des joueurs et de leurs mains.
dernier_joueur = liste_joueur[-1]
x = False

while x != True: #Tant que personne n'a gagné, le jeu continue.
    joueur_courant = sens_rotation(liste_joueur, pile_de_jeu, dernier_joueur, sens)
    num_joueur_courant = recuperateurnum(liste_joueur, joueur_courant)
    dernier_joueur = joueur_courant
    print("Tour de : " + str(joueur_courant))
    print("Dernière carte jouée : " + str(texte(pile_de_jeu[-1])))
    x = tourDeJeu(num_joueur_courant, dico_joueur, dico_cache_joueur)

print("Fin de la partie")


