from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import requests
import json
import utils

app = Flask("api")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    if request.method == 'POST':
        information = request.data
        symbol_empresa = json.loads(information)['empresa']
        objeto = utils.getDataAPI(symbol_empresa)
        return objeto
    
    objeto = utils.getDataAPI("IBOV.SAO")
    return objeto

app.run()