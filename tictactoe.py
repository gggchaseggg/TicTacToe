import keyboard
import time


class player:
    
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol


def menu():
    print('{:^30}'.format('МЕНЮ'))
    print('{:<30}'.format('1-Играть'))
    print('{:<30}'.format('2-Настройки'))
    print('{:<30}'.format('3-Выход'))
    print('{:^30}'.format('CBM Programming.2021'))

    menu_item = cheak_key_menu()
    menu_item()


def cheak_key_menu():
    while not (keyboard.is_pressed('1') or keyboard.is_pressed('2') or keyboard.is_pressed('3')):
        pass
    else:
        if keyboard.is_pressed('1'):
            menu_item = game()
        elif keyboard.is_pressed('2'):
            menu_item = settings()
        elif keyboard.is_pressed('3'):
            menu_item = exit_f()
    time.sleep(0.5)
    return menu_item


def cheak_key_settings():
    while not (keyboard.is_pressed('1') or keyboard.is_pressed('2')):
        pass
    else:
        if keyboard.is_pressed('1'):
            v_input = input_cell
        elif keyboard.is_pressed('2'):
            v_input = cheak_key_game
    time.sleep(0.5)
    return v_input


def game():
    tictactoe = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    
    first_player,second_player = player_info()

    for i in range(9):
        if i % 2 == 0:
            symbol = first_player.symbol
            name = first_player.name
        elif i % 2 != 0:
            symbol = second_player.symbol
            name = second_player.name
    
        print_table(tictactoe)
        time.sleep(0.5)
        print("{} выберете ячейку...".format(name))
        cheak_key_game(tictactoe,symbol)
        flag = find_winner(tictactoe,first_player.name,second_player.name)
        if flag == True:
            print_table(tictactoe)
            break


def settings():
    print('{:^30}'.format('НАСТРОЙКИ'))
    print('{:<30}'.format('Выберете тип ввода ячеек:'))
    print('{:<30}'.format('1-Ввод с клавиатуры'))
    print('{:<30}'.format('2-По нажатию клавиши'))

    setting_item = cheak_key_settings()
    setting_item()


def exit_f():
    print('Подтвердите выход нажатием Esc...')
    while not (keyboard.is_pressed('esc')):
        continue
    else:
        if keyboard.is_pressed('esc'):
            exit
    time.sleep(0.5)

def player_info():
    name1 = input("Имя 1 игрока: ")
    symbol1 = int(input("Символ 1 игрока: "))
    first_player = player(name1,symbol1)

    name2 = input("Имя 2 игрока: ")
    symbol2 = int(input("Символ 2 игрока: "))
    second_player = player(name2,symbol2)

    return first_player, second_player


def input_cell(table):
    cell = int(input("Введите номер ячейки: "))
    value = int(input("Введите значение: "))
    if cell == 1:
        table[0][0] = value
    elif cell == 2:
        table[0][1] = value
    elif cell == 3:
        table[0][2] = value
    elif cell == 4:
        table[1][0] = value
    elif cell == 5:
        table[1][1] = value
    elif cell == 6:
        table[1][2] = value
    elif cell == 7:
        table[2][0] = value
    elif cell == 8:
        table[2][1] = value
    elif cell == 9:
        table[2][2] = value

    return table


def print_table(table):
    for i in range (3):
        for j in range(3):
            print (table[i][j], end = '\t')
        print ('\n')


def find_winner(table,name1,name0):
    flag = False
    if (table[0][0]==table[0][1]==table[0][2]==1 or 
        table[1][0]==table[1][1]==table[1][2]==1 or
        table[2][0]==table[2][1]==table[2][2]==1 or
        table[0][0]==table[1][0]==table[2][0]==1 or 
        table[0][1]==table[1][1]==table[2][1]==1 or
        table[0][2]==table[1][2]==table[2][2]==1 or
        table[0][0]==table[1][1]==table[2][2]==1 or
        table[0][2]==table[1][1]==table[2][0]==1):
        print("{}, победил!".format(name1))
        flag = True
    elif (table[0][0]==table[0][1]==table[0][2]==0 or 
        table[1][0]==table[1][1]==table[1][2]==0 or
        table[2][0]==table[2][1]==table[2][2]==0 or
        table[0][0]==table[1][0]==table[2][0]==0 or 
        table[0][1]==table[1][1]==table[2][1]==0 or
        table[0][2]==table[1][2]==table[2][2]==0 or
        table[0][0]==table[1][1]==table[2][2]==0 or
        table[0][2]==table[1][1]==table[2][0]==0):
        print("{}, победил!".format(name0))
        flag = True
    elif -1 in table[0] or -1 in table[1] or -1 in table[2]:
        return flag
    else:
        print("\nНичья!\n")
        flag = True
    return flag


def cheak_key_game(table,symbol):
    while not (keyboard.is_pressed('1') or keyboard.is_pressed('2') or keyboard.is_pressed('3') 
    or keyboard.is_pressed('4') or keyboard.is_pressed('5') or keyboard.is_pressed('6') 
    or keyboard.is_pressed('7') or keyboard.is_pressed('8') or keyboard.is_pressed('9')):
        pass
    else:
        if keyboard.is_pressed('1'):
            table[0][0] = symbol
        elif keyboard.is_pressed('2'):
            table[0][1] = symbol
        elif keyboard.is_pressed('3'):
            table[0][2] = symbol
        elif keyboard.is_pressed('4'):
            table[1][0] = symbol
        elif keyboard.is_pressed('5'):
            table[1][1] = symbol
        elif keyboard.is_pressed('6'):
            table[1][2] = symbol
        elif keyboard.is_pressed('7'):
            table[2][0] = symbol
        elif keyboard.is_pressed('8'):
            table[2][1] = symbol
        elif keyboard.is_pressed('9'):
            table[2][2] = symbol
    return table

menu()