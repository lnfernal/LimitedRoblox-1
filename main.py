import requests
import os
from flask import Flask,jsonify


app = Flask(__name__)
print(os.getenv("PORT"))

@app.route('/LimitedData/<var>')
def GetLimitedData(var):
  Data = requests.get('https://economy.roblox.com/v1/assets/'+var+'/resale-data')
  if Data.status_code == 200:
    Data = Data.json()
    Data["success"] = True
    return jsonify(Data)
  else:
    print(Data.json())
    return jsonify({'success': False})
  
@app.route("/")
def Home():
  return "Home"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
