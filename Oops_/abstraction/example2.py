from abc import ABC, abstractmethod    
  
class Device(ABC):    
   
    def brand(self):    
        pass    
  
class Mobile(Device):    
        
    def brand(self):    
        return "Samsung"    
  
m = Mobile()    
print(m.brand())    