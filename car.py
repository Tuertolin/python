"""This is a class for Car's"""
      
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
