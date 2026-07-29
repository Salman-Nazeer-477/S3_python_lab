a = int(input('enter first number:'))
b = int(input('enter second number:'))
c = int(input('enter third number:'))
largest = a if a > b and a > c else b if b > c else c
print(f"largest number is {largest}")