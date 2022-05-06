def describe():
    print(                          )
    print({"     Приветствие!!!   "})
    print({"---------игра---------"})
    print({"    КРЕСТИКИ-НОЛИКИ   "})
    print({"----------------------"})
    print({" для совершения хода  "})
    print({"введите две координаты"})
    print({" через пробел {X} {Y} "})
    print({"----------------------"})

def draw_board():
    print()
    print()
    print(f"   | 0 | 1 | 2 |")
    print(" " * 2, "-" * 13)
    for i in range(3):
        print(f" {i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print(" " * 2, "-" * 13)
    print()


def enter():
    while True:
        value = input(" введите {x} {y} \n через пробел:   ").split()

        if len(value) != 2:
            print()
            print(" некорректный ввод, введите две координаты !!! ")
            continue

        x, y = value

        if not (x.isdigit()) or not (y.isdigit()):
            print()
            print(" введите числа !!!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print()
            print(" некорректный ввод координаты от 0 до 2 !!! ")
            continue

        if board[x][y] != " ":
            print()
            print(" это поле занято !!!")
            continue

        return x, y


def check_win():
    win_combo = [(board[0][0], board[0][1], board[0][2]),
                 (board[1][0], board[1][1], board[1][2]),
                 (board[2][0], board[2][1], board[2][2]),
                 (board[0][0], board[1][0], board[2][0]),
                 (board[0][1], board[1][1], board[2][1]),
                 (board[0][2], board[1][2], board[2][2]),
                 (board[0][0], board[1][1], board[2][2]),
                 (board[0][2], board[1][1], board[2][0])]

    for i in range(3):
        if win_combo[i][0] == "x" and win_combo[i][1] == "x" and win_combo[i][2] == "x":
            return True
        elif win_combo[i][0] == "O" and win_combo[i][1] == "O" and win_combo[i][2] == "O":
            return True

    for j in range(3):
        if win_combo[0][j] == "x" and win_combo[1][j] == "x" and win_combo[2][j] == "x":
            return True
        elif win_combo[0][j] == "O" and win_combo[1][j] == "O" and win_combo[2][j] == "O":
            return True

    for j in range(3):
        if win_combo[0][0] == "x" and win_combo[1][1] == "x" and win_combo[2][2] == "x":
            return True
        elif win_combo[0][0] == "O" and win_combo[1][1] == "O" and win_combo[2][2] == "O":
            return True

    for j in range(3):
        if win_combo[0][2] == "x" and win_combo[1][1] == "x" and win_combo[2][0] == "x":
            return True
        elif win_combo[0][2] == "O" and win_combo[1][1] == "O" and win_combo[2][0] == "O":
            return True

    return False

describe()
board = [[" "] * 3 for i in range(3)]
token = 0

while True:
    token += 1
    draw_board()

    if token % 2 == 1:
        print(" ходит Х: ")
    else:
        print(" ходит O: ")

    x, y = enter()

    if token % 2 == 1:

        board[x][y] = "x"
    else:

        board[x][y] = "O"

    if check_win():
        draw_board()
        print("  ПОБЕДА!!!")
        print(" конец игры ")
        print("сыграйте еще)))")
        break

    if token == 10:
        print()
        print(" ничья конец игры !!!")
        break
