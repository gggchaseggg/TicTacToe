import keyboard
import time

class player:
    
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol


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


def cheak_key(table,symbol):
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
    time.sleep(1)
    return table

tictactoe = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

name1 = input("Имя 1 игрока: ")
symbol1 = int(input("Символ 1 игрока: "))
first_player = player(name1,symbol1)

name2 = input("Имя 2 игрока: ")
symbol2 = int(input("Символ 2 игрока: "))
second_player = player(name2,symbol2)

for i in range(9):
    
    if i % 2 == 0:
        symbol = first_player.symbol
        name = first_player.name
    elif i % 2 != 0:
        symbol = second_player.symbol
        name = second_player.name
    
    print_table(tictactoe)
    print("{} выберете ячейку...".format(name))
    cheak_key(tictactoe,symbol)
    flag = find_winner(tictactoe,first_player.name,second_player.name)
    if flag == True:
        print_table(tictactoe)
        break