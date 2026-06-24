print("printing number")
for a in range(1,100):
    print(a)
    a=a+1

print("printing table")
for t in range(1,11):
    print("10*",t,"=",10*t)
    t=t+1

print("printing odd number\n")
for i in range(1,11,2):
    print(i,end=" ")
    continue    

print("printing even number\n")
for i in range(2,11,2):
    print(i,end=" ")
    continue   

print("printing even number\n")
for i in range(1,100):
    if i%2==0:
        print(i,end=" ")
        continue
    

print("printing odd number")
for i in range(1,100):
    if i%2!=0:
        print(i,end=" ")
        continue    