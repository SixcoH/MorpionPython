plateau = [] #on crée une variable qui va représenter le plateau 
case_vide = " "

choix_joueur = 0 

for i in range(9): #9 pour 9 caces
    plateau.append(case_vide)
print(plateau)

while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] != case_vide:
    choix_joueur = int(input("Entrez une case entre 1 et 9 : ")) #ici la fonction input renvoie une string et que nous on aimerait avoir un entier on transforme le resultat de la fonction input en int

joueur = "X"

plateau[choix_joueur - 1] = joueur

