import colorex

# Example usage
print(stylize("Hello, World!").color("0,255,0"))  # Green text
print(stylize("Error!").color("#FF0000"))  # Red text

print(stylize("Bold Text").bold())  # Bold text
print(stylize("Italic Text").italic())  # Italic text
print(stylize("Underlined Text").underline())  # Underlined text
print(stylize("Strikethrough Text").strikethrough())  # Strikethrough text
print(stylize("Dim Text").dim())  # Dim text
print(stylize("Inverted Text").invert())  # Inverted background text

print(stylize("Background Color").bg_color("0,0,255"))  # Blue background

# Combining multiple styles
print(stylize("ALL")
      .color("0,255,0")
      .bold()
      .italic()
      .underline()
      .strikethrough()
      .dim()
      .invert()
      .bg_color("0,0,255"))  # All styles applied
