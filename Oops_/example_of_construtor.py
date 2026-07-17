class teacher:
    def __init__(self,name,subject):
        self.name =name
        self.sub = subject
    def info_T(self):
        print("printing teacher details:-")
        print(self.name)
        print(self.sub)   

class student:
    def __init__(self,name,rollno):
        self.name =name
        self.roll =rollno
    def info_s(self):
        print("printing teacher details:-")
        print(self.name)
        print(self.roll)       

s = student("rohan",25)
s1 = teacher("rohini","math")
s.info_s()
s1.info_T()
