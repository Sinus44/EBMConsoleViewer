from Engine.Logging import Logging

class Group:
    """[GUI] Группа GUI элементов"""

    def __init__(self, screen, x, y, interval=1, maxElements=10):
        """[GUI] Группа GUI элементов"""
        self.screen = screen
        self.x = x
        self.y = y
        self.elements = []
        self.interval = interval
        self.selected = {}
        self.maxElements = maxElements

    def append(self, element):
        """Добавление элементов в группу"""
        self.elements.append(element)
    
    def eventHandler(self, event):
        """Обработка событий для всех элементов в группе"""
        for element in self.elements:
            element.intersectionFromEvent(event)

            if hasattr(element, "inputFromEvent"):
                element.inputFromEvent(event)
    
    def click(self):
        """Обработка событий для всех элементов в группе"""
        for element in self.elements:
            if element.focused:
                element.click(element)
    
    def sort(self):
        """Автопозиционирование элементов группы"""
        for i in range(len(self.elements)):
            element = self.elements[i]
            element.x = self.x
            element.y = self.y + i * (self.interval + 1)

    def draw(self):
        """Отрисовка всех элементов группы"""
        for i in range(min(len(self.elements), self.maxElements)):
            self.elements[i].draw()