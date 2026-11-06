import math


# zadanie 1
print("Zadanie 1")
n = str(input("Podaj liczbę naturalną n: "))
szóstki = n.count("6")
trójki = n.count("3")

if szóstki ==2 or trójki >= 3:
    print("W zapisie dziesiętnym liczby n występują dwie szóstki lub"
          " co najmniej trzy trójki")
else: print("W zapisie dziesiętnym liczby n NIE występują dwie szóstki lub"
          " co najmniej trzy trójki")



## rozwiązanie bez funkcji n.count:

n = str(input("Podaj liczbę naturalną n: "))

trójki = 0
szóstki = 0

for c in n:
    if c == '3': trójki += 1
    if c == '6': szóstki += 1



# zadanie 2
print()
print("Zadanie 2")
n = int(input("Podaj liczbę naturalną n: "))
x = float(input("Podaj liczbę rzeczywistą x: "))

suma = 0
for k in range(0, n+1):
    suma = suma + ((-1)**k)*(x**(2*k))/math.factorial(2*k)

print(suma)

# pierwsze n+1 wyrazów rozwinięcia w szereg Taylora funkcji cos(x).




# zadanie 3
print()
print("Zadanie 3")
print(f"{'m/s':<10} {'mph':<10} {'kable/tydzień'}")

for ms in range(0, 1001, 10):
    mph = ms*2.2369
    kable = (ms * 604800) / 185.2
    print(f"{ms:<10} {mph:<10.2f} {kable:<10.2f}")




# zadanie 4
print()
print("Zadanie 4")
ile = 0
suma = 0

while True:
    x = input("Podaj liczbę x albo 'end': ")
    if x== "end":
        break
    else:
        ile = ile+1
        suma = suma + float(x)
        #zakładamy, że jesli użytkownik nie wpisał end, to podał liczbę

if ile==0: print("Nie podano żandej wartości")
else:
    średnia = suma/ile
    print("Średnia arytmetyczna wpisanych liczb to: ", średnia)
