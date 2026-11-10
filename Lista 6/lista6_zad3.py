from matplotlib.pyplot import (plot, show, xlabel, ylabel,
                               title, grid, yscale)
from time import perf_counter
#---------------------------------------------------------------------------

#rekurencyjna funkcja binom z wykładu nr 4:
def binom(n, k):
    if k in (0, n):
        return 1
    return binom(n - 1, k - 1) + binom(n - 1, k)



def czas_działania_binom(n):
    t0 = perf_counter()
    binom(n, n // 2)
    t1 = perf_counter()
    return (t1 - t0)

n_wek = range(0, 30)

czas1 = [czas_działania_binom(n) for n in n_wek ]


def wykres_binom():
    plot(n_wek, czas1)
    yscale("log")
    title("Czas działania funkcji binom(n, n//2) - skala log")
    xlabel("n")
    ylabel("Czas")
    grid()
    show()

#print(wykres_binom())

#-------------------------------------------------------------------------------

#iteracyjna funkcja binom2 z wykładu nr 5:
def pascal(n):
    triangle = [[1]]
    for i in range(n):
        prev_row = triangle[-1]
        next_row = [1]
        next_row.extend([prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)])
        next_row.append(1)
        triangle.append(next_row)
    return triangle


# alternatywna implementacja binom, z uzyciem pascal()
def binom2(n, k):
    return pascal(n)[n][k]


def czas_działania_binom2(n):
    t0 = perf_counter()
    binom2(n, n // 2)
    t1 = perf_counter()
    return (t1 - t0)

czas2 = [czas_działania_binom2(n) for n in n_wek ]

def wykres_binom2():
    plot(n_wek, czas2)
    title("Czas działania funkcji binom2(n, n//2)")
    xlabel("n")
    ylabel("Czas")
    grid()
    show()

print(wykres_binom2())