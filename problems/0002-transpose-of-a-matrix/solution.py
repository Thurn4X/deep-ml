def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    lignes = len(a)
    colonnes = len(a[0])
    
    matrice_transposee = []
    
    # On boucle d'abord sur les colonnes (qui deviendront nos lignes)
    for j in range(colonnes):
        nouvelle_ligne = []
        # Ensuite on boucle sur les lignes pour récupérer les éléments de la colonne 'j'
        for i in range(lignes):
            nouvelle_ligne.append(a[i][j])
        
        # On ajoute cette nouvelle ligne à notre résultat final
        matrice_transposee.append(nouvelle_ligne)
        
    return matrice_transposee


    pass