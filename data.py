import requests as rq

def showListGame(game_name, game_price):
    c = 0
    for i in game_name:
        print(str(c+1) + '. ', i, game_price[c])
        c += 1
        
    
    ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
    ┃   List Game      ┃  Lowest Price    ┃
    ┡━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛
    
    │                  │                  │
    └──────────────────┴──────────────────┘

class Data:
    store_data = rq.get('https://www.cheapshark.com/api/1.0/stores').json()

    game_id = []
    game_name = []
    game_price = []
    store_name = []

    def __init__(self, gameSeach):
        self.game_data = rq.get('https://www.cheapshark.com/api/1.0/games?title=' + gameSeach).json()

        for i in self.store_data:
            self.store_name.append(i['storeName'])

        for i in self.game_data:
            self.game_id.append(i['gameID'])
            self.game_name.append(i['external'])
            self.game_price.append(i['cheapest'])
