from random import shuffle

# klasa z wykładu 10:

class TTTBoard:
    def __init__(self, n):
        self.board = [['.'] * n for _ in range(n)]
        self.current = 'O'

    def move(self, i, j, symbol):
        if symbol != self.current:
            return False
        if self.board[i][j] != '.':
            return False
        self.board[i][j] = symbol
        if self.current == 'O':
            self.current = 'X'
        else:
            self.current = 'O'

    def get_winner(self):
        n = len(self.board)
        for symbol in 'OX':
            for row in self.board:
                if row.count(symbol) == n:
                    return symbol
            for i in range(n):
                if [row[i] for row in self.board].count(symbol) == n:
                    return symbol
            if [self.board[i][i] for i in range(n)].count(symbol) == n:
                return symbol
            if [self.board[i][n-i-1] for i in range(n)].count(symbol) == n:
                return symbol
        return None


###########################################################


def jedna_gra(n):
    board = TTTBoard(n)
    pola = [(i, j) for i in range(n) for j in range(n)]
    shuffle(pola)
    # po przetasowaniu wiemy już, w jakiej kolejności będziemy uzupełniać pola

    #teraz zapełniamy pola
    for (i,j) in pola:
        board.move(i,j, board.current)
        # sprawdź czy ktoś już wygrał
        if board.get_winner() != None:
            return board.get_winner()

    return board.get_winner()



def pstwo(n, powtórzenia):
    remisy = 0

    for _ in range(powtórzenia):
        if jedna_gra(n)== None:
            remisy += 1

    result = "P-stwo remisu dla {} powtórzeń gry na planszy {}x{}: {}".format(
        powtórzenia, n, n, remisy/powtórzenia)
    return result


print(pstwo(3, 10000))
print(pstwo(4, 10000))




