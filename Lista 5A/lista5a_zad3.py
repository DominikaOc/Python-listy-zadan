def głębokie_jezioro(board, i, j):
    #pole musi być wodne:
    if board[i][j] != '=': return False

    #gdy istnieje sąsiad, który nie jest wodny, to zwróć False
    n = len(board)
    for col in range(max(j-1, 0), min(j+2, n)):
        for row in range(max(i-1,0), min(i+2, n)):
            if board[row][col] != '=': return False

    return True

# można zrobić funkcję, która zwraca listę sąsiadów dla konkretnego pola

#-----------------------------------------------------------------------------------


def płytkie_jezioro(board, i, j):
    #pole musi być wodne:
    if board[i][j] != '=': return False
    #nie jest głębokim jeziorem:
    if głębokie_jezioro(board, i, j): return False

    #sąsiaduje z głębokim jeziorem:
    n = len(board)
    #gdy znajdziemy choć jednego takiego sąsiada, zwróć True
    for col in range(max(j - 1, 0), min(j + 2, n )):
        for row in range(max(i - 1, 0), min(i + 2, n )):
            if głębokie_jezioro(board, row, col): return True

    return False


#------------------------------------------------------------------------------------



def gęstwina(board, i, j):
    #pole musi być zalesione:
    if board[i][j] != '&': return False

    #liczymy, ile ma zalesionych sąsiadów
    n = len(board) #liczba list, czyli wierszy
    zalesione = 0
    for col in range(max(j-1, 0), min(j+2, n)):
        for row in range(max(i-1,0), min(i+2, n)):
            if board[row][col] == '&': zalesione = zalesione+1

    zalesione = zalesione - 1
    #w pętli było też pole [i][j], a chcemy tylko sąsiadujące z nim pola
    return (zalesione >=5)


#-----------------------------------------------------------------------------------


def zamieszkiwalne(board, i, j):
    #pole musi być trawiaste:
    if board[i][j] != '.': return False

    #liczymy, ile jego sąsiadów jest płytkim jeziorem i polem trawiastym

    trawiaste =  0
    płytkie = 0
    n = len(board)
    for col in range(max(j - 1, 0), min(j + 2, n)):
        for row in range(max(i - 1, 0), min(i + 2, n)):
            if board[row][col] == '.': trawiaste = trawiaste + 1
            if płytkie_jezioro(board, row, col): płytkie = płytkie + 1
            if gęstwina(board, row, col): return False
            #gdy któryś jest gęstwiną, to pole nie może być zamieszkiwalne

    trawiaste = trawiaste - 1
    return( płytkie >=1 and trawiaste >=1)


#----------------------------------------------------------------------------------


def has_habitable_field(board):
    n = len(board)
    for col in range(0, n):
        for row in range(0, n):
            if zamieszkiwalne(board, row, col): return True

    return False


#-------------------------------- Testy---------------------------------------------

plansza = [["=", "=", ".", "&", "&"],
           ["=", "=", ".", "&", "&"],
           ["=", "=", ".", "&", "&"],
           ["=", ".", "&", "&", "."],
           ["=", ".", "&", "&", "."]]

#print(gęstwina(plansza, 1, 4)) #True
#print(gęstwina(plansza, 0, 0)) #False

#print(głębokie_jezioro(plansza, 0, 0)) #True
#print(głębokie_jezioro(plansza, 4, 4)) #False

#print(płytkie_jezioro(plansza, 1,1)) #True
#print(płytkie_jezioro(plansza, 1,2)) #False

#print(zamieszkiwalne(plansza, 3,1)) #True
#print(zamieszkiwalne(plansza, 3, 3)) #False

print(has_habitable_field(plansza)) #True