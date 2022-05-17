import requests
import os
from flask import Flask,jsonify
import bs4

app = Flask(__name__)

@app.route('/LimitedData/<var>')
def GetLimitedData(var):
  Data = requests.get('https://economy.roblox.com/v1/assets/'+var+'/resale-data')
  Data2 = requests.get('https://economy.roblox.com/v1/assets/'+var+'/resellers')
  if Data.status_code == 200:
    Lowest = Data2.json().get("data")
    if Lowest != None:
      Lowest = Lowest[0]['price']
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
