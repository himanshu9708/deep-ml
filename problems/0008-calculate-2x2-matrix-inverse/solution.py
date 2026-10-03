import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    """

    val = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    if val == 0:
        return None

    return np.linalg.inv(matrix).tolist()