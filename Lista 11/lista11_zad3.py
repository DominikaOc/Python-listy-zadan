from random import uniform

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def mean_distance(n, powtórzenia=10**4):
    śr_odl_wek = 0
    symbol_dwum = n*(n - 1)/2

    for _ in range(0, powtórzenia):

        x = [uniform(0, 1) for _ in range(n)]
        y = [uniform(0, 1) for _ in range(n)]
        suma = 0

        for i in range(0, n):
            for j in range(i+1, n):
                suma += distance(x[i], y[i], x[j], y[j])

        śr_odl_wek += suma/symbol_dwum

    średnia_odl = śr_odl_wek/powtórzenia

    result = "Średnia odl. dla n = {}: {}".format(n, średnia_odl)
    print(result)


for i in range(2, 11):
    mean_distance(i)

#wynik nie zależy od n i wynosi ok. 0.52