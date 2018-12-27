tet=30
def div(num1, num2):
    tet=num1/num2
    print("Inside a function local tet: ",tet)
    return tet
div(40, 10)
print("Outside a function global tet: ",tet)