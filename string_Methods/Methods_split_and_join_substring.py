str = "apple,banana,mango"

print(str.split(","))                
print(str.rsplit(",", 2))            
print(str.partition("--"))          

fruits = ["apple", "banana", "mango"]
print(" | ".join(fruits))      