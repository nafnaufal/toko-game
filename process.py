import requests as rq


search = input('Enter game name: ')

store_data = rq.get('https://www.cheapshark.com/api/1.0/stores').json()
game_data = rq.get('https://www.cheapshark.com/api/1.0/games?title=' + search).json()

game_id = []
game_name = []
game_price = []
store_name = []

for i in store_data:
    store_name.append(i['storeName'])

for i in game_data:
    game_id.append(i['gameID'])
    game_name.append(i['external'])
    game_price.append(i['cheapest'])

c = 0
for i in game_name:
    print(str(c+1) + '. ', i, game_price[c])
    c += 1

select = input('Pilih nomor game :')

sel_game = rq.get('https://www.cheapshark.com/api/1.0/games?id='+ str(game_id[int(select)-1])).json()

c2 = 0

for i in sel_game['deals']:
    print(c2 + 1)
    print(store_name[int(i['storeID'])-1])
    print(sel_game['deals'][c2]['price'])
    print(sel_game['deals'][c2]['retailPrice'])
    print("Hemat = ", float(sel_game['deals'][c2]['retailPrice']) - float(sel_game['deals'][c2]['price']))
    redic = "https://www.cheapshark.com/redirect?dealID="+sel_game['deals'][c2]['dealID']
    print(redic)
    c2 += 1
