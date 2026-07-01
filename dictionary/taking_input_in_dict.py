dict_x={}

for i in range(2):
    key=input(str("enter the key:-"))
    value=input(str("enter the value:-"))
    dict_x[key]=value
    print(key,":",value)

print("dictionary :-",dict_x)

# for key in dict_x:
#     value = dict_x[key]
dict_x.pop(key)
print("after pop:-",dict_x)


