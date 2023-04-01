def shop_items():
    shop_items = {'socks': 5, 'shirt': 25, 'bag': 500}
    return shop_items

shop_items = shop_items()
print("Welcome to the shop!")
for item, price in shop_items.items():
    print(f"{item}: £{price}")

item_choice = input("Please choose an item or type 'exit' to leave: ")
customer_money = 100


#Create Function1
def LeavingStore(item_choice):
    while item_choice == 'exit':
        leaving = "Goodbye!"
        print(leaving)
        break

    while item_choice not in shop_items:
        raise ValueError("Sorry, what you are looking for is not here")


#Create Function2
def Subtraction(customer_money,item_price):
    return customer_money - item_price


try:
    LeavingStore(item_choice)


    item_price = shop_items[item_choice]

    if customer_money < item_price:
        print("You don't have enough money")
        more_money = input("Do you have more money? y/n: ")
        if more_money == "y":
            count = 0
            while customer_money < item_price and count < 3:
                amount_of_money = float(input("How much more money do you have? "))
                customer_money = amount_of_money + customer_money
                print(f"Your balance is now £{customer_money}.")
                count = count + 1
            else:
                if customer_money >= item_price:
                    print(f"You have now bought your {item_choice}!")
                    print(f"Your balance is now £{Subtraction(customer_money,item_price)}.")
                else:
                    print("Sorry you don't have enough money to buy this item! Please come again another time")
        else:
            print("Sorry,see you soon!")
    else:
        num1 = item_price
        num2 = customer_money
        print(f"Here's your {item_choice}!")
        print(f"Your balance is now £{Subtraction(customer_money,item_price)}.")
except ValueError as e:
    print(f"Invalid input: {e}")
