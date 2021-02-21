from flask import request
import requests
import json

def getInfosEmpresa(name_empresa):
    URL = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+name_empresa
    URL += '&apikey=40XLOC783TDG4L6E'
    response = requests.get(URL)
    objeto = response.json()
    objeto = objeto['bestMatches']
    name = objeto[0]['2. name']
    symbol = objeto[0]['1. symbol']
    return { "name": name, "symbol": symbol }

def getDataAPI(empresa):
    infos = getInfosEmpresa(empresa)
    symbol = infos['symbol']
    param = 'function=TIME_SERIES_DAILY'
    param += '&symbol=' + symbol
    param += '&apikey=40XLOC783TDG4L6E'
    URL = 'https://www.alphavantage.co/query?'+param

    try:
        response = requests.get(URL)
        objeto = response.json()
        objeto = objeto["Time Series (Daily)"]
        ultima_atualizacao = list(objeto.keys())[0]
        objeto = objeto[ultima_atualizacao]['4. close']

        name = infos['name']
        return { "preco": objeto, "name": name }
    except Exception as error:
            print(error)
            return { "erro": "Error" }