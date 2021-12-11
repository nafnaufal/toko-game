import requests
import webbrowser
import numpy as np
import pandas as pd 
pd.set_option('display.max_colwidth', -1)
s = input()
s = s.replace(' ','_')
df = pd.read_json('https://www.cheapshark.com/api/1.0/games?title='+s)
df['usd'] = df['cheapest']
df['idr'] = df['cheapest']*14355

# print(df[['external','usd','idr']])

# a = int(input())
# print(df.iloc[a,4])
# d = (df.iloc[a,3])
# b = 'https://www.cheapshark.com/redirect?dealID='+d
# webbrowser.open(b, new=1) # link yg akan dituju

# cek = df.iloc[1,0]
# cek = cek(str)
# print(type(cek))
# df['gameID'] = df['gameID'].astype(str)
# cek = df.iloc[1,0]
# cek = str(cek)
# print(cek)
aa = '233214'

cf = pd.read_json('https://www.cheapshark.com/api/1.0/games?id='+aa)

print(cf)

# cf = pd.read_json('https://www.cheapshark.com/api/1.0/games?id='+cek)
# for game in df['gameID']:
#     i = i + 1
#     cek = df.iloc[i,0]
#     cek = cek(str)
#     print(type(cek))
#     cf = pd.read_json('https://www.cheapshark.com/api/1.0/games?id='+df.iloc[i,0])
