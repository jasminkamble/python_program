str = "musca domestica"

print(str.find("a"))  
print(str.index("m"))  #Similar to find(), but raises a ValueError if the substring is not found.
print(str.rfind("a"))
print(str.rindex("m"))
print(str.startswith("m"))
print(str.endswith("a"))
print(str.count(" "))
