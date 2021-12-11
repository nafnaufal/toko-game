import requests

import pandas as pd 
s = input()
s = s.replace(' ','_')
df = pd.read_json('https://www.cheapshark.com/api/1.0/games?title='+s)
print(df['internalName'])
