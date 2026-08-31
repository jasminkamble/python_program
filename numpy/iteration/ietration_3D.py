import numpy as n

var =n.array([[[1,2,3],[5,6,7]]])
for i in var:
    for x in i:
        for z in x:
            print(z)



print("\nby using built in function:-") 

for i in n.nditer(var):
    print(i)