from time import sleep, perf_counter

#---------------- zadanie 1------------------------------

def Fibonacci_iter(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        pp = 0 # a_{n-2}
        p = 1 # a_{n-1}
        for i in range(2, n+1):
            a_i = pp + p
            #przesuwamy indeksy
            pp = p
            p = a_i
		
	        #p, pp = p+pp, p
        return a_i


#print(Fibonacci_iter(71))

#--------------------------------------------------------------#

def Fibonacci_rek(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci_rek(n-1) + Fibonacci_rek(n-2)

#print(Fibonacci_rek(10))

#------------------------------------------------------------#

def Fibonacci_wzór(n):
    phi = (1 + 5**0.5)/2
    if n == 0: return 0
    elif n == 1: return 1
    else: return int( (phi**n)/5**0.5 + 0.5 )

#print(Fibonacci_wzór(71))

#----------------------------------------------------------------#

n = 2
while True:
    if Fibonacci_iter(n) == Fibonacci_wzór(n):
        n = n+1
    else:
        print(n)
        break


#-----------------zadanie 2--------------------------------------#

# Funkcja z wykładu zwracająca NWD(a,b) - wersja iteracyjna
def gcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)



def simplify(p,q):
    # q' dodatnie
    if q<0:
        q = q*(-1)
        p = p*(-1)

    # ułamek nieskracalny:
    nwd = gcd_iter(p,q)
    return (p//nwd ,q//nwd)

print(simplify(10, -40))


#----------------zadanie 3-----------------------------------------#

#Funkcja binom z wykładu - liczy symbol dwumianowy:
def binom(n, k):
    if k in (0, n):
        return 1
    return binom(n - 1, k - 1) + binom(n - 1, k)
    


def binom_max(t):
    czas = 0
    n = -1
    #print(f"{'n':<10}", f"{'t':<10}")
    while czas < t:
        n = n + 1
        t0 = perf_counter()
        binom(n, n//2)
        t1 = perf_counter()
        czas = t1 - t0
        #print(f"{n:<10}", f"{czas:<10.4}")

    return n

def tabelka(n):
    print(f"{'n':<10}", f"{'t':<10}")
    k = 0
    while k <= n:
        t0 = perf_counter()
        binom(k, k // 2)
        t1 = perf_counter()
        czas = t1 - t0
        print(f"{k:<10}", f"{czas:<10.4}")
        k = k + 1
    return None

#print(binom_max(3))
n = binom_max(3)
#tabelka(n)

#-----------------zadanie 4-------------------------------------#

def avg_even_indices(lst):
    ile = len(lst)
    if ile == 0: return 0
    else:
        suma = 0
        ile_parz = 0
        for i in range(0, ile, 2):
            suma = suma + lst[i]
            ile_parz = ile_parz + 1

        return suma/ile_parz

#print(avg_even_indices([]))
