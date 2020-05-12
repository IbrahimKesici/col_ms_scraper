

class Price():
    
    def __init__(self, web_price):
        self.price = self.__identify_price(web_price)
        self.currency = self.__identify_currency(web_price)

    def __identify_price(self, web_price):
        pass
    
    def __identify_currency(self, web_price):
        pass

    def get_currency(self):
        pass
  
    def get_price(self):
        pass

    def __str__(self):
        return f"{self.price} - {self.currency}"

class Product():

    def __init__(self, title, web_price):
        self.title = title
        self.price = Price(web_price = web_price)
    
    
  

    
