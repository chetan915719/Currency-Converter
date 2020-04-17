import requests

class Currency_convertor:

    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data['rates']

    def convert(self,from_currency,to_currency):
        rate = 1
        if from_currency != 'EUR':
            rate = 1 / self.rates[from_currency]
        
        rate = rate * self.rates[to_currency]
        return rate
