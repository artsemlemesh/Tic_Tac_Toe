# greet, field, def show, def ask(4 checks), def check-win, game cycle(finish)


def greet():
    print('---WELCOME---')
    print('-----to------')
    print('--------TIC--')
    print('---TAC-------')
    print('--------TOE--')
    print('-------------')


greet()

field = [[' '] * 3 for i in range(3)]


def show():
    print()
    print(' | 0 | 1 | 2 |')
    print('--------------')
    for i, line in enumerate(field):
        row = f'{i}| {" | ".join(line)} |'
        print(row)
        print('--------------')
    print()


show()


def ask():
    while True:
        coordinates = input('your turn: ').split()
        if len(coordinates) != 2:
            print('type two coordinates')
            continue

        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):
            print('type numbers')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('coordinates are beyond the range')
            continue

        if field[x][y] != ' ':
            print('the field is occupied')
            continue
        return x, y


ask()


def win_check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_cord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('X has won')
            return True
        if symbols == ['0', '0', '0']:
            print('0 has won')
            return True
    return False

win_check()

greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print('X"s turn')
    else:
        print('0"s turn')

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if win_check():
        break

    if count == 9:
        print('nobody won')
        break
