available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request in requested_toppings:
    if request in available_toppings:
        print("Adding "+ request+ ".")
    else:
        print(f"Sorry we don't have this {request} toppings")