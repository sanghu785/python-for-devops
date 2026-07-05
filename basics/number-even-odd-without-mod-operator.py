#program for printing even odd without mod operator.
#using bitwise operator:
number = int(input("enter a number"))
bit = number & 1
if bit:
    print("number is odd")
else:
    print("number is even")

# using // operator

if (number//2)*2 == number:
    print("number is even")
else:
    print("number is odd")

# USING STRING:
str_num = str(number)
if str_num[-1] in "02468":
    print("number is even")
else:
    print("number is odd")


