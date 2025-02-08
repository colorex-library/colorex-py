# colorex-py

`colorex-py` is a simple and flexible Python Module that provides an easy way to style your terminal output with color and text formatting. With support for both RGB and HEX color codes, as well as text styles like bold, italic, underline, strikethrough, and more, it makes your terminal applications visually more appealing and readable.

## Features
* RGB Color Support: Define colors using RGB values (e.g., color_rgb(255, 0, 0)).
* HEX Color Support: Use HEX color codes (e.g., color_hex("#FF0000")).
* Text Styles: Bold, italic, underline, strikethrough, dim, and inverted text.
* Background Colors: Set the background color using RGB or HEX.
* Chainable API: Apply multiple styles in a single statement using method chaining.

## Installation

To install `colorex-py`, you can use pip:

```bash
pip install colorex
```

## Usage
Here's how you can use `colorex` to add color and styles to your terminal output:

```python
import colorex

# Basic color usage
print("{}", "Hello, World!".color("0,255,0"))  # Green text
print("{}", "Error!".color("#FF0000"))         # Red text

# Text styles
print("{}", "Bold Text".bold())                # Bold text
print("{}", "Italic Text".italic())            # Italic text
print("{}", "Underlined Text".underline())     # Underlined text
print("{}", "Strikethrough Text".strikethrough()) # Strikethrough text
print("{}", "Dim Text".dim());                  # Dim text
print("{}", "Inverted Text".invert())          # Inverted (background) text

# Background color
print("{}", "Background Color".bg_color("0,0,255")) # Blue background

# Combining multiple styles
print("{}", "ALL".color("0,255,0").bold().italic().underline().strikethrough().dim().invert().bg_color("0,0,255")) # All styles
```

## Supported Styles

* Color: RGB and HEX color formats.
* Text Styles:
    * bold()
    * italic()
    * underline()
    * strikethrough()
    * dim()
    * invert()
* Background Colors: bg_color() with RGB or HEX values.

## Example Output
The following example would result in a green-colored "Hello, World!" and a red "Error!" message in the terminal.

```python
print("{}", "Hello, World!".color("0,255,0"))  // Green text
print("{}", "Error!".color("#FF0000"))         // Red text
```

## Supported Color Formats
* RGB: `"r,g,b"` (e.g., `"255,0,0"` for red).
* HEX: `"#RRGGBB"` (e.g., `"#FF0000"` for red).

# License
This project is licensed under the MPL-2.0 License - see the [LICENSE](LICENSE) file for details.