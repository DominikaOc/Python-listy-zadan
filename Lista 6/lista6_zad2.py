from math import exp
from matplotlib.pyplot import (plot, show, xlabel, ylabel, title, grid)

def f(t, T_env, T_0, k):
    wynik = T_env + (T_0 - T_env)*exp(-k*t)
    return wynik

#--------------------------------- KAWA --------------------------------------
time = range(0, 3601, 1)
T_0 = 90
T_env = 20
k = 10**(-3)

temp = [f(t, T_env, T_0, k) for t in time]

def wykres_kawa():
    plot(time, temp)
    title("Temperatura kawy podczas stygnięcia")
    xlabel("Czas w sekundach")
    ylabel("Temperatura kawy")
    grid()
    show()

#wykres_kawa()

#--------------------------- METAL ------------------------------------
time = range(0, 61, 1)
T_0 = 900
T_env = 15
k = 1/10

temp = [f(t, T_env, T_0, k) for t in time]

def wykres_metal():
    plot(time, temp, color="mediumturquoise")
    title("Temperatura metalu podczas stygnięcia")
    xlabel("Czas w sekundach")
    ylabel("Temperatura metalu")
    grid()
    show()

wykres_metal()