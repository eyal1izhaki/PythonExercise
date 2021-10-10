class Customer:
    def __init__(self, name :str):
        self.name = name.lower()
        self.shopping_list = {}
        self.total_cost = 0

    def add_product(self, product):

        if product.name not in self.shopping_list.keys():
            self.shopping_list[product.name] = product
            self.total_cost += product.total_price
        else:
            self.shopping_list[product.name].quantity += product.quantity
            self.shopping_list[product.name].total_price += product.total_price
            self.total_cost += product.total_price

    def remove_product(self, name: str, quantity: int):

        if quantity < self.shopping_list[name].quantity:
            self.shopping_list[name].quantity -= quantity
            self.shopping_list[name].total_price -= quantity*self.shopping_list[name].price
            self.total_cost -= quantity*self.shopping_list[name].price
            return True

        elif quantity == self.shopping_list[name].quantity:
            self.total_cost -= quantity*self.shopping_list[name].price
            del self.shopping_list[name]
            return True
        
        return False

    def __str__(self) -> str:
        shopping_list_str = ''
        for key in self.shopping_list:
            shopping_list_str += str(self.shopping_list[key]) + '\n'

        return f"Name: {self.name.capitalize()}\n\nShopping list:\n--------------\n{shopping_list_str}\nTotal cost: {self.total_cost}"

    


        
        
        


