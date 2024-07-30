class Animal:
      def __init__(self):
          print("Animal Constructor")
          self.age = 1
      def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
          print("Mammal Constructor")
          self.weight = 2
          super().__init__()
          #overrides constructor defined in class Animal, use super

m = Mammal()
print(m.age)
print(m.weight)