from Engine.Element import Element

class Label(Element):
    """[GUI] Текст"""
    
    def draw(self):
        """Отрисовка"""
        if self.visible:
            self.screen.text(self.text[:40], self.x, self.y, wordPrefix=self.style["background"] + self.style["text"])