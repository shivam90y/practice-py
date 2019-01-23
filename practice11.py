# Write a Python program to convert a tuple to a dictionary.

tuplex = ((9, "s"),(0, "h"),(8,"i"),(4,"v"),(7,"a"),(6,"m"))
print(dict((y, x) for x, y in tuplex))
