def pearson_corr(lst1, lst2):

    if len(lst1) != len(lst2):
        print("Listy muszą mieć taką samą długość!")
        return None

    n = len(lst1) # = len(lst2)
    mean_x = sum(lst1)/n
    mean_y = sum(lst2)/n
    x_minus_mean = [ x - mean_x for x in lst1 ]
    y_minus_mean = [ y - mean_y for y in lst2 ]
    licznik_wek = [ x_minus_mean[i]*y_minus_mean[i] for i in range(0, n) ]
    licznik = sum(licznik_wek)

    x_minus_mean_2 = [ w**2 for w in x_minus_mean]
    y_minus_mean_2 = [ v**2 for v in y_minus_mean]

    mianownik = ( sum(x_minus_mean_2)*sum(y_minus_mean_2) )**0.5

    wynik = licznik/mianownik
    return wynik



lista1 = [1,2,3,1,2]
lista2 = [5, 1, 30, 23, -3]
print(pearson_corr(lista1, lista2))