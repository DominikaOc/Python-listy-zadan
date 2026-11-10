from random import randint

def liczba_rzutów(n):
    rzut = [0]*n # lista n-elementowa
    # albo suma
    for i in range(n):
        ppoprzedni = randint(1, 4)
        poprzedni = randint(1, 4)
        obecny = randint(1, 4)
        rzut[i] = 3

        while True:
            if (ppoprzedni + poprzedni + obecny)%2 == 0 and poprzedni != obecny:
                break

            else:
                ppoprzedni = poprzedni
                poprzedni = obecny
                obecny = randint(1, 4)
                rzut[i] += 1

    result = "Średnia liczba rzutów dla n = {} : {}".format(n, sum(rzut)/n)
    print(result)

liczba_rzutów(100)
liczba_rzutów(10**5)  # między 4.6 - 4.7