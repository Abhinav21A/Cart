def get_price_of_item(item):
    if item == "item1":
        return 10.0
    elif item == "item2":
        return 20.0
    elif item == "item3":
        return 30.0
    else:
        return 0.0

# list to store the items in the cart
cart = []

# user input for adding items to the cart
while True:
    item = input("Enter item to add to cart (or 'done' to finish): ")
    if item == "done":
        break
    cart.append(item)

# user input for the price of each item in the cart
prices = {}
for item in cart:
    price = float(input("Enter the price of " + item + ": "))
    prices[item] = price

# user input for removing items from the cart
while True:
    item = input("Enter item to remove from cart (or 'done' to finish): ")
    if item == "done":
        break
    if item in cart:
        cart.remove(item)
        print(item + " removed from cart.")
    else:
        print(item + " not found in cart.")

# total cost of the items in the cart
total_cost = 0
for item in cart:
    match = False
    for key, value in prices.items():
        if key in item:
            total_cost += value
            match = True
            break
    if not match:
        print(item + " not found in prices.")

# Print the total cost of the items in the cart
print("Total cost of items in cart: $", total_cost)