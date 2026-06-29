subjects = {'physics', 'chemistry', 'english', 'biology', 'computer', 'maths'}  
print("Given Set:", subjects)  
print("\n")

#remove():This method allow us to remove a specific element from the set. It will raise a KeyError if the element is not found in the given set.
subjects.remove('computer')
print("removing computer subject from the set by remove fun^n:-",subjects)
print('\n')

#discard():This method is also used to remove a specified element from the set; however, it does not raise any error if the element is not found.
subjects.discard("english")
print("removing computer subject from the set by discard fun^n:-",subjects)
print("\n")

#pop():This method is used to remove and returns a random element from the set.
subjects.pop()
print("removing the random elements from the set using pop:-",subjects)
print("\n")

# removing all elements from the set  
subjects.clear()
print("removing all the element from the given set using clear:-",subjects)