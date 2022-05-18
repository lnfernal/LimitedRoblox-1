import requests

count = 0
while True:
    res=requests.get(
    "https://economy.roblox.com/v1/assets/7592037079/resale-data",
    proxies={
        "http": "http://endwaprt-rotate:eh99st1hdkqg@p.webshare.io:80/",
        "https": "http://endwaprt-rotate:eh99st1hdkqg@p.webshare.io:80/"})
    if res.status_code == 200:
        count += 1
        print(count)
    else:
        print(count,'end')
        break
