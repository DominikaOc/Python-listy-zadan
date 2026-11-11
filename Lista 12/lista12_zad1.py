import numpy as np

def multiplication_table(n):

    #mnożenie macierzowe: wektor 10x1 i kolumna 1x10
    X = np.arange(1, n+1).reshape(n, 1)
    Y = np.arange(1, n+1).reshape(1, n)

    return X*Y

print(multiplication_table(10))