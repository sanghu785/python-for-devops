# diffrence between "is" and "=="
var1 = [1,2]
var2 = [1,2]
if var1 == var2:
    print("both are equal")
else:
    print("both are not equal")

if var1 is var2:
    print("var1 is var2")
else:
    print("var1 is not var2")
