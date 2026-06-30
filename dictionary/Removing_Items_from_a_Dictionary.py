dict_x = {  
    "name": "Sachin",   
    "age": 18,   
    "gender": "male",   
    "profession": "student"  
    }  
print("Given dictionary:",dict_x)
print("\n")

print("del: This keyword is used to remove an item by key.")
del dict_x["gender"]
print("update dictoinary (remove gender)",dict_x)
print("\n")

print("pop(): This method is used to remove an item by key. It also returns the value of the removed item.")
pop_age = dict_x.pop("age")
print("update dictoinary(remove age)",dict_x)
print("pop_age:-",pop_age)
print("\n")

print("popitem(): This method removes and returns the last 'key: value' pair.")
poped_item =dict_x.popitem()
print("update dictoinary(remove last item):-",dict_x)
print("poped_item:-",poped_item)
print("\n")

print("clear(): This method is used to remove all items from the dictionary.")
dict_x.clear()   
print("Update Dictionary (Removed all items):", dict_x)  