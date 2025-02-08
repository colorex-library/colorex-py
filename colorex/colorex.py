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


class ColoredStr:
    def __init__(self, value: str):
        self.value = value

    def color(self, color: str) -> 'ColoredStr':
        try:
            c = Color.from_hex(color) if color.startswith('#') else Color.from_rgb(color)
            return ColoredStr(self.apply_ansi(c.to_foreground_ansi()))
        except ValueError:
            return self

    def bg_color(self, color: str) -> 'ColoredStr':
        try:
            c = Color.from_hex(color) if color.startswith('#') else Color.from_rgb(color)
            return ColoredStr(self.apply_ansi(c.to_background_ansi()))
        except ValueError:
            return self

    def bold(self) -> 'ColoredStr':
        return ColoredStr(self.apply_ansi("\033[1m"))

    def italic(self) -> 'ColoredStr':
        return ColoredStr(self.apply_ansi("\033[3m"))

    def underline(self) -> 'ColoredStr':
        return ColoredStr(self.apply_ansi("\033[4m"))

    def strikethrough(self) -> 'ColoredStr':
        return ColoredStr(self.apply_ansi("\033[9m"))

    def dim(self) -> 'ColoredStr':
        return ColoredStr(self.apply_ansi("\033[2m"))

    def invert(self) -> 'ColoredStr':
        return ColoredStr(self.apply_ansi("\033[7m"))

    def __str__(self):
        return self.value

    def apply_ansi(self, ansi_code: str) -> str:
        return f"{ansi_code}{self.value}\033[0m"


def colored_string(value: str) -> ColoredStr:
    return ColoredStr(value)


def apply_color_to_str():
    def color(self, color: str) -> ColoredStr:
        return ColoredStr(self).color(color)

    def bg_color(self, color: str) -> ColoredStr:
        return ColoredStr(self).bg_color(color)

    def bold(self) -> ColoredStr:
        return ColoredStr(self).bold()

    def italic(self) -> ColoredStr:
        return ColoredStr(self).italic()

    def underline(self) -> ColoredStr:
        return ColoredStr(self).underline()

    def strikethrough(self) -> ColoredStr:
        return ColoredStr(self).strikethrough()

    def dim(self) -> ColoredStr:
        return ColoredStr(self).dim()

    def invert(self) -> ColoredStr:
        return ColoredStr(self).invert()

    setattr(str, 'color', color)
    setattr(str, 'bg_color', bg_color)
    setattr(str, 'bold', bold)
    setattr(str, 'italic', italic)
    setattr(str, 'underline', underline)
    setattr(str, 'strikethrough', strikethrough)
    setattr(str, 'dim', dim)
    setattr(str, 'invert', invert)

# 초기화 시 apply_color_to_str 호출
apply_color_to_str()
