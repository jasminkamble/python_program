set_a={2,3,4}
print("set_a:=",set_a)
set_b ={1,4,5,6}
print("set_b=",set_b)
print("\n")

# union of set 
print("printing union of set a and set b by using two methods")
print("method 1: ",set_a|set_b)
print("method 2: ",set_a.union(set_b))
print("\n")

# Intersection of Sets
print("printing intersection of set a and set b by using two methods")
print("method 1: ",set_a & set_b)
print("method 2: ",set_a.intersection(set_b))
print("\n")

# Difference of Sets
print("printing difference of set a and set b by using two methods")
print("set_a - set_b")
print("method 1: ",set_a - set_b)
print("method 2: ",set_a.difference(set_b))
print("\n")

print("set_b - set_a")
print("method 1: ",set_b - set_a)
print("method 2: ",set_b.difference(set_a))
print("\n")
