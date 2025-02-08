import re

class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def from_rgb(rgb: str):
        try:
            parts = list(map(int, rgb.split(',')))
            if len(parts) == 3 and all(0 <= p <= 255 for p in parts):
                return Color(*parts)
        except ValueError:
            pass
        raise ValueError("Invalid RGB format")

    @staticmethod
    def from_hex(hex_str: str):
        if not re.fullmatch(r"#[0-9A-Fa-f]{6}", hex_str):
            raise ValueError("Invalid HEX format")
        return Color(*(int(hex_str[i:i + 2], 16) for i in (1, 3, 5)))

    def to_foreground_ansi(self):
        return f"\033[38;2;{self.r};{self.g};{self.b}m"

    def to_background_ansi(self):
        return f"\033[48;2;{self.r};{self.g};{self.b}m"

def apply_ansi(text: str, ansi_code: str) -> str:
    return f"{ansi_code}{text}\033[0m"

class ColoredStr:
    def __init__(self, value: str):
        self.value = value

    def color(self, color: str) -> 'ColoredStr':
        try:
            c = Color.from_hex(color) if color.startswith('#') else Color.from_rgb(color)
            return ColoredStr(apply_ansi(self.value, c.to_foreground_ansi()))
        except ValueError:
            return self

    def bg_color(self, color: str) -> 'ColoredStr':
        try:
            c = Color.from_hex(color) if color.startswith('#') else Color.from_rgb(color)
            return ColoredStr(apply_ansi(self.value, c.to_background_ansi()))
        except ValueError:
            return self

    def bold(self) -> 'ColoredStr':
        return ColoredStr(apply_ansi(self.value, "\033[1m"))

    def italic(self) -> 'ColoredStr':
        return ColoredStr(apply_ansi(self.value, "\033[3m"))

    def underline(self) -> 'ColoredStr':
        return ColoredStr(apply_ansi(self.value, "\033[4m"))

    def strikethrough(self) -> 'ColoredStr':
        return ColoredStr(apply_ansi(self.value, "\033[9m"))

    def dim(self) -> 'ColoredStr':
        return ColoredStr(apply_ansi(self.value, "\033[2m"))

    def invert(self) -> 'ColoredStr':
        return ColoredStr(apply_ansi(self.value, "\033[7m"))

    def __str__(self):
        return self.value

    def __format__(self, format_spec):
        return str(self)

def colored_string(value: str) -> ColoredStr:
    return ColoredStr(value)


def apply_color_to_str():
    setattr(str, 'color', lambda self, color: ColoredStr(self).color(color))
    setattr(str, 'bg_color', lambda self, color: ColoredStr(self).bg_color(color))
    setattr(str, 'bold', lambda self: ColoredStr(self).bold())
    setattr(str, 'italic', lambda self: ColoredStr(self).italic())
    setattr(str, 'underline', lambda self: ColoredStr(self).underline())
    setattr(str, 'strikethrough', lambda self: ColoredStr(self).strikethrough())
    setattr(str, 'dim', lambda self: ColoredStr(self).dim())
    setattr(str, 'invert', lambda self: ColoredStr(self).invert())

apply_color_to_str()
