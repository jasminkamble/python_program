# reading the file
'''f=open("palindrom.py")
print(f.read())'''

# readline 
'''f =open("palindrom.py")
print(f.readline(5))'''

# wtriing in the file (remove previsou data and add new one)
'''f =open("palindrome.py","w")
f.write("run it \a")'''

# appending (adding data without removing previous one)
'''f =open("palindrome.py","a")
f.write("run it \a")'''

# file for appending and reading 
'''f =open("palindrome.py","a")
f.write("run it \a")
f= open("palindrome.py")
print(f.read())'''

# file for writing and reading
'''f =open("palindrome.py","a")
f.write("run it \a")
f= open("palindrome.py")
print(f.read())'''

