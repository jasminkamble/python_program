import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for i in x:
        print(i)

print("\nby using built in function:-") 

for i in np.nditer(arr):
    print(i)