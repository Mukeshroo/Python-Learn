#find the largest number 
"""num = int(input("enter the number: "))
num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))

if(num > num1 and num> num2):
    print(num,"is largest")
elif(num1> num2 and num1>num):
    print(num1,"is largest")
else:
    print(num2,"is largest")"""


#reverse the number 

"""num = int(input("enter the number and reverse: "))
rev = 0
while num>0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev,"reverse number")"""

#for the factorial
"""num = int(input("enter the number for the factorial: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i
print(fact)"""

#for the prime number
""""num = int(input("enter the number for the : "))
count = 0
for i in range(1, num+1):
    if(num % i == 0):
        count = count + 1
if(count == 2):
    print("it is prime number")

else:
    print("it is not a prime number")"""

#arm strong number
"""num = int(input("enter the number for the : "))
imp = num 
di = 0
while num > 0:
    b = num % 10
    di = di + b ** 3 
    num = num // 10
if(di == imp):
    print(imp,"is is the armstrong ")
else:
    print("it is not armstrong mumber")"""

#print the number row and column
"""for i in range(1,10):
    for j in range(1,i+1):
        print("*",end="")
    print()"""
#print the ab row and column

"""for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()"""
    
"""for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)"""

"""a = "mukesh"
print(a[2:5])"""

#list 

"""a = ["mukesh",25,3.4]
print(a)
a[1] = 2 
print(a)
a[0] = 4
print(a)
print(a[2])
print(type(a))
print(len(a))
a[2] = True
print(type(a[2]))

print(a[-1])"""

num = [20,55,88,66,7,44,11,]
print(num[::-1])




