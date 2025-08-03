class SubtitleGeneratorClient:
    def __init__(
        self,
        width: int = 1080,
        height: int = 1920,
        font_name: str = "Bubblegum Sans",
        font_size: int = 60,
        primary_colour: str = "&H00FFFFFF",
        bold: int = 0,
        italic: int = 0,
        alignment: int = 2,
        margin_lr: int = 10,
        margin_v: int | None = None,
    ):
        self.width = width
        self.height = height
        self.font_name = font_name
        self.font_size = font_size
        self.primary_colour = primary_colour
        self.bold = bold
        self.italic = italic
        self.alignment = alignment
        self.margin_lr = margin_lr
        self.margin_v = margin_v or int(height * 0.3)
