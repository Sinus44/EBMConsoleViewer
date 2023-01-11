from Engine.Input import Input
from Engine.Events import Events

class Element(Events):
    """[GUI] База для GUI элементов"""
    
    def __init__(self, screen, style, x=0, y=0, text="", enable=True, visible=True):
        """[GUI] База для GUI элементов"""
        self.screen = screen
        self.style = style
        self.x = x
        self.y = y
        self.text = text
        self.focused = False
        self.intersectionLen = len(text)
        self.enable = enable
        self.visible = visible

    def block(self):
        """Блокировка элемента"""
        self.focused = False
        self.enable = False

    def intersectionFromEvent(self, event):
        """Проверка на пересечение с мышью из события"""
        if self.enable:
            if event.type == Input.Types.Mouse:
                if event.mouseType == Input.Mouse.MOVE:
                    self.intersection(event.mouseX, event.mouseY)

    def intersection(self, x, y):
        """Проверка на пересечение по координатам"""
        if self.enable:
            if (self.x <= x < self.x + self.intersectionLen) and (self.y == y):
                self.focused = True
                self.focus(self)
            else:
                self.focused = False
