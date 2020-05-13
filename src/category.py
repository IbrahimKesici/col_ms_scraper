from price import Price

class Category():
    id = 0
    def __init__(self, name, href=None):
        self.name = name.capitalize()
        self.href = href
        self.subcategories = {}
        self.products = {}
        self.id = Category.id 
        Category.id += 1

    def get_name(self):
        return self.name

    def get_unique_name(self):
        return str(self.id) + self.name
    
    def get_href(self):
        return self.href

    def get_subcategories(self):
        return self.subcategories.values()

    def get_id(self):
        return self.id

    def add_subcategory(self, subcategory):
        self.subcategories[subcategory.get_unique_name()] = subcategory

    def add_product(self, product):
        self.products[product.get_title] = product
    
    def get_products(self):
        return self.products.values()

    def __str__(self):
        return f"{self.id} - {self.name} has {len(self.subcategories)} subcategories."

class Product():
    
    def __init__(self, title, price):
        self.title = title
        self.price = Price(web_price=price)
       
    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.title} - {self.price}"