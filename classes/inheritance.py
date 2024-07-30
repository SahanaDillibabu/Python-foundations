class Animal:
      def __init__(self):
          self.age = 1
      def eat(self):
        print("eat")

#animal: parent, base
#mammal: child, sub
class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)