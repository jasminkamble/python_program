class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print("person name:-",self.name)
        print("age:-",self.age)

p1= person("no_one","21")
p2= person("rohan","45")

p1.show_details()
p2.show_details()


