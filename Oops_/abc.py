from abc import ABC, abstractmethod    
  
class Device(ABC):    
    @property    
    @abstractmethod    
    def brand(self):    
        pass    
  
class Mobile(Device):    
    @property    
    def brand(self):    
        return "Samsung"    
  
m = Mobile()    
print(m.brand)    