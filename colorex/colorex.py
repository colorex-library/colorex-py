class StyledString:
    def __init__(self, text: str):
        self.text = text

    def color(self, color: str) -> 'StyledString':
        color_obj = Color.from_rgb(color) if ',' in color else Color.from_hex(color)
        if color_obj:
            self.text = f"\x1b[38;2;{color_obj.r};{color_obj.g};{color_obj.b}m{self.text}\x1b[0m"
        return self

    def bg_color(self, color: str) -> 'StyledString':
        color_obj = Color.from_rgb(color) if ',' in color else Color.from_hex(color)
        if color_obj:
            self.text = f"\x1b[48;2;{color_obj.r};{color_obj.g};{color_obj.b}m{self.text}\x1b[0m"
        return self

    def bold(self) -> 'StyledString':
        self.text = f"\x1b[1m{self.text}\x1b[0m"
        return self

    def italic(self) -> 'StyledString':
        self.text = f"\x1b[3m{self.text}\x1b[0m"
        return self

    def underline(self) -> 'StyledString':
        self.text = f"\x1b[4m{self.text}\x1b[0m"
        return self

    def strikethrough(self) -> 'StyledString':
        self.text = f"\x1b[9m{self.text}\x1b[0m"
        return self

    def dim(self) -> 'StyledString':
        self.text = f"\x1b[2m{self.text}\x1b[0m"
        return self

    def invert(self) -> 'StyledString':
        self.text = f"\x1b[7m{self.text}\x1b[0m"
        return self

    def __str__(self):
        return self.text


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def from_rgb(rgb: str):
        parts = rgb.split(',')
        if len(parts) == 3:
            try:
                r = int(parts[0])
                g = int(parts[1])
                b = int(parts[2])
                return Color(r, g, b)
            except ValueError:
                return None
        return None

    @staticmethod
    def from_hex(hex: str):
        if len(hex) == 7 and hex.startswith('#'):
            try:
                r = int(hex[1:3], 16)
                g = int(hex[3:5], 16)
                b = int(hex[5:7], 16)
                return Color(r, g, b)
            except ValueError:
                return None
        return None


# Helper function to make string stylable
def stylize(text: str) -> StyledString:
    return StyledString(text)
