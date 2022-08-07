from urllib import response
import requests

key = '*' # Your steam API-key goes here, you can find it under "https://steamcommunity.com/dev/registerkey"

def check_bans(steamid):
    r = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={key}&steamids={steamid}')
    print(r.text)

check_bans('*') # You can put multiple steamids like this: steamid1,steamid2,steamid3
