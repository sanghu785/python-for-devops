# convert to celcisu and back 
print("press 1 for cg to fn and 2 for otherway around")
choice = int(input())
print("enter temprature")
temprature = int(input())

if choice == 1:
    answer = (temprature*(9/5))+32
else:
    answer = (temprature-32)*(5/9)

print(answer)