from matplotlib.pyplot import (plot, show, xlabel, ylabel,
                               title, grid, yscale)
from math import pi, prod

def an(n):
    wektor_ak = [4*(-1)**k/(2*k + 1) for k in range(0, n+1, 1)]
    an = sum(wektor_ak)
    return an

def bn(n):
    wektor_bk = [ (2*k + 2)**2/((2*k + 1)*(2*k + 3)) for k in range(0, n+1, 1)]
    bn = 2*prod(wektor_bk)
    return bn

def cn(n):
    wektor_ck = [16**(-k)*( 4/(8*k + 1) - 2/(8*k + 4) - 1/(8*k + 5) - 1/(8*k + 6))
                 for k in range(0, n+1, 1)]
    cn = sum(wektor_ck)
    return cn


n_wek = range(5, 200, 1)
różnice_a = [abs(an(n) - pi) for n in n_wek]
różnice_b = [abs(bn(n) - pi) for n in n_wek]
różnice_c = [abs(cn(n) - pi) for n in n_wek]
różnice_c_log = [max(x, 10**(-17)) for x in różnice_c]



def wykres_a():
    plot(n_wek, różnice_a)
    title("Błąd bezwzględny oszacowania pi przez a_n")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()


def wykres_b():
    plot(n_wek, różnice_b, color="lightcoral")
    title("Błąd bezwzględny oszacowania pi przez b_n")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()


def wykres_c():
    plot(n_wek, różnice_c, color="forestgreen")
    title("Błąd bezwzględny oszacowania pi przez c_n")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()

def wykres_c_log():
    plot(n_wek, różnice_c_log, color="purple")
    title("Błąd bezwzględny oszacowania pi przez c_n - skala log")
    yscale("log")
    xlabel("n")
    ylabel("Błąd")
    grid()
    show()


print(wykres_c())
