#zadanie 1
a = float(input("Podaj dodatnią liczbę rzeczywistą a: "))
P = (a**2) * (3**0.5)
V = (a**3)*(2**0.5)/12
print("Pole powierzchni czworościanu foremnego o krawędzi a wynosi: ", P)
print("Natomiast objętość takiego czworościanu to: ", V)


# zadanie 2
xa = float(input("Podaj niezerową liczbę rzeczywistą x_a: "))
xb = float(input("Podaj niezerową liczbę rzeczywistą x_b: "))
ya = float(input("Podaj niezerową liczbę rzeczywistą y_a: "))
yb = float(input("Podaj niezerową liczbę rzeczywistą y_b: "))

if xa*ya>=0 and xb*yb>=0:
    print("Punkty (x_a,x_b) i (y_a,y_b) są w tej samej ćwiartce.")
else:
    print("Punkty (x_a,x_b) i (y_a,y_b) nie są w tej samej ćwiartce.")


# zadanie 3
x = float(input("Podaj dodatnią kwotę dochodu x: "))
if x<=8000:
    podatek = 0
elif x<=34500:
    podatek = 0.1*(x-8000)
else: podatek = 0.24*(x-34500) + 0.1*(34500-8000)

print("Podatek dla dochodu x wynosi: ", podatek)


# zadanie 4
n = int(input("Podaj dodatnią liczbę naturalną n: "))
ilość = 0
for i in range(3,n):
    if n%i==0 and i%3==0:
        print(i)
        ilość = ilość+1

print("Liczba n=", n, "ma", ilość, "naturalnych dzielników podzielnych przez 3.")
