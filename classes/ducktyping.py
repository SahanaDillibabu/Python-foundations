from abc import ABC, abstractmethod

class TextBox:
    def draw(self):
        print("Textbox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

#ducktyping: only a "draw" method is needed for Python to achieve polymorphism - we don't need a common interface
#common interface is still a good practice