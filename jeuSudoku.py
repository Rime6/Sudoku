def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient
        déja des nombres de 1 à 9
    '''
    if num in grille[row]:
        return False
    else:
        return True

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    for col in grille:
        if col==num:
            return False
        else:
            continue
    return True
def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    
    i=0
    while i<3:
        j=0
        while j<3:
            if grille[start_row + i][start_col + j] == num:
                return False
            j=j+1
        i=i+1
    return True
    
def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
    a=1
    i=0
    while i<9:
        j=0
        while j<9:
            if grille[i][j]==0:
                return False
            j=j+1
        i=i+1
    return True
    
def verifierValide(grille, row, col, num):
    ''' (list, int, int, int) ->  bool
    * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
    * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
    '''
    b=1
    return verifierSousGrille(grille, row, col, num) and verifierCol(grille, col, num) and verifierLigne(grille, row, num)
    
   
grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
              [7, 4, 6, 0, 3, 2, 8, 1, 9],
              [1, 9, 2, 0, 8, 4, 3, 5, 6],
              [8, 7, 1, 2, 6, 3, 4, 9, 5],
              [3, 2, 9, 4, 5, 7, 1, 6, 8],
              [4, 6, 5, 9, 1, 8, 7, 2, 3],
              [0, 0, 4, 3, 7, 9, 5, 8, 2],
              [9, 8, 3, 1, 0, 5, 6, 7, 4],
              [2, 5, 0, 8, 4, 6, 9, 3, 1]]

