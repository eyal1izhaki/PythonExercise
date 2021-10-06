class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name.lower()
        self.price = price
        self.quantity = quantity
        self.total_price = price*quantity

    def __repr__(self) -> str:
        return f"{self.name}\t\tx{self.quantity}\t* {self.price}$\t= {self.total_price}"