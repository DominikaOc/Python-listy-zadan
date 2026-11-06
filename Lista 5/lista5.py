#import statistics as st

# zadanie 1

def counting_down_list(n):
    lst = []
    for i in range(n):
        lst = [i]*i + lst
    return lst

#print(counting_down_list(4))

def counting_down_list2(n):
    return[ i for i in range(n-1, 0, -1) for j in range(i) ]

#print(counting_down_list2(4))


# zadanie 2
def analyze_data(lst):
    ile = len(lst)
    lst = lst.sort()

    if ile < 2: return None
    if ile%2 == 0:
        # w przypadku parzystych //, żeby w wyniku był int a nie float
        # teoretycznie /2 też całkowite, ale zwraca float .0
        mediana = (lst[ile//2 - 1] + lst[ile//2])/2
    else: mediana = lst[ile//2]

    rozstęp = max(lst) - min(lst)
    średnia = sum(lst)/ile
    # tworzę wektor pomocniczy:
    nowa_lista = [(i-średnia)**2 for i in lst]
    s = ( sum(nowa_lista)/(ile-1) )**0.5

    return(min(lst), max(lst), mediana, rozstęp, średnia, s)

lista = [1,2,3,7]
#print(st.stdev(lista))
#print(analyze_data(lista))


# zadanie 3

def remove_guests(guest_list, name):
    ile = len(guest_list)
    # idę od końca listy i usuwam odpowiednich gości
    # po usunięciu nie zmieniają się indeksy wcześniejszych gości na liście
    # pętla do -1, żeby 0 też wzięła pod uwagę (indeksy od 0 do ile-1)
    for i in range(ile-1, -1, -1):
        if guest_list[i][1] == name: del guest_list[i]

    return guest_list

goście = [ ( "Anna" , "Kowalska" ), ( "Maciej", "Wilk" ),
( "Tomasz" , "Nowak" ), ( "Piotr" , "Wilk" ) ]

#print(goście)
#print(remove_guests(goście, "Wilk"))


# zadanie 4

def ttt_result(board):
    lines = (
        board #wiersze
        + [[board[i][i] for i in range(3)]] #przekątna
        + [[board[i][2-i] for i in range(3)]] #druga przekątna
        + [[board[i][j] for i in range(3)] for j in range(3)] #kolumny
    )
    for line in lines:
        if line == ['O']*3: return 1
        if line == ['X']*3: return 2

    return 0

board = [["X", "O", "O"], [".", "O", "X"], ["X", "O", "."]]
print(ttt_result(board))

lines = board  + [[board[i][i] for i in range(3)]]  + [[board[i][2 - i] for i in range(3)]]+ [[board[i][j] for i in range(3)] for j in range(3)]
#powyższe lines działa tak, jak lines w funkcji.
# #Okragłe nawiasy gdy chcemy przenieść wyrażenie na kilka linijek