import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    matrix = np.array(matrix)
    det = np.linalg.det(matrix)
    if det != 0:
        A_inv = np.linalg.inv(matrix)
    else:
        return None
    return A_inv