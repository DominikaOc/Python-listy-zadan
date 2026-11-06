# zadanie 1
def first_common_character(s1, s2):
    for znak1 in s1:
        for znak2 in s2:
            if znak1 == znak2: return znak1
    return None

str1 = input("Napis nr 1: ")
str2 = input("Napis nr 2: ")
print(first_common_character(str1, str2))


# zadanie 2

def sum_digits(n):
    suma = 0
    while n > 0:
        suma = suma + n%10 # dodajemy dzielenie modulo przez 10, czyli ostatnią cyfrę
        n = n // 10 # obcinamy ostatnią cyfrę
    return suma

m = int(input("Policzmy sumę cyfr wpisanej liczby: "))
print(sum_digits(m))


def is_divisible3(n):
    if n <10:
        return n in {0, 3, 6, 9}
    else:
        n = sum_digits(n)
        return is_divisible3(n)

n = int(input("Sprawdź, czy podana liczba jest podzielna przez 3: "))
print(is_divisible3(n))



# zadanie 3
def print_conversion_table(start, step, count):

    print(f"{'m/s':<10} {'mph':<10} {'kable/tydzień'}")

    for ms in range(start, start + step*(count-1) + 1, step):
        mph = ms * 2.2369
        kable = (ms * 604800) / 185.2
        print(f"{ms:<10} {mph:<10.2f} {kable:<10.2f}")

    return None

start = int(input("Podaj wartość startową: "))
step = int(input("Podaj krok: "))
count = int(input("Ile wartości ma być: "))
print_conversion_table(start, step, count)