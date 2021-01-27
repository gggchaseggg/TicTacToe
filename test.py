class player:
    
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

first_player = player('john','x')

print ("{} выиграл".format(first_player.name))