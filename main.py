import requests
import os
from flask import Flask,jsonify
import bs4

app = Flask(__name__)

@app.route('/LimitedData/<var>')
def GetLimitedData(var):
  Data = requests.get('https://economy.roblox.com/v1/assets/'+var+'/resale-data')
  Data2 = requests.get('https://www.roblox.com/catalog/'+var)
  if Data.status_code == 200:
    document= bs4.BeautifulSoup(Data2.text, 'html.parser')
    Lowest = document.find("span",class_="text-robux-lg wait-for-i18n-format-render")
    if Lowest != None:
      Lowest = Lowest.string
    else:
      Lowest = ''
      
    Data = Data.json()
    Data["success"] = True
    Data['SellingPrice'] = Lowest
    return jsonify(Data)
  else:
    print(Data.json())
    return jsonify({'success': False})
  
@app.route("/")
def Home():
  return "Home"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
