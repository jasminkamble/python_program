class animal:
    def speak(self):
        print("animal speaking")

class dog(animal):
    def bark(self):
        print("bark")

class dogchild(dog):
    def eat(self):
        print("dog child doing nothing") 


d= dogchild()
d.speak()
d.bark()
d.eat()

