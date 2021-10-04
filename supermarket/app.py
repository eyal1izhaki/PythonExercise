import os


def clear_screen():
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def str2float(input: str):
    # returns float represented by given str or None if the given str not formatted as float
    try:
        result = float(input)
    except ValueError:
        return None
    return result


def str2int(input: str):
    # Returns int represented by given str or None if the given str not formatted as float
    try:
        result = int(input)
    except ValueError:
        return None
    return result

def read_name(message: str):
    # Reads a name of product and returns it as lowercase
    clear_screen()
    name = input(message + " : ").lower()
    while name == '':
        clear_screen()
        name = input(message + " (can't be empty): ").lower()
    return name


def read_price(message: str):
    # Reads the price of a product and validates the input. Returns the price
    clear_screen()
    price = str2float(input(message + ": "))
    while not price:
        clear_screen()
        price = str2float(input(message + " (only decimal number): "))
    return price


def read_quantity(message: str):
    #  Reads the quantity and validates the input. Returns the quantity
    clear_screen()
    quantity = str2int(input(message + ": "))
    while not quantity:
        clear_screen()
        quantity = str2int(input(message + " (numbers only): "))
    return quantity


def add_to_cart(shopping_cart: dict):
    # Adds a product to a given shopping cart dict and returns a message that should be printed to the user

    name = read_name("Enter product name")

    if name not in shopping_cart.keys():
        price = read_price("Enter product price")

    quantity = read_quantity("Enter quantity")

    # Updating shopping cart
    if name not in shopping_cart.keys():
        shopping_cart[name] = {"price": price, "quantity": quantity}
    else:
        shopping_cart[name]["quantity"] += quantity

    return " + " + name + " x" + str(quantity)


def remove_from_cart(shopping_cart: dict):
    # Removes a product from the cart and return a message that should be printed to the user

    name = read_name("Enter product to remove")
    while name not in shopping_cart.keys():
        name = read_name("Product not found, enter product to remove")

    quantity = read_quantity("Enter quantity to remove")
    quantity_in_cart = shopping_cart[name]["quantity"]

    if quantity < quantity_in_cart:
        shopping_cart[name]["quantity"] -= quantity
        return " - " + name + " x" + str(quantity)

    elif quantity == quantity_in_cart:
        del shopping_cart[name]

    else:
        return f" ! can't remove quantity of {name} higher then {quantity_in_cart}"

    return " - " + name + " x" + str(quantity)


def checkout(shopping_cart :dict):
    clear_screen()
    print("#####################################\nProduct\t\tQuantity\t\tPrice\n#####################################")
    for key in shopping_cart.keys():
        quantity = shopping_cart[key]['quantity']
        price = shopping_cart[key]['price']
        print(f"{key}\t\tx{quantity}\t\t{price}$")
    print('\n\nTotal', calculate_total_cost(shopping_cart),'\n')



def print_ui(total_cost: float, message=''):
    clear_screen()
    print(
        f"""
#####################################
         Supermarket Receipt
#####################################

Enter 1, 2 or 3:                    # 
1 for adding new product            # 
2 for removing product from cart    #
3 for checkout                      # Total cost: {total_cost}

{message}
#####################################

"""
    )


def calculate_total_cost(shopping_cart: dict):
    result = 0
    for key in shopping_cart:
        result += int(shopping_cart[key]["quantity"])*float(shopping_cart[key]["price"])
    return result


def main():
    total_cost = 0
    shopping_cart = {}

    user_message = ''

    while True:
        print_ui(total_cost, user_message)

        # Reads user menu choice
        choice = input("Enter your choice: ")
        while choice not in ['1' , '2', '3']:
            choice = input("Enter your choice (1, 2 or 3 only): ")

        if choice == '1':
            user_message = add_to_cart(shopping_cart)
        elif choice == '2':
            user_message = remove_from_cart(shopping_cart)
        elif choice == '3':
            checkout(shopping_cart)
            break

        total_cost = calculate_total_cost(shopping_cart)



if __name__ == "__main__":
    main()