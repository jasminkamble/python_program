from multipledispatch import dispatch

class calculator:

    @dispatch(int,int)
    def add(self,a,b):
        return a+b
    
    @dispatch(float,int)
    def add(self,a,b):
        return a+b
    
    @dispatch(float,float)
    def add(self,a,b):
        return a+b
    

    @dispatch(str,str)
    def add(self,a,b):
        return a+b

cal = calculator()

print(cal.add(4,6))
print(cal.add(4.5,6.7))
print(cal.add(4.5,6))
print(cal.add("tpoint","tech"))



