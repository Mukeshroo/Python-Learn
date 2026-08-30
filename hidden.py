"""a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)

a = [1, 2 , 2]
b = [1, 2, 2]

print(a == b)
print(2 is 2)"""


for i in range(1,11):
    print(i,"new")
    if ( i == 4):
        continue
    print(i) 
print(i,"last")   