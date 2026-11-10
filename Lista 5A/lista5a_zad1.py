def determinant(matrix):
    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    return det

#macierz = [[1,2], [3,4]]
#print(determinant(macierz))


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        print("Macierz odwrotna nie istnieje.")
        return None
    result = [ [matrix[1][1]/det, -matrix[0][1]/det],
        [-matrix[1][0]/det, matrix[0][0]/det] ]
    return result

#x = inverse(macierz)


def product(matrix1, matrix2):
    a_00 = matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0]
    a_01 = matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1]
    a_10 = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
    a_11 = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]
    wynik = [[a_00, a_01], [a_10, a_11]]
    return print(wynik)

macierz1 = [[2,2], [3,4]]
macierz2 = [[5,6], [7,8]]
#product(macierz, x)