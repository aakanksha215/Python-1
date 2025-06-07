# Define the menue

menu = {
    'Pizza':400,
    'Burger':60,
    'Pasta':110,
    'Salad':50,
    'Momos':90,
    'Coffee':40,
}

print("Welcome to Restraunt")

print("Pizza: Rs400\nBurger: Rs60\nPasta: Rs60\nSalad: Rs50\nMomos: Rs90\nCoffee: Rs40")

total_order = 0

item1 = input("Enter the name of item you want to order = ")
if item1 in menu:
    total_order += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Order item {item1} is not available yet")

another_order = input("Do you want to add another item? (Yes/NO)")
if another_order == "Yes":
    item2 = input("Enter second item : ")
    if item2 in menu:
        total_order += menu[item2]
        print(f"Item {item2} has been added to order")    
    else:
        print(f"Ordered item {item2} is not avaialable")       

print(f"The total amount of items to pay {total_order}")         