from typing import Self
import math

from typing import Self
import math

class Matrix:
    @staticmethod
    def is_valid(array):
        # Перевірка правильності вхідних даних (має бути список)
        if not array or not isinstance(array, list):
            raise TypeError("Input data must be array!")
        
        # Перевірка однакової довжини рядків
        row_length = len(array[0])
        for row in array:
            if not isinstance(row, list) or len(row) != row_length:
                raise ValueError("All the sub-arrays must have the same length.")
            if not all(isinstance(x, (int, float)) for x in row):
                raise ValueError("All the element of array must be numerical.")
    
    def __init__(self, array: list):
        # Ініціалізація матриці, перевірка її правильності
        self.is_valid(array)
        self.array: list = array

    def get_shape(self) -> tuple:
        # Повертає кількість рядків і стовпців матриці
        rows = len(self.array) if isinstance(self.array, list) else 0
        cols = len(self.array[0]) if rows > 0 and isinstance(self.array[0], list) else 0
        return (rows, cols)

    def get_len(self): 
        # Повертає кількість рядків матриці
        return len(self.array)

    def msum(self, matrix: Self) -> Self:
        # Додавання двох матриць
        if matrix.get_shape() != self.get_shape():
            raise ValueError("The shape of the matrices must be the same.")
        
        result = [
            [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
            for row1, row2 in zip(self.array, matrix.array)
        ]
        return Matrix(result)

    def const_mul(self, num: int) -> Self:
        # Множення матриці на константу
        result = [
            list(map(lambda x: x * num, row))
            for row in self.array
        ]
        return Matrix(result)

    def mat_mul(self, matrix: Self) -> Self:
        # Множення двох матриць
        if self.get_shape()[1] != matrix.get_shape()[0]:
            raise ValueError(
                "Number of columns in the first matrix must equal number of rows in the second matrix."
            )
        
        # Ініціалізація результату як нульової матриці
        result = [[0] * matrix.get_shape()[1] for _ in range(self.get_shape()[0])]

        # Перемноження матриць
        for i in range(self.get_shape()[0]):
            for j in range(matrix.get_shape()[1]):
                for k in range(self.get_shape()[1]):
                    result[i][j] += self.array[i][k] * matrix.array[k][j]
        
        return Matrix(result)

    def transpose(self) -> Self:
        # Транспонування матриці (поворот по діагоналі)
        transposed = [list(row) for row in zip(*self.array)]
        return Matrix(transposed)

    def transpose_secondary_diagonal(self) -> Self:
        # Транспонування по другій діагоналі (зворотне)
        rows, cols = self.get_shape()
        result = [
            [self.array[rows - 1 - j][cols - 1 - i] for j in range(rows)]
            for i in range(cols)
        ]
        return Matrix(result)

    def transpose_vertical(self) -> Self:
        # Транспонування по вертикалі (дзеркальне відображення по вертикалі)
        result = [row[::-1] for row in self.array]
        return Matrix(result)

    def transpose_horizontal(self) -> Self:
        # Транспонування по горизонталі (дзеркальне відображення по горизонталі)
        result = self.array[::-1]
        return Matrix(result)

    def determinant(self) -> float:
        """Обчислення детермінанту для квадратної матриці."""
        rows, cols = self.get_shape()
        if rows != cols:
            raise ValueError("Matrix must be square to compute determinant.")

        # Базовий випадок для 2x2 матриці
        if rows == 2:
            return self.array[0][0] * self.array[1][1] - self.array[0][1] * self.array[1][0]

        # Рекурсивний випадок для матриці більшого розміру
        det = 0
        for i in range(cols):
            sub_matrix = [row[:i] + row[i + 1:] for row in self.array[1:]]
            det += ((-1) ** i) * self.array[0][i] * Matrix(sub_matrix).determinant()
        return det

    def inverse(self) -> Self:
        """Знаходження зворотної матриці."""
        rows, cols = self.get_shape()
        if rows != cols:
            raise ValueError("Matrix must be square to compute the inverse.")

        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")

        # Обчислення матриці мінорів
        minors = []
        for i in range(rows):
            minor_row = []
            for j in range(cols):
                # Виключення i-го рядка та j-го стовпця
                sub_matrix = [
                    row[:j] + row[j + 1:] for row in self.array[:i] + self.array[i + 1:]
                ]
                minor_row.append(Matrix(sub_matrix).determinant())
            minors.append(minor_row)

        # Транспонування матриці мінорів (матриця алгебраїчних доповнень)
        cofactors = [
            [((-1) ** (i + j)) * minors[i][j] for j in range(cols)]
            for i in range(rows)
        ]

        # Транспонування матриці доповнень
        cofactor_matrix = Matrix(cofactors).transpose()

        # Множення на 1/детермінант
        return cofactor_matrix.const_mul(1 / det)

    def __str__(self):
        # Повертає рядкове представлення матриці
        return str(self.array)




def main():
    while True:
        print("\nMenu:")
        print("1. Add matrices")
        print("2. Multiply matrix by constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Transpose matrix by secondary diagonal")
        print("6. Transpose matrix by vertical axis")
        print("7. Transpose matrix by horizontal axis")
        print("8. Inverse matrix")
        print("9. Exit")

        try:
            choice = int(input("Choose an operation: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 9.")
            continue

        if choice == 1:
            print("\nEnter the first matrix:")
            matrix1 = input_matrix()
            if matrix1 is None:
                continue
            print("\nEnter the second matrix:")
            matrix2 = input_matrix()
            if matrix2 is None:
                continue
            try:
                result = matrix1.msum(matrix2)
                print("\nResult of matrix addition:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            print("\nEnter the matrix:")
            matrix = input_matrix()
            if matrix is None:
                continue
            try:
                num = float(input("Enter the constant to multiply the matrix by: "))
                result = matrix.const_mul(num)
                print("\nResult of constant multiplication:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            print("\nEnter the first matrix:")
            matrix1 = input_matrix()
            if matrix1 is None:
                continue
            print("\nEnter the second matrix:")
            matrix2 = input_matrix()
            if matrix2 is None:
                continue
            try:
                result = matrix1.mat_mul(matrix2)
                print("\nResult of matrix multiplication:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 4:
            print("\nEnter the matrix:")
            matrix = input_matrix()
            if matrix is None:
                continue
            result = matrix.transpose()
            print("\nResult of transposing the matrix:")
            print(result)

        elif choice == 5:
            print("\nEnter the matrix:")
            matrix = input_matrix()
            if matrix is None:
                continue
            result = matrix.transpose_secondary_diagonal()
            print("\nResult of transposing the matrix by the secondary diagonal:")
            print(result)

        elif choice == 6:
            print("\nEnter the matrix:")
            matrix = input_matrix()
            if matrix is None:
                continue
            result = matrix.transpose_vertical()
            print("\nResult of transposing the matrix by the vertical axis:")
            print(result)

        elif choice == 7:
            print("\nEnter the matrix:")
            matrix = input_matrix()
            if matrix is None:
                continue
            result = matrix.transpose_horizontal()
            print("\nResult of transposing the matrix by the horizontal axis:")
            print(result)

        elif choice == 8:
            print("\nEnter the matrix:")
            matrix = input_matrix()
            if matrix is None:
                continue
            try:
                result = matrix.inverse()
                print("\nResult of the inverse matrix:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 9:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()

