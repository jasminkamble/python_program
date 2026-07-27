from abc import ABC
class flower(ABC):
    def tulip(self):
        pass

class details(flower):
    def tulip(self):
        print("red,blue,white")

d = details()
d.tulip()


