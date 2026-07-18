class cal1:
    def add(self, a,b ):
        return a+b

class cal2:
    def sub(self,a,b):
        return a-b

class result(cal1,cal2):
    def ans(self):
        print("printing add and sub")        

c = result()
c.ans()
print("addition:-",c.sub(10,20))
print("substraction:-",c.add(10,20))       


# cheking class relationship
print(issubclass(result,cal1))
print(issubclass(cal1,result))

#cheking class and object relation
print(isinstance)