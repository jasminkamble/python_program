# Use a list to create a NumPy array:

import numpy as np
var = np.array([1,2,3,4,5])
print("list to numpy array(ndarray)",var)
print(type(var))
print("\n")


# use a tuple to create a numpy array:

import numpy as np
var = np.array([1,2,3,4,5])
print("tuple to numpy array(nparray)",var)
print(type(var))
print("\n")


#dimensions in array

import numpy as np 
var =  np.array(75)
var1 = np.array([1,2,3,4,5,6])
var2 = np.array([[3,4,5],[5,6,7]])
var3 = np.array([[[1,2,3],[5,6,7],[1,3,5]]])

print("array diamention:")
print("0D : ",var)
print("1D : ",var1)
print("2D : ",var2)
print("3D : \n",var3)

print("number of diamension:-")
print(var.ndim)
print(var1.ndim)
print(var2.ndim)
print(var3.ndim)

print("\n")

#Create an array with 5 dimensions and verify that it has 5 dimensions:
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=3)

print(arr)
print('number of dimensions :', arr.ndim)


