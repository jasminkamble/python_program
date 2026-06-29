# A frozenset is an immutable version of a set, which means we cannot add or remove elements after it is created. It is created using the built-in frozenset() function.

set_a =frozenset(['one','two','three','four'])
print("frozenset =",set_a)

print(type(set_a))