class Frame:
    """[GUI] Основа кадра и заливка фона"""
    
    def __init__(self, screen, style):
        """[GUI] База кадра и фона"""
        self.screen = screen
        self.style = style
    
    def draw(self):
        """Отрисовка"""
        self.screen.fill(self.style["background"] + " ")