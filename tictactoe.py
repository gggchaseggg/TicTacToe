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

def find_winner(table):
    flag = False
    if (table[0][0]==table[0][1]==table[0][2]==1 or 
        table[1][0]==table[1][1]==table[1][2]==1 or
        table[2][0]==table[2][1]==table[2][2]==1 or
        table[0][0]==table[1][0]==table[2][0]==1 or 
        table[0][1]==table[1][1]==table[2][1]==1 or
        table[0][2]==table[1][2]==table[2][2]==1 or
        table[0][0]==table[1][1]==table[2][2]==1 or
        table[0][2]==table[1][1]==table[2][0]==1):
        print("Играющий за 1, победил!")
        flag = True
    elif (table[0][0]==table[0][1]==table[0][2]==0 or 
        table[1][0]==table[1][1]==table[1][2]==0 or
        table[2][0]==table[2][1]==table[2][2]==0 or
        table[0][0]==table[1][0]==table[2][0]==0 or 
        table[0][1]==table[1][1]==table[2][1]==0 or
        table[0][2]==table[1][2]==table[2][2]==0 or
        table[0][0]==table[1][1]==table[2][2]==0 or
        table[0][2]==table[1][1]==table[2][0]==0):
        print("Играющий за 0, победил!")
        flag = True
    elif -1 in table[0] or -1 in table[1] or -1 in table[2] >= 5:
        return flag
    else:
        print("\nНичья!\n")
    return flag

tictactoe = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

while True:
    print_table(tictactoe)
    input_cell(tictactoe)
    flag = find_winner(tictactoe)
    if flag == True:
        break