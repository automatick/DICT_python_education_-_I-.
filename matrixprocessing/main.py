from typing import Self


class Matrix:

    def __init__(self, array: list):
        self.array: list = array

    def get_shape(self) -> tuple:
        rows = len(self.array) if isinstance(self.array, list) else 0
        cols = len(self.array[0]) if rows > 0 and isinstance(self.array[0], list) else 0
        return (rows, cols)

    def get_len(self): return len(self.array)

    def msum(self, matrix: Self) -> Self:
        if matrix.get_shape() != self.get_shape():
            raise ValueError("The shape of the matrices must be the same.")
        result = [
                [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
                for row1, row2 in zip(self.array, matrix.array)
            ]
        return Matrix(result)
    
    def __str__(self):
        return str(self.array)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])

result = m1.msum(m2)

print(result)
