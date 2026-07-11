n=[3,8,9,5,6,4,2]

is_even= filter(lambda a: a%2==0,n)
is_odd =filter(lambda b:b%2!=0 ,n)

print(list(is_even))
print(list(is_odd))
print(tuple(is_even))