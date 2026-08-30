#table

'''for i in range(1,11):
    print(f"2 * {i} = {2*i}")'''

"""for i in range(1,11):
     print("*" * i)"""


rows = 5
for i in range( 1 , rows + 1 ):
    space = (" " * (rows - i))
    start = ("*" * (2*i -1))
    print(space + start)