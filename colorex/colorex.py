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


class Colorize:
    def __init__(self, value: str):
        self.value = value

    def color(self, color: str) -> 'Colorize':
        try:
            c = Color.from_hex(color) if color.startswith('#') else Color.from_rgb(color)
            return Colorize(apply_ansi(self.value, c.to_foreground_ansi()))
        except ValueError:
            return self

    def bg_color(self, color: str) -> 'Colorize':
        try:
            c = Color.from_hex(color) if color.startswith('#') else Color.from_rgb(color)
            return Colorize(apply_ansi(self.value, c.to_background_ansi()))
        except ValueError:
            return self

    def bold(self) -> 'Colorize':
        return Colorize(apply_ansi(self.value, "\033[1m"))

    def italic(self) -> 'Colorize':
        return Colorize(apply_ansi(self.value, "\033[3m"))

    def underline(self) -> 'Colorize':
        return Colorize(apply_ansi(self.value, "\033[4m"))

    def strikethrough(self) -> 'Colorize':
        return Colorize(apply_ansi(self.value, "\033[9m"))

    def dim(self) -> 'Colorize':
        return Colorize(apply_ansi(self.value, "\033[2m"))

    def invert(self) -> 'Colorize':
        return Colorize(apply_ansi(self.value, "\033[7m"))

    def __str__(self):
        return self.value

    def __format__(self, format_spec):
        return str(self)

def colored_string(value: str) -> Colorize:
    return Colorize(value)
