swap = int(input("Enter the ATM PIN: "))

rev = 0

while swap > 0:
    digit = swap % 10
    rev = rev * 10 + digit
    swap = swap // 10

print("Reversed PIN:", rev)