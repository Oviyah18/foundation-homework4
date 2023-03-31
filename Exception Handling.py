class Money(Exception):
    pass

shop_items = {'socks': 5, 'shirt': 25, 'bag': 500}

customer_money = 100

print("Welcome to the shop!")
for item, price in shop_items.items():
    print(f"{item}: £{price}")

for i in range(3):
    item_choice = input("Please choose an item or type 'exit' to leave: ")

    try:
        if item_choice == 'exit':
            print("Goodbye!")
            break

        if item_choice not in shop_items:
            raise ValueError("Invalid item choice.")

        item_price = shop_items[item_choice]
        if item_price > customer_money:
            print("Sorry, you don't have enough money to buy this item.")
            additional_money = input("Do you have more money? Enter the amount or type 'no': ")
            if additional_money == 'no':
                raise Money("You don't have enough money to make a purchase.")
            else:
                customer_money += int(additional_money)
                print(f"Your balance is now £{customer_money}.")
                customer_money -= item_price
                print(f"Here's your {item_choice}!")
                print(f"Your new balance is now £{customer_money}.")
                break

        else:
            customer_money -= item_price
            print(f"Here's your {item_choice}!")
            print(f"Your balance is now £{customer_money}.")
            break

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Money as e:
        print(e)
        print("Goodbye!")
        break
    else:
        print("Thank you!")
    finally:
        print("Come Again Soon!")
