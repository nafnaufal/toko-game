from process import *
import requests as rq, os

loop = True
#main loop
while loop:
    os.system('cls')

    search = input('Enter game name: ')
    session = Data(search)

    showListGame(session.game_name, session.game_price)

    select = input('Pilih nomor game :')
    sel_game = rq.get('https://www.cheapshark.com/api/1.0/games?id='+ str(session.game_id[int(select)-1])).json()
    

    showStore(sel_game, session.store_name, session.game_name[int(select)-1])

    ulang = input('Ulang?(Y/N)')
    if ulang == 'Y' or ulang == 'y':
        loop = True
        session.delete()
    elif ulang == 'N' or ulang == 'n':
        loop = False
    else:
        loop = False
        print('Input salah')
