from abc import ABC
  
# abstract base class    
class Vehicle(ABC):    
  
    def start(self):    
        pass    
 

    def stop(self):    
        pass    
  
# child class    
class Car(Vehicle):    
  
    def start(self):    
        print("Car is starting with a key ignition.")    
  
    def stop(self):    
        print("Car is stopping using the brake.")    
  

my_car = Car()    
my_car.start()    
my_car.stop()    
