
from src.price import Price

class Product():

    def __init__(self, title, web_price):
        self.title = title
        self.price = Price(web_price = web_price)
    
    def get_title(self):
        return self.title

    def get_price(self):
        return self.price
    
    def __str__(self):
        return f"{self.title}: {self.price}"
    
  

    
