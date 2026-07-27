class calculator:
    def add(self,*args):
        return sum(args)

cal = calculator()

print(cal.add(6)) # single argument  
print(cal.add(6, 12)) # two arguments  
print(cal.add(6, 12, 18)) # three arguments    