from Engine.Color import Color

class Style(dict):
    """[GUI] Настройка цветов для GUI элементов"""

    def __init__(self):
        """[GUI] Настройка цветов для GUI элементов"""
        super().__init__({
			"text": Color.rgbText(196, 196, 196),
			"textF": Color.rgbText(255, 255, 255),

			"background": Color.rgbBackground(127, 127, 127),
			"backgroundF": Color.rgbBackground(0, 0, 0),

            "disable": Color.rgbBackground(0, 0, 0)
		})

    def importFromConfig(self, cfg):
        """Иморт стилей из файла конфигураций"""
        for param in ["text", "textF"]:
            rgb = cfg["STYLE"][param].split(" ")
            self[param] = Color.rgb(rgb[0], rgb[1], rgb[2])

        for param in ["background", "backgroundF", "disable"]:
            rgb = cfg["STYLE"][param].split(" ")
            self[param] = Color.Background.rgb(rgb[0], rgb[1], rgb[2])
