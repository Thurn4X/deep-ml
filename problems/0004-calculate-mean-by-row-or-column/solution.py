import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrice_np = np.array(matrix)
    vecteurs = []
    final_list = []
    
    if mode == "column":
        for i in range(len(matrix[0])):
            vecteurs.append(matrice_np[:, i])
            
    if mode == "row":
        for i in range(len(matrix)):
            vecteurs.append(matrice_np[i, :])
    
    for element in vecteurs:
        moyenne = element.mean()
        final_list.append(moyenne)
        
    return final_list