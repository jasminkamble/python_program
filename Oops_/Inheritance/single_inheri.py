class animal:
    def speak(self):
        print("animal speacking")

class dog(animal):
    def bark(self):
        print("bark")

c = dog()
c.speak()
c.bark()        
    