from .colorex import ColoredStr

# 문자열이 자동으로 확장될 수 있도록 설정
str.__bases__ += (ColoredStr,)
