#================================== Import =================================#

# deepcopy permet de copier des listes de listes
from copy import deepcopy

# randrange permet de prendre une valeur aleatoire entre arg1 inclus
# et arg2 non inclus
from random import randrange





#================================== Versions ===============================#
#                                                                           #
#   v1.0 : 1v1                                                              #
#   v1.1 : IA aleatoire                                                     #
#   v1.2 : IA intelligente(debut) + choix de la taille du plateau           #
#   v1.3 : l'IA regarde 4 coup dans le future + choix de la difficulter     #
#   v1.4 : test/debut de l'algorithme Alpha/Beta                            #
#   v1.5 : algorithme Alpha/Beta fonctionnel                                #







#==================================== Outil ================================#


def ResetGrid(x_size,y_size):
    """
    f( int , int ) -> list
    retourne la liste pour la partie avec la taille voulut"""
    # Met la liste gridRest avec que des 1 avec y_size pour hauteur
    # et x_size pour largeur puis la retourne
    gridReset = []
    for i in range(y_size):
        x_liste = []
        for j in range(x_size):
            x_liste += [1]
        gridReset += [x_liste]
    return gridReset


def NombrePosition(gridTest):
    """
    f( list ) -> int
    retourne le nombre de 1 present dans la liste en argument"""
    # commence en se disant qu'il y en a pas
    nombre = 0
    for i in range(len(gridTest)):
        for j in range(len(gridTest[0])):
            # ajoute 1 a 'nombre' quand il trouve un 1
            if gridTest[i][j] == 1:
                nombre += 1
    return nombre


def Remplace(x,y,gridModifie):
    """
    f( int , int , list ) -> list
    retourne la liste entree en argument en lui changeant la ligne x
    (en argument)et la colonne (y en argument) en 0"""
    # remplace a droite de la position jouer en (x;y)
    save = gridModifie[y-1]
    for i in range(len(save)):
        if i+1 >= x:
            save[i] = 0
    gridModifie[y-1] = save

    # remplace en bas de la position jouer en (x;y)
    for i in range(y):
        save = gridModifie[i]
        save[x-1] = 0
        gridModifie[i] = save
    return gridModifie


def Contient(gridTest):
    """
    f( list ) -> bool
    retourne True si la liste en argument contient 1 et False sinon"""

    # verifie que la liste gridTest contient encore une cases non utiliser
    if NombrePosition(gridTest) == 0:
        return False
    return True


def possible(x,y,grid):
    """
    f( str, str , list ) -> bool
    retourne False si la position x;y (entre en argument) est  un 1
    utilise VerifInput( str , int )"""

    if VerifInput(x,len(grid[0])) or VerifInput(y,len(grid)):
        return True
    # verifie si on peut jouer a une position (x;y)
    x = int(x)
    y = int(y)
    if grid[y-1][x-1] == 1:
        return False
    return True


def VerifInput(char,maxi):
    """
    f( str , int ) -> bool
    retourne False si une chaine de caractere est valide et True sinon
    (c'est pour l'entre de l'utilisateur)
    entree valide: nombre naturel sans 0 """

    # Evite que l'input soit faux
    if char == "":
        return True
    if type(char) != str:
        return True

    # Verifie si char est un input acceptable ou non
    charPossible = ["1","2","3","4","5","6","7","8","9","0"]
    for i in char:
        # verifie si le charactere i est dans la liste charPossible
        if i not in charPossible:
            return True


    # Evite que l'input 0 soit renvoyer alors quel il n'est pas valide
    # Alors que 10 ou 20 le sont
    if char == "0":
        return True
    # Evite d'entree des valeurs trop grande
    # si le programme arrive ici on est sur que c'est un entier
    # donc on peut utiliser 'int()'
    if int(char) > maxi:
        return True

    # Si le programme arrive ici c'est que tout est bon
    # donc il retourne False
    return False


def MontreJeu(grid):
    """
    f( list )
    permet l'affichage de la liste en argument soit le plateau"""

    for i in range(len(grid)):
        # affiche chaque element de la listedans la console
        print(grid[len(grid)-i-1])









#=============================== IA developpement ==========================#


################################## IA aleatoire #############################

