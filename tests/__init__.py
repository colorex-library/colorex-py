import colorex

print("Hello, World!".color("0,255,0"))  # Green text
print("Error!".color("#FF0000"))         # Red text

print("Bold Text".bold())                # Bold text
print("Italic Text".italic())            # Italic text
print("Underlined Text".underline())     # Underlined text
print("Strikethrough Text".strikethrough()) # Strikethrough text
print("Dim Text".dim())                  # Dim text
print("Inverted Text".invert())          # Inverted text

print("Background Color".bg_color("0,0,255")) # Blue background

print("ALL".color("0,255,0").bold().italic().underline().strikethrough().dim().invert().bg_color("0,0,255")) # All styles applied
