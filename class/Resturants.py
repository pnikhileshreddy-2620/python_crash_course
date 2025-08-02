class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type =cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"Hi {self.restaurant_name} and the cuisine type present in restaurant is {self.cuisine_type}")
    def open_restaurant(self):
        print("Hi RESTAURANT IS OPEN NOW")
    def increment_served(self,number):
        self.number_served += number

restaurant = Restaurant("Spice Hub", "Indian")
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_served(25)
print(f"Customers served: {restaurant.number_served}")
restaurant.increment_served(2)
print(f"Customers served: {restaurant.number_served}")