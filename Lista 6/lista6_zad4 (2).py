from matplotlib.pyplot import (plot, show, xlabel, ylabel,
                               title, grid, yscale)
from math import pi, prod


an = 4  #a0
błędy_a = [abs(an - pi)]

for n in range(1, 200):
    an += 4 * (-1)**n / (2*n + 1)
    błędy_a.append(abs(an - pi))


b = 8/3          # b0
błędy_b = [abs(b - pi)]

for n in range(1, 200):
    b *= (2*n + 2)**2 / ((2*n + 1)*(2*n + 3))
    błędy_b.append(abs(b - pi))


cn = 4/1 - 2/4 - 1/5 - 1/6
błędy_c = [abs(cn-pi)]

for n in range(1,200):
    składnik = (
        16**(-n) * ( 4/(8*n+1) -2/(8*n+4) -1/(8*n+5) -1/(8*n+6) )
    )
    cn += składnik
    błędy_c.append(abs(cn-pi))

błędy_c_log = [max(x, 10**(-17)) for x in błędy_c]
n_wek = range(1, 201)

def wykres_a():
    plot(n_wek, błędy_a)
    title("Błąd bezwzględny oszacowania pi przez a_n")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()


def wykres_b():
    plot(n_wek, błędy_b, color="lightcoral")
    title("Błąd bezwzględny oszacowania pi przez b_n")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()


def wykres_c():
    plot(n_wek, błędy_c, color="forestgreen")
    title("Błąd bezwzględny oszacowania pi przez c_n")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()

def wykres_c_log():
    plot(n_wek, błędy_c_log, color="purple")
    title("Błąd bezwzględny oszacowania pi przez c_n - skala log")
    yscale("log")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()


print(wykres_c())