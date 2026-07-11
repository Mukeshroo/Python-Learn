a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

choise = int(input("1.add\n2.sub\n3.mul\n4.div\n5.choose one: "))

if choise == 1:
    print("add total",a+b)
elif choise == 2:
    print("sub total",a-b)
elif choise == 3:
    print("mul total",a*b)
elif choise == 4:
    if b == 0:
        print("it not devide")
    else:
        print("div",a/b)