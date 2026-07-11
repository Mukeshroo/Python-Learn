n = int(input("enter the number to check it is prime or not: "))
if(n<=1):
    print("its not prime")

else:
    for i in range(2,n):
        if(n%i==0):
            print("its not prime")
            break
        else:
            print("its prime")

