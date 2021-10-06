import os
import re
from customer import Customer
from product import Product
from register import Register
import json
import sys


def clear_screen():
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def print_ui():
    clear_screen()

    print(
        f"""
#####################################
        Supermarket system
#####################################

Enter number between 1 to 7:

1. Create customer
2. Create register

3. List customers
4. List registers

5. Start shopping

6. Print summary

7. Exit and save data

#####################################

"""
    )


def print_shop(customer: Customer):
    clear_screen()
    print(
        f"""
#####################################
##             Shop                ##
#####################################

Hello {customer.name.capitalize()}
Total purchase is {customer.total_cost}$


Enter number between 1 to 4:

1. Add product to cart
2. Remove product from cart
3. Your shopping cart

4. Checkout

5. Go back

#####################################

"""
    )


def new_customer_page(customers):
    # Printing the 'new customer' page to the user and adding it to the customers dict
    clear_screen()
    customer_name = input('Enter customer name: ').lower()
    while (customer_name in customers.keys()) or customer_name == '':
        customer_name = input(
            'Customer name already exists or no name was entered. Try another name: ').lower()

    customers[customer_name] = Customer(customer_name)


def new_register_page(registers):
    # printing the 'new register' page to the user and adding it to the registers dict
    clear_screen()
    register_name = input('Enter register name: ').lower()
    while (register_name in registers.keys()) or register_name == '':
        register_name = input(
            'Register name already exists or no name was entered. Try another name: ').lower()
    registers[register_name] = Register(register_name)


def list_customers_page(customers):
    # Printing all existing customers to the user
    clear_screen()
    for key in customers:
        print(customers[key])
        print('############################\n\n')
    input('\n\nPress enter key to continue...')


def list_registers_page(registers):
    # Printing all existing registers to the user
    clear_screen()
    print(
        """
############################
Available registers
############################
"""
    )
    for key in registers:
        print(key)
    input('\n\nPress enter key to continue...')


def print_summary(registers):
    # Printing summary of all registers to the user
    clear_screen()
    for key in registers:
        print(registers[key])
        print('############################')

    input('\n\nPress enter key to continue...')


def shopping_page(customers: dict, registers: dict):
    # Printing 'shopping page', reading all the necessary input from user
    # and takes care of all the user actions inside the shop page

    clear_screen()

    # Asking the user to enter a customer name
    current_customer = input('Enter your customer name: ').lower()
    if current_customer not in customers.keys():
        print("Customer not exists, you can create new customer in the main menu.")
        input('\n\nPress enter key to continue...')
        return

    # Asking the user to enter the name of register hey wants to buy from
    current_register = input(
        "Enter register name to checkout to (Leave empty to see available registers): ")
    while current_register not in registers.keys():
        clear_screen()
        if current_register == '':
            list_registers_page(registers)
            current_register = input("Enter register name to checkout to: ")
        else:
            current_register = input(
                "Register not found, enter register name to checkout to (Leave empty to see available registers): ")

    # Entering the shop
    while True:
        print_shop(customers[current_customer])
        user_action = input('Enter Your choice: ')
        while not (user_action.isdigit() and 0 < int(user_action) < 6):
            print_shop(customers[current_customer])
            user_action = input('Invalid input! Enter Your choice again: ')

        user_action = int(user_action)

        # User adds a product to his cart
        if user_action == 1:
            clear_screen()
            product_name = input("Enter product name: ").lower()

            product_quantity = input("Enter product quantity: ")
            while not product_quantity.isdigit():
                product_quantity = input("Enter a valid product quantity: ")

            if product_name not in customers[current_customer].shopping_list.keys():
                product_price = input("Enter product price: ")
                while not re.fullmatch("[0-9]+(\.[0-9]+)?", product_price):
                    product_price = input("Enter a valid product price: ")
            else:
                product_price = customers[current_customer].shopping_list[product_name].price

            customers[current_customer].add_product(
                Product(product_name, float(product_price), int(product_quantity)))
            input(
                f"You Added {product_name} x{product_quantity} to your cart.\n\nEnter any key to continue...")

        # User removes a product from his cart
        elif user_action == 2:
            clear_screen()
            if len(customers[current_customer].shopping_list) == 0:
                input(
                    "You don't have any products in your cart.\n\nPress enter to continue...")
                continue

            product_name = input("Enter product name: ").lower()
            while product_name not in customers[current_customer].shopping_list:
                product_name = input(
                    "Product not exists in your cart, Enter product name: ")

            while True:
                quantity_to_remove = input("Enter quantity for remove: ")

                if not quantity_to_remove.isdigit():
                    print("Invalid quantity!")
                    continue

                if int(quantity_to_remove) > customers[current_customer].shopping_list[product_name].quantity:
                    print(
                        f"Quantity higher then what in your cart (quantity of '{product_name}' in your cart is "
                        f"{customers[current_customer].shopping_list[product_name].quantity})"
                    )
                    continue
                break
            customers[current_customer].remove_product(
                product_name, int(quantity_to_remove))
            input(
                f"You removed {product_name} x{quantity_to_remove} from cart.\n\nEnter any key to continue...")

        # Prints customer shopping list
        elif user_action == 3:
            clear_screen()
            print(customers[current_customer])
            input('\n\nPress Enter to continue... ')

        # Checkout
        elif user_action == 4:
            clear_screen()
            if customers[current_customer].total_cost == 0:
                input("You didn't buy anything.\n\nPress enter to continue...\n")
                continue

            registers[current_register].checkout_customer(
                customers[current_customer])

            input(
                f"You paid {customers[current_customer].total_cost}$ to {registers[current_register].name}\n\nEnter any key to continue...")

        # User returns to main menu
        else:
            return


