class simple_calculator:
    def add(self,a,b=0,c=0):
        return a+b+c

cal= simple_calculator()

print("one argument:-",cal.add(4))
print("two argument :-",cal.add(2,6))
print("three argument:-",cal.add(1,125,27))    