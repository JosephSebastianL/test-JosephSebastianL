Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ValueError

1 rectangle_area(-3, 4)

<ipython-input-1> in rectangle_area(a, b)
      1 def rectangle_area(a, b):
      2   if a<0 or b<0:
      3     raise ValueError("if either number was negative")
      4   return a*b

ValueError: if either number was negative
