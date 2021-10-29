import random

def greet():
    print('-----------------------------')
    print("    Игра крестики-нолики     ")
    print('-----------------------------')
    print("       Формат ввода:")
    print("     XY или X Y или X,Y")
    print("     X - номер строки,")
    print("     Y - номер столбца")
    print("-----------------------------")
    print("   1.  Игра с компьютером    ")
    print("   2.  Игра в двоём          ")
    print("-----------------------------")

def ask_name():
    userName = None
    while userName is None:
        numStr = input("\n Выберете режим игры [1 или 2]:  ")
        if numStr.isdigit():
            if int(numStr) == 1:
                userName = {'X': input(" Введите своё имя:   "),
                            'O': "Comp"}
            elif int(numStr) == 2:
                userName = {'X': input(" Введите имя Первого игрока: "),
                            'O': input(" Введите имя Второго игрока: ")}
        else:
            print(" Вы ввели некорректное число!")
            continue

    return userName


def show_field(f):
    num = '  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")


def users_input(f, userName):
    if userName.count('Comp'):
        print("Play with Comp!!!")
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while f[x][y] != '-':
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        return x, y

    else:
        while True:
            place = input(f"\n Ходит {userName}. Введите координаты:")
            if len(place) > 3 or not(place[0].isdigit() and place[1].isdigit()):
                print('Введите числа от 0 до 2')
                continue
            if len(place) == 2:
                place = [place[0], place[1]]
            elif len(place) == 3:
                place = place.split(place[1])

            x, y = map(int, place)
            if not (x >= 0 and x < 3 and y >= 0 and y < 3):
                print('Вышли за границы поля!')
                continue

            if f[x][y] != '-':
                print('Клетка занята')
                continue
            break
        return x, y


def win_position(f, user):
    f_list = []
    for i in f:
        f_list += i

    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False


def start():
    count = 0
    greet()
    userName = ask_name()
    fld = [['-'] * 3 for _ in range(3)]
    while True:
        show_field(fld)
        if count % 2 == 0:
            user = 'X'
        else:
            user = 'O'
        if count < 9:
            x, y = users_input(fld, userName.get(user))
            fld[x][y] = user
        elif count == 9:
            print('Ничья')
            break
        if win_position(fld, user):
            print(f"{userName.get(user)} выйграл!!!")
            show_field(fld)
            break
        count += 1

#
start()
