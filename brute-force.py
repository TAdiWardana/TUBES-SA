def solveSudoku(A):
    S = [row[:] for row in A]  # Clone A to S

    def initial(A, S):
        valid = True
        i = 0
        while i < 9 and valid:
            j = 0
            while j < 9 and valid:
                if A[i][j] != 0 and A[i][j] != S[i][j]:
                    valid = False
                j += 1
            i += 1
        return valid

    def valid(S):
        for i in range(9):
            row = [0] * 9
            col = [0] * 9
            for j in range(9):
                if S[i][j] != 0:
                    if row[S[i][j] - 1] == 1:
                        return False
                    row[S[i][j] - 1] = 1
                if S[j][i] != 0:
                    if col[S[j][i] - 1] == 1:
                        return False
                    col[S[j][i] - 1] = 1
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [0] * 9
                for k in range(3):
                    for l in range(3):
                        if S[i + k][j + l] != 0:
                            if box[S[i + k][j + l] - 1] == 1:
                                return False
                            box[S[i + k][j + l] - 1] = 1
        return True

    def solve(S):
        for i in range(9):
            for j in range(9):
                if S[i][j] == 0:
                    for num in range(1, 10):
                        S[i][j] = num
                        if initial(A, S) and valid(S) and solve(S):
                            return True
                        S[i][j] = 0
                    return False
        return True
    
    if solve(S):
        return S
    else:
        return None

# Contoh penggunaan
A = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_sudoku = solveSudoku(A)
if solved_sudoku:
    for row in solved_sudoku:
        print(row)
else:
    print("No solution found")