class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5


    def __neg__(self):
        return Complex(-self.real, -self.imag)


    def __str__(self):
        if self.imag >=0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"


    # czy ja mogę założyć, że other_num też jest obiektem mojej klasy Complex? Tak
    def __add__(self, other_num):
        return Complex(self.real + other_num.real, self.imag + other_num.imag)


    def __sub__(self, other_num):
        return Complex(self.real - other_num.real, self.imag - other_num.imag)


    def __mul__(self, other_num):
        a = self.real
        b = self.imag
        c = other_num.real
        d = other_num.imag
        return Complex(a*c - b*d, a*d + b*c)


    # sprzężenie: a+bi -> a-bi
    def conjugate(self):
        return Complex(self.real, -self.imag)




    def __truediv__(self, other_num):

        if other_num.real ==0 and other_num.imag ==0:
            return print("Nie można dzielić przez 0")

        licznik = self.__mul__(other_num.conjugate())  #mnożymy przez sprzężenie mianownika
        mianownik = other_num.__mul__(other_num.conjugate())  # to będzie liczba rzeczywista
        mianownik = mianownik.real  # pozbywamy się "0i"
        licznik.real = licznik.real / mianownik
        licznik.imag = licznik.imag / mianownik

        return licznik


    def __eq__(self, other_num):
        if self.real == other_num.real and self.imag == other_num.imag:
            return True

        return False





c1 = Complex(3,2)
c2 = Complex(1, -1)
c3 = c1.__truediv__(c2)
print(c3)



