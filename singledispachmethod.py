from functools import singledispatchmethod

class calculator:

    @singledispatchmethod
    def add(self,a,b):
        raise NotImplementedError("unsported datatype")
    
    @add.register(int)
    def _(self,a:int,b:int) -> int :
        return a+b
    

    @add.register(float)
    def _(seelf,a:float,b:float) -> float:
        return a+b
    
cal = calculator()

print(cal.add(9,8))
print(cal.add(3.9,4.6))

try:
    print(cal.add("tpoint","tech"))
except NotImplementedError as E:
    print(E)    