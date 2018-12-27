tet =30
def mod(num1, num2):
    tet= num1%num2
    print("Inside a function local tet: ",tet)
    return tet
mod(50, 20)
print("Outside a function global tet: ",tet)