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

m = Mammal()
print(isinstance(Mammal,Animal))
issubclass