def IA_aleatoire(grid):
    """
    f( list ) -> list
    retourne une position aleatoire
    utilise:
    possible( int , int or str , list ) et Remplace( int , int , list )"""

    # Recupere toutes les possibilites de jouer et les met dans 'pos'
    pos = []
    for i in range(len(grid)):
        entre = grid[i]
        for j in range(len(entre)):
            if entre[j] == 1:
                pos += [[j+1,i+1]]

    # Prend aleatoirement une position a jouer dans les positions legals
    rando = pos[randrange(0,len(pos))]
    x = rando[0]
    y = rando[1]

    # Retourne la liste modifiee
    return Remplace(x,y,grid)


############################### IA 'intelligente' #############################

def Eval(Evaluation):
    """
    f( list ) -> list
    retourne toutes les position possible de jouer au coup suivant
    (fait pour evaluer les possibilites de l'IA)"""
    newPosition = []
    for loop1 in range(len(Evaluation)):
        EvalX = Evaluation[loop1]
        for loop2 in range(len(EvalX)):
            if EvalX[loop2] != 0:
                # calcul le prochain coup
                newPosition += [[loop2+1,loop1+1]] + [Remplace(loop2+1,loop1+1,deepcopy(Evaluation))]

    # 'newPosition' est compose de 2 elements par coup possible
    return newPosition


def ScoreCounter(grid,coup,player):
    """
    f( list , int , int ) -> int
    retourne le score pour l'IA ou l'utilisateur en fonction de la position"""

    Score = 0

    # coup permet de gagner le plus rapidement possible

    # calcule le score du coup de l'IA
    if Contient(grid) and player == 1:
        if NombrePosition(grid) == 1:
            Score += coup * 10
        elif NombrePosition(grid) > 1:
            Score += coup
        else :
            Score -= coup * 2

    # calcule le score du coup de l'utilisateur
    if NombrePosition(grid) > 1 and player == 2:
            Score += coup
    return Score



def CalculScore(Grid,position,best):
    """
    f( list , int , int ) -> int
    retourne le score de la position Grid en argument
    et des 3 coups suivants (mais plus est possible XD) """
    coup = 10
    Score = 0

    # calcule le coup de l'IA

    Score += ScoreCounter(deepcopy(Grid[(position*2)+1]),coup,1)
    Tour2 = Eval(Grid[(position*2)+1])

    # calcule le score du coup apres l'IA par l'utilisateur
    coup -= 1
    for toure2 in range(int(len(Tour2)/2)):
        Score += ScoreCounter(deepcopy(Tour2[(toure2*2)+1]),coup,2)

        if NombrePosition(Tour2[(toure2*2)+1]) > 0 and Score > (best/2):
            Tour3 = Eval(Tour2[(toure2*2)+1])
            coup -= 1

            # calcule le coup de l'IA apres l'utilisateur
            for toure3 in range(int(len(Tour3)/2)):
                Score += ScoreCounter(deepcopy(Tour3[(toure3*2)+1]),coup,1)

                if NombrePosition(Tour3[(toure3*2)+1]) > 0 and Score < (best* (2/3)):
                    Tour4 = Eval(Tour3[(toure3*2)+1])
                    coup -= 1

                    # calcule le coup de l'utilisateur apres
                    # l'IA qui est apres l'utilisateur
                    for toure4 in range(int(len(Tour4)/2)):
                        Score += ScoreCounter(deepcopy(Tour4[(toure4*2)+1]),coup,2)

    # retourne le score total de la position Grid[(position*2)+1]
    return Score




def IA_EvaluPossibilite(gridEval):
    """
    f( list ) -> list
    retourne les scores calcules a partir des evaluations de la
    fonction Eval( list ) et CalculScore( list , int , int )"""
    ScoreEval = []
    Tour1 = Eval(gridEval)
    Best = -100000000
    for toure1 in range(int(len(Tour1)/2)):
        # Calcule le score de la position Tour1[toure1*2]
        # (le premier coup est a 10 et decroit de 1 a chaque fois)
        ScoreCoup = CalculScore(Tour1,toure1,Best)

        Best = max(Best,ScoreCoup)
        ScoreEval += [Tour1[toure1*2],ScoreCoup]
    return ScoreEval


def IA_forte(IA):
    """
    f( list ) -> list
    retourne le meilleur score des positions (et si plusieurs on le meme
    c'est de l'aleatoire qui decide pour eviter les repetitions)
    calcule avec IA_EvaluPossibilite( list ) et utilise
    Remplace( int , int , list )"""

    AllScore = IA_EvaluPossibilite(IA)
    best = -1000000000
    for evalu in range(int(len(AllScore)/2)):
        if AllScore[(evalu*2)+1] > best:
            best = AllScore[(evalu*2)+1]
            bestPosition = AllScore[(evalu*2)]
        elif AllScore[(evalu*2)+1] == best and randrange(0,1) == 0:
            bestPosition = AllScore[(evalu*2)]
    print("l'IA jou en " + str(bestPosition))
    return Remplace(int(bestPosition[0]),int(bestPosition[1]),IA)






