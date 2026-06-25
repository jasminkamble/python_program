list_a=[54,87,6.7,"one","two",5+6j]

# print("append(): Adds a single element to the end of the list.")
list_a.append("add")
print("adding add word by using append\n",list_a)
print("\n")

# print("insert(): Inserts an element at a specific index.")
list_a.insert(1,6+8j)
print("adding \'5+6i\' to the frist position using insert\n",list_a)
print("\n")

# extend(): Adds multiple elements to the end of the list.
list_a.extend(["float",135,98.5])
print("addimg multiple element to the list  using extend\n",list_a)