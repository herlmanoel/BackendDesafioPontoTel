import unittest
from src.utils import getInfosEmpresa, getDataAPI

class ServerTest(unittest.TestCase):
    
    def test_getInfosEmpresa(self):
        result = getInfosEmpresa("bovespa")
        test = { "name": 'BOVESPA INDUSTRIAL SECTOR INDEX', "symbol": 'INDX.SAO' }
        self.assertEqual(test, result)
    
    def test_getDataAPI(self):
        result = getDataAPI("IBOV.SAO")
        test = { "preco": "118647.0900", "name": "Sao Paulo Bovespa Index" }

if __name__ == '__main__':
    unittest.main()