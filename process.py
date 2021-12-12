# limit string 30
def limit(str):
    if len(str) > 30:
        str = str[:15]+' ... '+str[len(str)-10:]
    return str

# limit string 30
def limit98(str):
    if len(str) > 98:
        str = str[:50]+' ... '+str[len(str)-40:]
    return str

# double digit
def dg(n):
    if n > 99:
        x = str(n)
        return '.' + x[len(x)-1:]
    elif n > 9:
        return str(n)
    else:
        return ' '+str(n)


def showListGame(game_name, game_price):

    print('┏━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('┃NO┃           List Game          ┃       Lowest Price (USD)     ┃')
    print('┡━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩')

    c = 0
    for i in game_name:
        p = str(i).center(30, ' ')
        q = ((game_price[c]).center(30, ' ')).ljust(30, ' ')

        print('│'+dg(c+1)+'│'+limit(p) + '│'+limit(q) + '│')
        print('├──┼──────────────────────────────┼──────────────────────────────┤')

        c += 1

    print('└──┴──────────────────────────────┴──────────────────────────────┘')


def showStore(sel_game, store_name, nama_game):
    counter = 0
    print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('┃' + limit98(nama_game.ljust(98, ' ')))
    print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    for i in sel_game['deals']:
        redic = "https://www.cheapshark.com/redirect?dealID="+sel_game['deals'][counter]['dealID']
        
        print('│' + ('Store Name').ljust(15, ' ') + '│ ' + store_name[int(i['storeID'])-1])
        print('│' + ('Harga Normal').ljust(15, ' ') + '│ ' + sel_game['deals'][counter]['retailPrice'])
        print('│' + ('Harga Diskon').ljust(15, ' ') + '│ ' + sel_game['deals'][counter]['price'])
        print('│' + ('% Save').ljust(15, ' ') + '│', float(sel_game['deals'][counter]['retailPrice']) - float(sel_game['deals'][counter]['price']))
        print('│' + ('Link').ljust(15, ' ') + '│ ' + redic)
        print('└───────────────┴────────────────────────────────────────────────────────────────────────────────────')
        counter += 1
