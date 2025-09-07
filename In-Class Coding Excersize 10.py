total = 0
number = int(input("Enter a number: "))
while number != 0:
    print(f'{number = }')
    total = total + number
    print(f'{total = }')
    number = int(input("Enter a number: "))
print(total)