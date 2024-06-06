import time

SIZE = 9
EMPTY = 0
steps = 0  # Variabel global untuk melacak jumlah langkah
nodes_created = 0  # Variabel global untuk melacak jumlah simpul yang dibuat

def main():
    global steps, nodes_created  # Menggunakan variabel global
    sudoku_string = input("Please enter a Sudoku string: ")
    sudoku = initialize_sudoku(sudoku_string)

    start_time = time.time()
    solve_sudoku(sudoku)
    end_time = time.time()

    print_sudoku(sudoku)
    print("Execution time: ", end_time - start_time, "seconds")
    print("Total steps:", steps)
    print("Total nodes created:", nodes_created)

def initialize_sudoku(sudoku_string):
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]
    index = 0
    for i in range(SIZE):
        for j in range(SIZE):
            sudoku[i][j] = int(sudoku_string[index])
            index += 1
    return sudoku

def solve_sudoku(sudoku):
    global steps, nodes_created  # Menggunakan variabel global
    row, col = [0], [0]  # pakai list untuk menyimpan value baris dan kolom
    steps += 1  # Melacak jumlah langkah

    if not cariKosong(sudoku, row, col):
        return True  # Sudoku is solved

    num = 1
    while num <= SIZE:
        if valid(sudoku, row[0], col[0], num):
            sudoku[row[0]][col[0]] = num
            nodes_created += 1  # Menghitung jumlah simpul yang dibuat

            if solve_sudoku(sudoku):
                return True

            sudoku[row[0]][col[0]] = EMPTY  # Backtrack
        num += 1

    return False  # tidak ada solusi untuk kotak ini

def cariKosong(sudoku, row, col):
    i = 0
    while i < SIZE:
        j = 0
        while j < SIZE:
            if sudoku[i][j] == EMPTY:
                row[0], col[0] = i, j
                return True
            j += 1
        i += 1
    return False

def valid(sudoku, row, col, num):
    return not (cekBaris(sudoku, row, num) or 
                cekKolom(sudoku, col, num) or 
                cekMiniGrid(sudoku, row - row % 3, col - col % 3, num))

def cekBaris(sudoku, row, num):
    j = 0
    while j < SIZE:
        if num == sudoku[row][j]:
            return True
        j += 1
    return False

def cekKolom(sudoku, col, num):
    i = 0
    while i < SIZE:
        if num == sudoku[i][col]:
            return True
        i += 1
    return False

def cekMiniGrid(sudoku, start_row, start_col, num):
    i = start_row
    while i < start_row + 3:
        j = start_col
        while j < start_col + 3:
            if num == sudoku[i][j]:
                return True
            j += 1
        i += 1
    return False

def print_sudoku(sudoku):
    i = 0
    while i < SIZE:
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        j = 0
        while j < SIZE:
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")
            j += 1
        i += 1

main()
