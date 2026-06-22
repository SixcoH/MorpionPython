case_vide = " "
plateau = [case_vide for i in range(9)] #on crée une variable qui va représenter le plateau 

joueur = "X"

choix_joueur = 0 

for i in range(9): #9 pour 9 caces
    plateau.append(case_vide)
print(plateau)

while True:
    choix_joueur = 0    

    while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] != case_vide:
    choix_joueur = int(input("Entrez une case entre 1 et 9 : ")) #ici la fonction input renvoie une string et que nous on aimerait avoir un entier on transforme le resultat de la fonction input en int



    plateau[choix_joueur - 1] = joueur

    for i in range(9):
        print(plateau[i], end=" ")
        if i % 3 == 2:
            print("")

    if case_vide != plateau[0] == plateau[1] == plateau[2] \
    or case_vide != plateau[3] == plateau[4] == plateau[5] \
    or case_vide != plateau[6] == plateau[7] == plateau[8] \
    or case_vide != plateau[0] == plateau[3] == plateau[6] \
    or case_vide != plateau[1] == plateau[4] == plateau[7] \
    or case_vide != plateau[2] == plateau[5] == plateau[8] \
    or case_vide != plateau[0] == plateau[4] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[6]:
        print("Ke joueur", joueur, "gagne la partie !")
    break

    joueur = "O" if joueur = "X" else "X"