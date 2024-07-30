class Product:
    def __init__(self, price):
        self.price = (price)
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    #propertyfunction called in decorator
    #parameter 1: get value of function
    #parameter 2: set value of attribute
    #parameter 3: delete attribute
    #parameter 4: documentation

product = Product(10)
product.price = -1
print(product.price)