def save_to_files(customers):
    # Saving the data about all customers and their cart.
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    for customer_name in customers:
        os.makedirs(os.path.join(ROOT_DIR, 'data',
                    customer_name, 'items'), exist_ok=True)

        shopping_list_file = {}
        items = {}
        for product in customers[customer_name].shopping_list:
            item = {
                "name": customers[customer_name].shopping_list[product].name,
                "price": customers[customer_name].shopping_list[product].price,
                "units": customers[customer_name].shopping_list[product].quantity
            }

            with open(os.path.join(ROOT_DIR, 'data', customer_name, 'items', product + '.json'), 'w') as item_file:
                item_file.write(json.dumps(item))

            items[customers[customer_name].shopping_list[product].name] = {
                "total_price": customers[customer_name].shopping_list[product].price * customers[customer_name].shopping_list[product].quantity
            }

        shopping_list_file["products"] = items
        shopping_list_file["total_cost"] = customers[customer_name].total_cost
        with open(os.path.join(ROOT_DIR, 'data', customer_name, 'shopping_list.json'), 'w') as shopping_file:
            shopping_file.write(json.dumps(shopping_list_file))


def main():

    customers = {}
    registers = {}

    while True:
        print_ui()

        # main menu
        user_input = input('Enter Your choice: ')
        while not (user_input.isdigit() and 0 < int(user_input) < 11):
            print_ui()
            user_input = input('Invalid input! Enter Your choice again: ')

        user_input = int(user_input)

        # Creates new customer
        if user_input == 1:
            new_customer_page(customers)

        # Creates new register
        elif user_input == 2:
            new_register_page(registers)

        # Lists all existing customers
        elif user_input == 3:
            list_customers_page(customers)

        # Lists all existing registers
        elif user_input == 4:
            list_registers_page(registers)

        # Starts the shopping process
        elif user_input == 5:
            if not (len(registers) and len(customers)):
                input("\nYou have to create at least one register and one customer before entering the shop.\n\nPress enter key to continue...")
                continue
            shopping_page(customers, registers)

        # Prints summary
        elif user_input == 6:
            print_summary(registers)

        # User quits the program
        else:
            save_to_files(customers)
            sys.exit(0)


if __name__ == "__main__":
    main()