############################## Minimax + alpha/beta ##########################




def EvalMinimax(Evaluation):
    """
    f( list ) -> list
    retourne toutes les position possible de jouer au coup suivant
    (fait pour evaluer les possibilites de l'IA)"""
    newPosition = []
    for loop1 in range(len(Evaluation)):
        EvalX = Evaluation[loop1]
        for loop2 in range(len(EvalX)):
            if EvalX[loop2] != 0:
                # calcul le prochain coup
                newPosition += [Remplace(loop2+1,loop1+1,deepcopy(Evaluation))]
    return newPosition


def ScoreMinimax(position,player,fin):
    """
    f( list , bool , int ) -> int
    retourne le score calcule a la position 'position'
    fin permet de gagner rapidemant"""

    # par exemple si l'IA est sur de gagner dans 5 coups et avec une autre
    # position elle est sur de gagner que dans 2 alors l'IA prendra
    # la victoire la plus rapide grace a la variable 'fin'
    Score = 0
    if NombrePosition(position) < 2:
        # permet a l'algorithme de savoir si il a ou non gagne
        # si NombrePosition n'est pas egale a 0 alors la partie
        # se termine au coup d'apres

        if NombrePosition(position) == 1:
            if player:
                Score += -10 - fin
            else:
                Score += 10 + fin
        else:
            if player:
                Score += 10 + fin
            else:
                Score += -10 - fin

    else:
        Score += randrange(0,2) - 1
        if NombrePosition(position)%2 == 0:
            if player:
                Score += 1
            else:
                Score -= 1
        else:
            if player:
                Score -= 1
            else:
                Score += 1

    return Score






def Minimax(position,fin,alpha=-100000,beta=100000,maxi=False):
    """
    f( list , int , int , int , bool ) -> int
    retourne le total de l'evaluation de l'IA en faisant l'arbre des
    possibles et l'algorithme minimax tout en 'elaguant' avec
    l'algorithme alpha/beta
    utilise:
    EvalMinimax( list ), ScoreMinimax( list , bool )"""

    # 'position' est la position a calculer le score
    # 'fin' permet de reduir l'arbre des possibles a une hauteur defini
    if fin == 0 or NombrePosition(position) < 2:
        return ScoreMinimax(position,maxi,fin)

    child = EvalMinimax(position)

    if maxi:
        maxEval = -100000
        for i in range(len(child)):
            evaluation = Minimax(child[i],fin-1,alpha,beta,False)

            maxEval = max(maxEval,evaluation)

            alpha = max(alpha,evaluation)

            if beta <= alpha:
                break

        return maxEval
    else:
        minEval = 100000
        for i in range(len(child)):
            evaluation = Minimax(child[i],fin-1,alpha,beta,True)

            minEval = min(minEval,evaluation)

            beta = min(beta,evaluation)

            if beta <= alpha:
                break

        return minEval






def IA_minimax(grid):
    """
    f( list ) -> list
    permet de faire jouer l'IA en utilisant l'algorithme alpha/beta
    utilise:
    EvalMinimax( list ), Minimax( list , int , int, int , bool )"""
    Possibilites = EvalMinimax(deepcopy(grid))
    Best = -10000000000
    BestPosition = Possibilites[1]
    for i in range(len(Possibilites)):
        # dans la fonction Minimax on commence avec False car on evalu deja les
        # positions que l'IA peut faire
        Evaluation = Minimax(Possibilites[i],4)
        if Evaluation + randrange(0,1) > Best:
            Best = Evaluation
            BestPosition = Possibilites[i]

    return BestPosition










#================================== Main game ==============================#



