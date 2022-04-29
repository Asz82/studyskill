board = [[" "] * 3 for i in range(3)]


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
    x, y = map(int,input(" введите {x} {y} \n через пробел  " "\n").split())
    return x, y


draw_board()


while True:
    x,y = enter()
    board[x][y] = "N"
    draw_board()
    continue
