import random
print("1=rock\n2=paper\n3=scissor")
choices=[1,2,3]
p1=int(input("enter your choise:-"))
p2=random.choice(choices)
print(p2)
if p1== 1 and p2==3 or p1==2 and p2==1 or p1==3 and p2==2:
    print("Player one  is winner!")
elif p1==1 and p2==2 or p1==2 and p2==3 or p1==3 and p2==1:
    print("player two wins!")
else:
    print("oops tie!")



    
