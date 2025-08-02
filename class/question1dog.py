class Dog:
    """A simple Dog class"""
    def __init__(self,name,age):
        """Initialize the name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name.title()} is sitting")
    def rolling(self):
        print(f"{self.name.title()} this dog is rolling on the grass")

road_dog = Dog("LUCK",2)
road_dog.sit()
