list_a =[34.6,67,89,"one",4+7j,"ram",67]

# remove(value): Removes the first occurrence of the value.
list_a.remove(67)
print("removing the firt occurrence of 67 from the list using remove fun^n\n",list_a)
print("\n")

# pop(index): Removes the element at a specific index (or the last element by default).
list_a.pop()
print("remove the last element by default\n",list_a)
print("\n")

list_b=[34.8,98,90,"one",4+9j,98]
list_b.pop(3)
print("Removes the element at a specific index\n",list_b)
print("\n")

del list_b[0]
print("deliting the list")