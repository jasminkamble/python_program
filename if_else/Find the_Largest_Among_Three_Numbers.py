n1 =int(input("enter a number 1:-"))
n2 =int(input("enter a number 2:-"))
n3 =int(input("enter a number 3:-"))

if n1>n2 and n1>n3:
    print("Number 1 is greater then n2 and n3")
elif  n2>n1 and n2>n3: 
    print("Number 2 is greater then n1 and n3") 
elif n3>n1 and n3>n2:   
    print("Number 3 is greater then n1 and n2")  
else:
    print("May be the number are same")    