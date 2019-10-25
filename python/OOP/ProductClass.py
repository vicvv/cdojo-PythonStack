#To product class:
# update_price(self, percent_change, is_increased) - updates the product's price. 
# If is_increased is True, the price should increase by the percent_change provided. 
# If False, the price should decrease by the percent_change provided.
# print_info(self) - print the name of the product, its category, and its price.   


class Product:
    #myproducts = []
    def __init__(self, id = 0, name=None, price=0, category=0):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, product= None, is_increased=None):
        
            if is_increased == True:                
                product.price = product.price + (product.price/100) * percent_change

            elif is_increased == False:
                product.price= product.price  - (product.price/100) * percent_change 
            
            else:
                print("Not found")
            return product
          

    def __str__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])