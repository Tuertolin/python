class Dog:
    """This is my first class, call dog"""
    
    def __init__(self, name, age):
        """Initializing name and age attributes """
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate dog respond to a command"""
        print(f"{self.name} is now sitting!")
        
    def roll_over(self):
        """Simulate dog respond to a command"""
        print(f"{self.name} is rolled over !")
      
class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.price = 0
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} km on it")
        
    def update_odometer(self, kms):
        if kms >=self.odometer_reading:
            self.odometer_reading = kms
        else:
            print("You can't roll back the odometer")
            
    def increment_odometer(self, kms):
        self.odometer_reading += kms

######## BASIC CLASS  #################
my_dog = Dog("Rame", 15)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}!")
my_dog.sit()

print(f"My dog's name is {your_dog.name}!")
#######################################################

my_car = Car("Holden", "Nomeacuerdo", 2015)
print(my_car.get_descriptive_name())

######## CHILD CLASS FOR Car Parent   ###################

class ElectricCar(Car):
    """Represent aspects of Car"""
    
    def __init__(self, make, model, year):
        """initialize attributes from parent"""
        super().__init__(make, model,year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model X', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
