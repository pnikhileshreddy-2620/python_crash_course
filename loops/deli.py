
sandwich_orders = [
    "Club Sandwich",
    "BLT",
    "Grilled Cheese",
    "Ham & Swiss",
    "Tuna Melt",
    "Egg Salad Sandwich",
    "Turkey & Avocado",
    "Roast Beef & Cheddar",
    "Caprese Sandwich",
    "Cuban Sandwich",
    "Reuben",
    "Croque Monsieur",
    "Banh Mi",
    "Italian Sub",
    "Philly Cheesesteak",
    "French Dip",
    "Chicken Caesar Wrap",
    "Falafel Pita",
    "Shawarma Wrap",
    "Paneer Tikka Roll",
    "Veggie Hummus Wrap",
    "BBQ Chicken Wrap",
    "Greek Gyro",
    "Avocado & Sprout Sandwich",
    "Grilled Veggie Panini",
    "Chickpea Salad Sandwich",
    "Tofu Banh Mi",
    "Mushroom Melt",
    "Vegan BBQ Jackfruit Sandwich",
    "Hummus & Roasted Red Pepper"
]

finished_sandwiches=[]


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Such as I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)