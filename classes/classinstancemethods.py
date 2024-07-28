class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod #decorator
    def zero(cls):
        return cls(0,0) #creating a point object with initial values

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()