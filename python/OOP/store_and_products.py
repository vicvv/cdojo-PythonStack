from ProductClass import *
   
# to Store class
# add_product(self, new_product) - takes a product and adds it to the store
# sell_product(self, id) - remove the product from the store's list of products 

# given the id (assume id is the index of the product in the list) and print its info.

# inflation(self, percent_increase) - increases the price of each product 
# by the percent_increase given (use the method you wrote in the Product class!)

# get_clearance(self, category, percent_discount) - updates all the products 
# matching the given category by reducing the price by the percent_discount given 
# (use the method you wrote in the Product class!)

import uuid
import time

class Store:
    def __init__(self, name = None, prod_list=[]):
        self.name = name
        self.prod_list = prod_list

    def add_product(self,new_product_name, price, category):
        id = "{}-{}".format(uuid.uuid4(), time.time())
        newprod = Product(id,new_product_name, price, category)
        self.prod_list.append(newprod)
        
    
    def sell_product(self, prod_id):
        self.prod_list.pop(prod_id)

    def print_prod_info(self, prod_id=None):
        if prod_id == None:
            print("All products in the store:")
            for item in self.prod_list:    
                print(item)
        else:
            print("\nInfo for product with id:", prod_id)
            print(self.prod_list[prod_id], end ="")

    def inflation(self, id, percent_increase):
        prod = Product()
        upd_prod=prod.update_price(percent_increase, self.prod_list[id],is_increased=True)
        self.prod_list[id] = upd_prod

    def get_clearance(self, category_id, percent_discount):
        prod = Product()
        i = 0
        for prod in self.prod_list:
            if prod.category == category_id: 
                print("found a catid match!", prod.category, category_id)   
                upd_prod=prod.update_price(percent_discount, self.prod_list[i],is_increased=False)
                self.prod_list[i] = upd_prod
            i = i+1
           
       
    # def __str__(self):
    #     # Override to print a readable string presentation of your object
    #     # below is a dynamic way of doing this without explicity constructing the string manually
    #     return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])


mystore= Store()
mystore.add_product("Buble", 20, 11)
mystore.add_product("Chair", 250, 8)
mystore.add_product("Table", 25, 3)
mystore.add_product("T", 5, 3)
mystore.add_product("B", 15, 3)
mystore.add_product("D", 3, 3)
mystore.add_product("Plate", 20, 11)

mystore.print_prod_info()
mystore.print_prod_info(1)

print("\nAfter inflation:")
mystore.inflation(0,2)

mystore.print_prod_info()
print('After clearence')
mystore.get_clearance(3,2)
mystore.print_prod_info()


mystore.sell_product(2)
print("\nSold product with id = 2")
mystore.print_prod_info()

#print(mystore)


