# Object orientated implementation

class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = []

    def construct_matrix(self, queue):
        for _ in range(self.rows):
            arr = list(map(float, input(f'Enter {queue} matrix: ').split()))
            self.matrix.append(arr)

    def convert_2dlist_matrix(self, d_matrix):
        for i in range(self.rows):
            arr = d_matrix[i]
            self.matrix.append(arr)

    def __eq__(self, other) -> bool:
        return self.rows == other.rows and self.cols == other.cols

    def check_matrix(self, other) -> bool:
        return self.cols == other.rows

    def add_matrix(self, other):
        if self == other:
            result_matrix = [[float(self.matrix[i][j] + other.matrix[i][j]) for j in range(self.cols)] for i in range(self.rows)]
            return result_matrix
        else:
            print('The operation cannot be performed.')
            return None

    def scalar_multi(self, scalar):
        result_matrix = [[float(self.matrix[i][j] * scalar) for j in range(self.cols)] for i in range(self.rows)]
        return result_matrix

    def multiply_matrix(self, other):
        if self.check_matrix:
            result_matrix = [[round(sum(a*b for a, b in zip(self.rows, other.cols)), 2) for other.cols in zip(*other.matrix)] for self.rows in self.matrix]
            return result_matrix

    def diagonal_transpose_main(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return transposed_matrix

    def diagonal_transpose_side(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(self.cols-1, -1, -1)] for i in range(self.rows-1, -1, -1)]
        return transposed_matrix

    def diagonal_transpose_vertical(self):
        transpose_matrix = [row[::-1] for row in self.matrix]
        return transpose_matrix

    def diagonal_transpose_horizontal(self):
        transpose_matrix = self.matrix[::-1]
        return transpose_matrix

    def matrix_minor(self, i, j):
        minor = Matrix(i, j)
        for row in (self.matrix[:i]+self.matrix[i+1:]):
            minor.matrix.append(row[:j] + row[j+1:])
        return minor

    def get_determinant(self):
        # base case for 2x2 matrix
        if len(self.matrix) == 2:
            return self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]
        elif len(self.matrix) == 1:
            return self.matrix[0][0]

        determinant = 0
        for c in range(len(self.matrix)):
            determinant += ((-1)**c)*self.matrix[0][c]*Matrix.get_determinant(Matrix.matrix_minor(self, 0, c))
        return determinant

    def determinant_2n(self):
        return self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]

    def get_cofactor_matrix(self):
        cofactor_matrix = [[((-1)**(i+j))*Matrix.determinant_2n(Matrix.matrix_minor(self, i, j)) for j in range(self.cols)] for i in range(self.rows)]
        return

    # Temp codes
    @staticmethod
    def transpose(m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m))]

    def get_matrix_inverse(self):
        determinant = Matrix.get_determinant(self)
        if len(self.matrix) == 2:
            return [[self.matrix[1][1]/determinant, -1*self.matrix[0][1]/determinant], [-1*self.matrix[1][0]/determinant, self.matrix[0][0]/determinant]]

        cofactors = []
        for r in range(len(self.matrix)):
            cofactorRow = []
            for c in range(len(self.matrix)):
                minor = Matrix.matrix_minor(self, r, c)
                cofactorRow.append(((-1)**(r+c)) * Matrix.get_determinant(minor))
            cofactors.append(cofactorRow)
        cofactors = Matrix.transpose(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors


def matrix_addition():
    matrix_a = Matrix(*map(int, input('Enter size of first matrix: ').split()))
    matrix_a.construct_matrix('first')
    matrix_b = Matrix(*map(int, input('Enter size of second matrix: ').split()))
    matrix_b.construct_matrix('second')
    result = matrix_a.add_matrix(matrix_b)
    return result


def matrix_constant_multi():
    matrix_a = Matrix(*map(int, input('Enter size of matrix: ').split()))
    matrix_a.construct_matrix('')
    scalar = float(input('Enter constant: '))
    result = matrix_a.scalar_multi(scalar)
    return result


def multiply_matrices():
    matrix_a = Matrix(*map(int, input().split()))
    matrix_a.construct_matrix('first')
    matrix_b = Matrix(*map(int, input().split()))
    matrix_b.construct_matrix('second')
    result = matrix_a.multiply_matrix(matrix_b)
    return result


def transpose(opt):
    matrix_a = Matrix(*map(int, input('Enter size of matrix: ').split()))
    matrix_a.construct_matrix('')
    if opt == 1:
        result = matrix_a.diagonal_transpose_main()
    elif opt == 2:
        result = matrix_a.diagonal_transpose_side()
    elif opt == 3:
        result = matrix_a.diagonal_transpose_vertical()
    elif opt == 4:
        result = matrix_a.diagonal_transpose_horizontal()
    return result


def matrix_determinant():
    matrix_a = Matrix(*map(int, input().split()))
    matrix_a.construct_matrix('')
    result = matrix_a.get_determinant()
    return result


def inverse_matrix():
    matrix_a = Matrix(*map(int, input().split()))
    matrix_a.construct_matrix('')
    # det = matrix_a.get_determinant()
    # if det == 0:
    #     return None
    # cofactor_matrix = matrix_a.get_cofactor_matrix()
    # cofac_matrix = Matrix(matrix_a.rows, matrix_a.cols) # Matrix Object Template
    # cofac_matrix.convert_2dlist_matrix(cofactor_matrix) # Convert the 2D list to Matrix Object
    # cof_matrix = cofac_matrix.diagonal_transpose_main() # Transpose the cofactor matrix
    # cofac_matrix2 = Matrix(matrix_a.rows, matrix_a.cols) # Matrix Object Template 2
    # cofac_matrix2.convert_2dlist_matrix(cof_matrix) # Convert the 2D list to Matrix Object
    # scalar = 1 / det
    # result = cofac_matrix2.scalar_multi(scalar)

    result = matrix_a.get_matrix_inverse()
    return result


def print_matrix(matrix) -> None:
    print('The result is:')
    for row in matrix:
        print(*row)
    print('\n')


def main():
    while True:
        val = int(input('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\nYour choice:'))
        if val == 1:
            result = matrix_addition()
            if result:
                print_matrix(result)
        elif val == 2:
            result = matrix_constant_multi()
            if result:
                print_matrix(result)
        elif val == 3:
            result = multiply_matrices()
            if result:
                print_matrix(result)
        elif val == 4:
            transpose_opt = int(input('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\n'))
            result = transpose(transpose_opt)
            if result:
                print_matrix(result)
        elif val == 5:
            result = matrix_determinant()
            print(f'The result is:\n{result}')
        elif val == 6:
            result = inverse_matrix()
            if result:
                print_matrix(result)
            else:
                print("This matrix doesn't have an inverse.")
        else:
            break


if __name__ == '__main__':
    main()
