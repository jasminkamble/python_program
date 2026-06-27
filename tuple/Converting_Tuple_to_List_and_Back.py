tuple_a = ("mango", "orange", "banana", "apple", "papaya")
print("given tuple:-",tuple_a)

tuple_lst = list(tuple_a)

tuple_lst.append("banana")
tuple_a =tuple(tuple_lst)
print(tuple_a)