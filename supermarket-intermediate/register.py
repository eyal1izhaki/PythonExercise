class Register:

    def __init__(self, name):
        self.name = name
        self.profits = 0
        self.sales_list = {}

    def checkout_customer(self, customer):
        self.profits+= customer.total_cost
        if customer.name in self.sales_list.keys():
            self.sales_list[customer.name] += customer.total_cost
        else:
            self.sales_list[customer.name] = customer.total_cost

    def print_summary(self):
        print(
            f"""
            All shopping lists:
            {self.shopping_lists}

            profit: {self.profits}
            """
        )

    def __str__(self) -> str:
        sale_str = ''
        for customer in self.sales_list:
            sale_str += f"\n{customer}\t{str(self.sales_list[customer])}$"
        return f"Register name: {self.name}\nProfits: {self.profits}$\n\nSales list: {sale_str}\n"