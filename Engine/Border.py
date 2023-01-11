from Engine.Style import Style

class Border:
    """[GUI] Рамка для изображения"""
    
    def __init__(self, screen, style, symbol="*"):
        """[GUI] Рамка для изображения"""
        self.screen = screen
        self.style = style
        self.symbol = symbol
        
    def draw(self):
        """Отрисовка"""
        self.screen.rect(0, 0, self.screen.w, self.screen.h, self.style["text"] + self.style["background"] + self.symbol)