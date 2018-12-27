def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(6, 9)
multiply(3, 8)
multiply(5, 9,7)
multiply(5, 8,7)
multiply(5, 5, 5)
