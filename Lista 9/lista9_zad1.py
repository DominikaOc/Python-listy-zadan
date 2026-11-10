class Player:

    def __init__(self, money=1000, houses=0, tokens=1):
        if tokens < 0 or houses < 0 or money < 0:
            raise ValueError()
        self.money = money
        self.houses = houses
        self.tokens = tokens

    def add_tokens(self, tokens = 1):
        if tokens < 0:
            raise ValueError("Liczba dodanych tokenów musi być większa od 0")
        self.tokens += tokens


    def change_money(self, money):
        if self.money + money < 0: raise ValueError("Gracz nie może mieć ujemnej ilości pieniędzy")

        self.money += money


    def build_houses(self, n=1):
        if n<0:
            raise ValueError("Liczba domków musi być nieujemna")
        if self.money < 400*n:
            raise ValueError(f"Gracz nie ma wystarczająco dużo pieniędzy, aby zbudować {n} domków")
        if self.tokens < n:
            raise ValueError(f"Gracz nie ma wystarczająco dużo tokenów, aby zbudować {n} domków")

        self.houses += n
        self.money -= 400*n
        self.tokens -= n


    def __str__(self):
        return f"Player(money={self.money}, houses={self.houses}, tokens={self.tokens})"


gracz1 = Player(1000, 1, 2)
print(gracz1)
gracz1.add_tokens(3)
print(gracz1.tokens)
gracz1.change_money(200)
print(gracz1.money)
gracz1.build_houses(2)
print(gracz1.houses)
print(gracz1.money)
