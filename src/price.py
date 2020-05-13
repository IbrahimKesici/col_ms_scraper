import re

class Price():
    
    def __init__(self, web_price):
        self.price = self.__identify_price(web_price)
        self.currency = self.__identify_currency(web_price)

    def __identify_price(self, web_price):
        numeric_price = re.findall(r"\d+\.\d+", web_price)[0]
        return float(numeric_price)
    
    def __identify_currency(self, web_price):
        return re.sub('\d.*','', web_price).strip()

    def get_numberic_price(self):
        return self.price

    def get_currency(self):
        return self.currency
  
    def __str__(self):
        return f"{self.price} - {self.currency}"