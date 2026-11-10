from math import sin, cos, pi
from matplotlib.pyplot import (plot, show, xlabel, ylabel, title, grid)

n = 3
m = 3

#funkcja z wykładu:
# jak range, ale z krokiem niecałkowitym, tylko dla ciągów rosnących
def frange(start, final, step=1.0):
    result = []
    while start < final:
        result.append(start)
        start = start + step
    return result

time = frange(0, 2*pi + 1/100, 2*pi/100)

def x(t):
    wynik = cos(t) + cos((n+1)*t)/2 + sin((m+1)*t)/3
    return wynik

def y(t):
    wynik = sin(t) + sin((n+1)*t)/2 + cos((m+1)*t)/3
    return wynik

x_wek = [x(t) for t in time]
y_wek = [y(t) for t in time]

plot(x_wek, y_wek, color='orchid')
title("Wykres krzywej parametrycznej")
xlabel("x(t)")
ylabel("y(t)")
grid() #dodaje siatkę w tle
show()