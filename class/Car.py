class Car:
    """Displaying the car information """
    def __init__(self, make, model, year):
        self.make = make
        self.model  =model
        self.year = year
        self.odometer=0

    def descriptive(self):
        """Display the car information"""
        long_name  = str(self.year)+' '+self.model+'  '+self.make
        return  long_name.title()
    def odometer_display(self):
        """Displaying the Speed on the console"""
        return f"This car has {str(self.odometer)} miles on it."

new_car = Car("Audi","A8",2025)
print(new_car.descriptive())
print(new_car.odometer_display())
new_car.odometer=55
print(new_car.odometer_display())