import sys
import time

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Prompt system operator for tax rate
tax_rate_str = input("System operator please enter the tax rate (as a %): ")

# Verify tax rate can be a float and convert to decimal value via try/except
try:
    tax_rate = float(tax_rate_str) / 100
except:
    print("Unable to convert tax rate. Exiting!")
    exit()

# Notify operator how to exit infinite loop as a kiosk
print("\nTo exit Kiosk press Ctrl + C.\n")
_ = input("Press Enter to begin Kiosk mode.")
while True:
    # Would be nice to add a clear screen here. Seems OS dependent
    #   but simulate it with a bunch of blank lines for now
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    # initialize blank order list here for each new order
    order_list = []

    # Display Welcome for patron at beginning of order
    print("Welcome to NGT Food Truck Ordering System\n\n")

    # Loop for continuous order starting with main menus
    continue_order = True
    while continue_order:
        print("Available Menus:")

        # Store list of main menu names
        menu_names = []

        # Print main menu and wait for patron input
        idx = 1
        for main_menu in menu:
            menu_names.append(main_menu)
            print(f"   {str(idx)}: {main_menu}")
            idx += 1
        menu_txt = input("\nPlease enter the number for the menu to order from: ")
        
        # Check input to verify input is one of the main menu options
        if menu_txt.isdigit() and int(menu_txt) >= 1 and int(menu_txt) <= len(menu):
            # keep an index for item numbers and print header
            idx = 1
            print(" # | Item                      | Price  ")
            print("-" * 40)
            # Flatten any nested dictionaries into list of labeled dicts
            sub = []
            sub_menu = menu[menu_names[int(menu_txt)-1]]
            for food_item in sub_menu:
                if type(sub_menu[food_item]) is not dict:
                    # And print menu as we flatten
                    print(f"{idx:>2} | {food_item:25} | ${sub_menu[food_item]:>5}")
                    sub.append({"Number" : str(idx),
                                "Name" : food_item,
                                "Price" : sub_menu[food_item]})
                    idx += 1
                else:
                    for sub_food_item in sub_menu[food_item]:
                        # Concat name with sub name, print, and store
                        sub_name = food_item + " - " + sub_food_item
                        print(f"{idx:>2} | {sub_name:25} | ${sub_menu[food_item][sub_food_item]:>5}")
                        sub.append({"Number" : str(idx),
                                    "Name" : sub_name,
                                    "Price" : sub_menu[food_item][sub_food_item]})
                        idx += 1
            
            # Prompt user for individual item choice
            choice = input("Please enter the number for an item: ")
            # validate item # stored as string with list comprehension
            if choice in [item["Number"] for item in sub]:
                # Prompt user for quantity and verify integer or defualt 1
                qty_str = input("How many would you like to order? ")
                if qty_str.isdigit:
                    qty = int(qty_str)
                else:
                    print("\nInvalid number, defaulting to 1 quantity.\n")
                    qty = 1

                # Iterate through recent sub menu for choice and store
                for item in sub:
                    if item["Number"] == choice:
                        # add item to order list as labeled dict 
                        order_list.append({"Name" : item["Name"],
                                           "Price" : item["Price"],
                                           "Qty" : qty})
                        print(f"Added: {qty} {item['Name']}")
            else:
                print("\nInvalid option, please try again.\n")
            
            # loop until user inputs Y, y, N, or n
            while True:
                # Prompt user to continue order or end order
                more_order = input("Would you like to continue ordering (Y)es or (N)o? ")
                match more_order.lower():
                    case "y":
                        print("\nYou may continue.\n")
                        break
                    case "n":
                        print("\nPlease review your order below.\n\n")
                        continue_order = False
                        break
                    case _:
                        prin("\nYou must type 'Y' to continue or 'N' to end your order.\n")
            
        else:
            print("\nMenu not found. Please enter menu number from availabile menus.\n\n")
        
    # Confirm or edit order
    confirmed = False
    canceled = False
    while not confirmed and not canceled:
        # Iterate order printing order review table based on:
        print(" # | Item                      | Price  | Qty |  Cost   ")
        print("-" * 55)
        idx = 1
        for item in order_list:
            cost = f"{(item['Price'] * item['Qty']):.2f}"
            print(f"{idx:>2} | {item['Name']:25} | ${item['Price']:>5} | {item['Qty']:^3} | ${cost:>6}")
            idx += 1
        # Calculate and print sub total, tax, and total rows
        sub_total = sum([item["Price"] * item["Qty"] for item in order_list])
        print("-" * 55)
        print(f"{' ' * 37}Subtotal | ${sub_total:>6.2f}")
        tax = sub_total * tax_rate
        tax_rate_str = str(tax_rate * 100) + "%"
        spacer = " " * (39 - len(tax_rate_str))
        print(f"{spacer}Tax ({tax_rate_str}) | ${tax:>6.2f}")
        total = sub_total + tax
        print(f"{' ' * 46}{'-' * 9}")
        print(f"{' ' * 40}Total | ${total:>6.2f}")
        print(f"{' ' * 46}{'-' * 9}\n")

        while True:
            # Continually prompt user to confirm, cancel or edit order
            confirm = input("Confirm order (Y)es, (N)o to cancel, or type line # to edit: ")
            match confirm.lower():
                case 'y':
                    confirmed = True
                    break
                case 'n':
                    print("\n\nOrder canceled!\n\n")
                    canceled = True
                    break
                case _:
                    if confirm.isdigit() and int(confirm) >=1 and int(confirm) <= len(order_list):
                        # Allow editing of quantity for that line item
                        idx = int(confirm) - 1
                        qty_str = input(f"How many {order_list[idx]['Name']} would you like to order (type 0 to remove item from order)? ")
                        if qty_str.isdigit():
                            order_list[idx]["Qty"] = int(qty_str)
                            if int(qty_str) == 0:
                                order_list.pop(idx)
                        else:
                            print("Invalid number, defaulting to 1.")
                            order_list[idx]["Qty"] = 1
                        break
                    else:
                        print("\nYou must confirm, cancel, or edit this order.\n")
                              
    if confirmed:
        # Thank user, notify of preperation
        print("\n\nThank you for your order. Your food is bring prepared.\n\n")
        
        """ 
        Ordinarily here would be printing a reciept,
        sending order to food preperation staff,
        creating ticket/order number for pickup,
        and processing some form of payment, etc.
        But, this is the extent of my intended practice.
        """

    # Pause to allow user to read before reseting screen for next patron
    time.sleep(10)
