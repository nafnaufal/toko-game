from data import *
import requests as rq

loop = True
#main loop
while loop:

    search = input('Enter game name: ')
    session = Data(search)

    select = input('Pilih nomor game :')
    sel_game = rq.get('https://www.cheapshark.com/api/1.0/games?id='+ str(session.game_id[int(select)-1])).json()

    counter = 0
    for i in sel_game['deals']:
        print(counter + 1, '.', session.store_name[int(i['storeID'])-1])
        print(sel_game['deals'][counter]['price'])
        print(sel_game['deals'][counter]['retailPrice'])
        print("Hemat = ", float(sel_game['deals'][counter]['retailPrice']) - float(sel_game['deals'][counter]['price']))
        redic = "https://www.cheapshark.com/redirect?dealID="+sel_game['deals'][counter]['dealID']
        print(redic)
        counter += 1
    
    del session

    ulang = input('Ulang?(Y/N)')
    if ulang == 'Y':
        loop = True
    elif ulang == 'N':
        loop = False
    else:
        loop = False
        print('Input salah')