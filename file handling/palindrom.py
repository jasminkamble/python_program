a = int(input("enter a number:-"))


n1 = a/100
n2 =(a/10)%10
n3 =(a%100)%10
rev = (n3*100) + (n2*10) +n1
print(rev)
if a == rev:
    print("the num is palindrom",a)

else:
    print("the num is not palindrom",a)    