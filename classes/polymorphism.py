from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
#draw method takes several forms -> polymorphism