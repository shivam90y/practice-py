tet= 20
def sub(num1,num2):
   tet= num1-num2
   print("Inside a function local tet: ",tet)
   return tet
sub(50, 10)
print("Outside a function global tet: ",tet)


