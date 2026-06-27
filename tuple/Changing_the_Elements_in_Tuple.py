fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
print("given tuple:-",fruits_tuple)
print("\n")
fruits_list= list(fruits_tuple)

fruits_list[3]="bluebarry"
print("Converting:-", fruits_tuple[3], "=>", fruits_list[3])  
print("\n")

fruits_tuple=tuple(fruits_list)
print("after chaning the element of tule with the help of list")
print("\n")
 
print("fruits_tuple=",fruits_tuple)