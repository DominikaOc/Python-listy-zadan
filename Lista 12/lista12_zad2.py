import numpy as np

# board to tablica numpy 3x3

def ttt_result(board):
    lines = (
          [board[i, :] for i in range(3)] #wiersze
        + [board[:, j] for j in range(3)] #kolumny
        + [board[i, i] for i in range(3)] # przekątna
        + [board[i, 2-i] for i in range(3)] #druga przekątna

    )
    for line in lines:
        #print(line =='O')
        if np.sum(line == 'O') == 3: return 1
        if np.sum(line == 'X') == 3: return 2

    return 0


board = np.array([["X", "O", "O"], [".", "O", "X"], ["X", "O", "."]])

#print(ttt_result(board))

#####
h = np.array([board[i, 2-i] for i in range(3)])
print(h)
print(h=='O')
print(np.sum(h == 'O'))