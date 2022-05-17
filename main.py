import requests
import os
from flask import Flask,jsonify
import bs4
from time import sleep

app = Flask(__name__)

def GetPriceAndName(var):
  Lowest = None
  Name = None
  while Lowest == None and Name == None:
    Data2 = requests.get('https://www.roblox.com/catalog/'+var)
    document= bs4.BeautifulSoup(Data2.text, 'html.parser')
    Lowest = document.find("span",class_="text-robux-lg wait-for-i18n-format-render")
    Name = document.title
    sleep(2)
  return Lowest.string,Name.string

def GetResaleData(var):
  Data = None
  while Data == None :
    GetData = requests.get('https://economy.roblox.com/v1/assets/'+var+'/resale-data')
    if GetData.status_code == 200:
      Data = GetData.json()
    else:
      sleep(2)
  return Data

@app.route('/LimitedData/<var>')
def GetLimitedData(var):
    Data = GetResaleData(var)
    Data["success"] = True
    Data['BestPrice'],Data['Name'] = GetPriceAndName(var)
    return jsonify(Data)
  
@app.route("/")
def Home():
  return "Home"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
