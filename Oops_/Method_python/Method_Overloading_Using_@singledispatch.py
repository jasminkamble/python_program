from functools import singledispatchmethod 

class calculator:


    @singledispatchmethod  
    def add(self,a,b):
        print("Default method")
        raise NotImplementedError("Unsupported Data Type")  

    @add.register
    def _(self, a: int, b: int) -> int:
        return a+b  
        
    def _(self, a: float, b: float) -> float:
        return a+b     

cal = calculator()

print(cal.add(23,7))
print(cal.add(23.0,7.9))
try:
    print(cal.add("no","one"))
except NotImplementedError as E:
    print(E)

