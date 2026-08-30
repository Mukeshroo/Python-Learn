""""num = [22,"mukesh",66.00,True,"Suraj"]
print(type(num))

num.append("janu")
print(num)
num.extend([55,22,"msk singh"])
print(num)
num.insert(2,"musa")
print(num)
num.remove("musa")
print(num)
num.pop()
print(num)
num.pop(5)
print(num)
num.reverse()
print(num)

n = [55,56,88,92,12,19,7]
n.sort()
print(n)

nu = n.copy()
print(nu)

print(max(nu))
print(min(nu))
print(sum(nu))
nu.sort()
print(nu)

add = nu[-1 ] + nu[-2]
print(add)"""

"""num1 = []
num2 = []
num = []

for i in range(0,5):
    val = int(input("enter the first numbe to add "))
    num1.append(val)
for i in range(0,5):
    val = int(input("enter the second numbe to add "))
    num2.append(val)
    num.append(num1[i]+num2[i])
print(num1)
print(num2)
print(num)"""

#even & odd

"""even = []
odd = []
for i in range (1,99):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)"""


"""num = (55,20,40,55,[20,40,"sonu"],"mukesh")
print(type(num))
print(num)
print(num[-1])
print(num[4])
print(num[4][0])
num[4][0]="msk singh"
print(num)"""

#find the common number from the list 

"""a = [12,55,36,88,66]
b = [56,12,37,66,77]
common = []
for i in a:
    if i in b:
        common.append(i)
print(common)"""


#Write a program to merge two lists.

"""list1 = [45,88,77,62,66]
list2= [45,88,99,32,66]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])

print(list3)"""

#palindrome

"""li = [1,2,1]
if li == li[::-1]:
    print("it is palindrome number")

else:
    print("it is not the palindrome number")"""

nums = [1, 2, 2, 3, 1, 2, 4, 3]

freq = {}

for i in nums:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print(freq)