def Game_IA(x_size,y_size):
    """
    permet de jouer contre une IA jouant aleatoirement pour l'instant
    fait l'affichage de la partie
    utilise:
    Contient( int , int , list ), possible( int , int or str , list ),
    Remplace( int , int , list ), IA_aleatoire( list ),
    ResetGrid( int , int ) et IA_minimax( list )"""

    # Remet le jeu a zero et pose des questions comme la difficulter

    grid = list(ResetGrid(x_size,y_size))
    print("Entrez la difficulter de l'IA(max=10 / min=1, difficulter aleatoire par defaut)")
    print("/!\ SI LE PLATEAU A UNE TAILLE SUPERIEUR A 10x10 N'UTILISEZ PAS L'IA FORTE !!")
    difficulter = input()
    if not(VerifInput(difficulter,10)):
        difficulter = int(difficulter)
    else:
        if x_size * y_size < 65:
            difficulter = randrange(1,10)
        else:
            difficulter = 1
    print("Difficulter choisie : " + str(difficulter))
    print("Voulez vous utilisez l'algorithme Alpha/Beta? (OUI/NON)")
    AlphaBeta = input().lower()
    if AlphaBeta == "oui":
        AlphaBeta = True
    else:
        AlphaBeta = False
    joueur = randrange(0,1)
    if joueur == 1:
        print("L'IA commence")
    else:
        print("A vous de jouer")


    # Fait le jeu contre l'IA

    # Continut tant que l'on peut jouer: tant qu'il y a des 1 dans la liste

    while Contient(grid):
        if joueur == 0:
            # evite du code innutile (repetion de la boucle while)
            x = "no"
            y = 0
            while possible(x,y,grid):
                if x != "no":
                    print("mauvaise entre")
                MontreJeu(grid)
                print("joueur: " + str(joueur + 1))
                print("Quelle valeur de x? ")
                x = input()
                print("Quelle valeur de y? ")
                y = input()

            # L'entree est correct donc on joue:
            grid = Remplace(int(x),int(y),deepcopy(grid))
        else:
            print("Tour de l'IA")
            print("entrain de reflechir...")
            if randrange(0,difficulter+1) == 0 and difficulter != 10:
                # Fait jouer l'IA debile
                grid = IA_aleatoire(grid)
            else:
                # Fait joure l'IA intelligente
                if AlphaBeta:
                    # IA avec alpha beta
                    grid = IA_minimax(deepcopy(grid))
                else:
                    # IA sans alpha beta
                    grid = IA_forte(deepcopy(grid))
        joueur = 1 - joueur
    MontreJeu(grid)
    if joueur == 0:
        print("Vous avez gagner!!!!")
    else:
        print("L'IA a gagner !!")



def JoueurContreJoueur(x_size,y_size):
    """
    permet de jouer a deux (joueur vs joueur)
    utilise Remplace( int , int , list ),
    possible( int , int or str  , list ), Contient( list )
    et ResetGrid( int , int )"""

    # permet de faire joueur vs joueur avec l'affichage
    grid = ResetGrid(x_size,y_size)
    joueur = randrange(0,1)
    # Permet de nommer les joueur (par-ce que 'why not????')
    print("Voulez vous nommer les joueur ? (OUI/NON)")
    reponse = input().lower()
    if reponse == "oui" or reponse == "o" or reponse == "yes":
        joueurName = []
        print("Nom du premier :")
        joueurName += [input()]
        print("Nom du second :")
        joueurName += [input()]
    else:
        joueurName = ["1","2"]
    while Contient(grid):
        x = ""
        y = ""
        while possible(x,y,grid):
            MontreJeu(grid)
            if x != "" and y != "":
                print("mauvaise entree")
            print("joueur: " + joueurName[joueur])
            x = input("Quelle valeur de x? ")
            y = input("Quelle valeur de y? ")
        x = int(x)
        y = int(y)
        grid = Remplace(x,y,grid)
        joueur = 1 - joueur
    MontreJeu(grid)
    print(joueurName[joueur] + " a gagne la partie")



def MainGame():
    """
    permet de jouer au jeu en choisissant son mode (ex joueur vs IA)
    utilise Game_IA() et JoueurContreJoueur()"""
    # fait l'affichage et le jeu en lui meme
    mode = "start"
    while mode != "stop":
        print("Choisissez:")
        print("1: joueur contre IA")
        print("2: joueur contre joueur")
        mode = input()
        x = ""
        y = ""
        while VerifInput(x,30) or VerifInput(y,30):
            if x != "" and y != "":
                print("Mauvaise entree !!")
            # Fait en sorte d'avoir un plateau de taille variee
            print("Choisissez la largeur de votre plateau (max: 30)")
            x = input()
            print("Choisissez la hauteur de votre plateau (max: 30)")
            y = input()

        if mode == "1":
            Game_IA(int(x),int(y))
        else:
            JoueurContreJoueur(int(x),int(y))
        print("Appuyez sur entre pour recommencer")
        mode = input()





print("Pour commencer a jouer entrez 'MainGame()' dans la console")
