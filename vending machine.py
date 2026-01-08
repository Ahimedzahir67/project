def vending_machine():
    # 1. Product list
    products = {
        "1": {"name": "Coke", "price": 2.5},
        "2": {"name": "Water", "price": 1.0},
        "3": {"name": "Chips", "price": 1.5},
        "4": {"name": "Chocolate", "price": 3.0}
    }

    print(" Welcome to the vending machine ")
    
    # 2. Display products 
    for code, details in products.items():
        print(f"Code {code}: {details['name']} - price: ${details['price']}")

    # 3. User choice
    choice = input("\nPlease enter the product code: ")

    if choice in products:
        item = products[choice]
        print(f"You selected {item['name']}. Price: ${item['price']}")
        
        try:
            money = float(input("Insert money: "))
            if money >= item['price']:
                print(f"Enjoy your {item['name']}! Change: ${money - item['price']:.2f}")
            else:
                print("Not enough money.")
        except ValueError:
            print("Please enter numbers only.")
    else:
        print("Invalid code.")

vending_machine()
#this my project to vending machine



