# MORPION EN PYTHON
# Les joueurs jouent chacun leur tour en choisissant une case numérotée de 1 à 9.



# On définit une variable qui représente une case vide.
# C'est un simple espace " " (caractère blanc).
# On utilise une variable plutôt qu'écrire " " partout dans le code
# pour pouvoir changer facilement si besoin, et pour que le code soit lisible.
case_vide = " "

# On crée le plateau de jeu : une liste de 9 cases, toutes vides au départ.
# "for i in range(9)" signifie : répète 9 fois (de 0 à 8).
# La compréhension de liste [case_vide for i in range(9)] est un raccourci
# Python équivalent à écrire [" ", " ", " ", " ", " ", " ", " ", " ", " "].
# Les cases correspondent à la grille 3x3 du morpion :
#   [0][1][2]
#   [3][4][5]
#   [6][7][8]
plateau = [case_vide for i in range(9)]

# On définit les symboles utilisés par les deux joueurs.
# C'est un tuple (liste non-modifiable) de deux emojis.
# symboles[0] = "❌" pour le joueur 1
# symboles[1] = "⭕" pour le joueur 2
symboles = ("❌", "⭕")

# Les placeholders sont les numéros affichés dans les cases vides.
# Quand une case est libre, on affiche son numéro (1 à 9) pour aider
# le joueur à savoir quel chiffre taper pour y jouer.
# C'est aussi un tuple (non-modifiable, car l'ordre ne change jamais).
placeholder = ("1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ")

# On définit quel joueur commence.
# Au départ, c'est le joueur 1 (symboles[0] = "❌").
joueur = symboles[0]


# DÉFINITION DE LA FONCTION afficher_plateau()
# Une fonction est un bloc de code qu'on peut appeler plusieurs fois.
# Ici, cette fonction affiche l'état actuel du plateau dans le terminal.
def afficher_plateau():
    # On commence par afficher la ligne de séparation du haut.
    print(" ----+----+----")

    # On parcourt les 9 cases du plateau une par une (i va de 0 à 8).
    for i in range(9):
        # Pour chaque case, on affiche soit :
        #   - le symbole du joueur (❌ ou ⭕) si la case est occupée
        #   - le numéro de la case (placeholder) si elle est vide
        # La syntaxe "A if condition else B" signifie :
        #   affiche A si la condition est vraie, sinon affiche B.
        # "end=" " " dit à print() de ne PAS aller à la ligne après,
        # et d'afficher un espace à la place.
        print("|", plateau[i] if plateau[i] != case_vide else placeholder[i], end=" ")

        # Après chaque 3ème case (indices 2, 5, 8), on va à la ligne
        # et on affiche la séparation horizontale.
        # "i % 3 == 2" signifie : le reste de la division de i par 3 est 2.
        # C'est vrai pour i=2 (fin de ligne 1), i=5 (fin de ligne 2), i=8 (fin de ligne 3).
        if i % 3 == 2:
            print("|")              # Ferme la 3ème cellule et va à la ligne
            print(" ----+----+----")  # Affiche la séparation horizontale


# BOUCLE PRINCIPALE DU JEU
# "while True" crée une boucle infinie.
# Le programme tourne en boucle jusqu'à ce qu'un joueur gagne
# (le mot-clé "break" interrompra alors la boucle).
while True:
    # À chaque début de tour, on affiche le plateau actuel.
    afficher_plateau()

    # On initialise le choix du joueur à 0.
    # On le met à 0 exprès pour que la condition du while ci-dessous
    # soit vraie dès le départ (0 < 1), ce qui force l'entrée dans la boucle.
    choix_joueur = 0

    # BOUCLE DE SAISIE : on redemande au joueur tant que son choix est invalide.
    # La condition vérifie 3 choses (toutes doivent être fausses pour continuer) :
    #   1. choix_joueur < 1          → le numéro est trop petit (en dessous de 1)
    #   2. choix_joueur > 9          → le numéro est trop grand (au dessus de 9)
    #   3. plateau[choix_joueur - 1] != case_vide → la case est déjà occupée
    # Le "-1" est là parce que le joueur tape 1 à 9, mais les indices Python vont de 0 à 8.
    while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] != case_vide:
        # input() affiche un message et attend que l'utilisateur tape quelque chose.
        # int() convertit la réponse (qui est un texte) en nombre entier.
        choix_joueur = int(input("Entrez une case entre 1 et 9 : "))

    # On place le symbole du joueur actuel dans la case choisie.
    # On fait "-1" car le joueur tape 1-9 mais les indices du tableau sont 0-8.
    plateau[choix_joueur - 1] = joueur

    # VÉRIFICATION DE LA VICTOIRE
    # On vérifie toutes les combinaisons gagnantes possibles au morpion :
    #   - 3 lignes horizontales
    #   - 3 colonnes verticales
    #   - 2 diagonales
    # Chaque condition utilise le principe de comparaison chaînée Python :
    #   "case_vide != A == B == C" signifie :
    #     A n'est pas vide ET A est égal à B ET B est égal à C.
    # La barre oblique "\" en fin de ligne permet de continuer
    # l'expression sur la ligne suivante (lisibilité).

    if case_vide != plateau[0] == plateau[1] == plateau[2] \
    or case_vide != plateau[3] == plateau[4] == plateau[5] \
    or case_vide != plateau[6] == plateau[7] == plateau[8] \
    or case_vide != plateau[0] == plateau[3] == plateau[6] \
    or case_vide != plateau[1] == plateau[4] == plateau[7] \
    or case_vide != plateau[2] == plateau[5] == plateau[8] \
    or case_vide != plateau[0] == plateau[4] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[6]:
        # Si une combinaison gagnante est trouvée, on annonce le vainqueur.
        print("Le joueur", joueur, "gagne la partie !")
        # On affiche le plateau final pour que les joueurs voient la position gagnante.
        afficher_plateau()
        # "break" sort immédiatement de la boucle "while True" principale.
        # Le programme s'arrête ici.
        break

    # CHANGEMENT DE JOUEUR
    # Si personne n'a encore gagné, on passe au joueur suivant.
    # Cette ligne utilise l'opérateur ternaire : "A if condition else B"
    #   Si le joueur actuel est ❌ (symboles[0]), on passe à ⭕ (symboles[1]).
    #   Sinon (le joueur est ⭕), on repasse à ❌ (symboles[0]).
    joueur = symboles[1] if joueur == symboles[0] else symboles[0]
