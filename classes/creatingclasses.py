class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1,2)
point.draw()


class Tree:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    

    def color(self):
        print("Color")

tree= Tree(2,3)
tree.color()
