from math import sin, cos, acos, pi

# zadanie 1
print("Zadanie 1")
def count_punctuation_marks(s):
    ile = (s.count(",") + s.count(".") + s.count(";")+ s.count(":")
           + s.count("?") + s.count("!"))
    return ile

napis = str(input("Podaj napis: "))
print("Liczba znaków interpunkcyjnych to: ", count_punctuation_marks(napis))




# zadanie 2
print()
print("Zadanie 2")
def is_lucky(n):
    n = str(n)
    siódemki = n.count("7")
    if siódemki>0: return True
    else: return False

nn = int(input("Podaj dodatnią liczbę naturalną n: "))
if is_lucky(nn): print("Liczba jest szczęśliwa :)")
else: print("Liczba nie jest szczęśliwa :(")




def is_semilucky(n):
    for i in range(1, n+1):
        if n%i == 0 and is_lucky(i): return True

    return False

liczba = int(input("Podaj liczbę naturalną dodatnią: "))
if is_semilucky(liczba): print("Liczba ", liczba, " jest półszczęśliwa")
else: print("Liczba ", liczba, " nie jest półszczęśliwa")



def next_semilucky(n):
    i = n+1
    while True:
        if is_semilucky(i): return i
        else: i = i+1

print(next_semilucky(7))



def print_semilucky(k):
    ile = 0
    i = 1
    while ile<k:
        if is_semilucky(i):
            ile = ile+1
            print(i)
        i = i+1
    return None

print_semilucky(10)




# zadanie 3
print()
print("Zadanie 3")
def great_circle_distance(phi1, lambda1, phi2, lambda2):
    #zamiana stopni na radiany:
    phi1 = phi1*pi/180
    lambda1 = lambda1*pi/180
    phi2 = phi2*pi/180
    lambda2 = lambda2*pi/180
    d = 6371.01*acos( sin(phi1)*sin(phi2) + cos(phi1)*cos(phi2)*cos(lambda1 - lambda2))
    print(f"{d:.3f}")
    return None

#odległość między Wrocławiem a Tromso
great_circle_distance(51, 17, 69, 19)

