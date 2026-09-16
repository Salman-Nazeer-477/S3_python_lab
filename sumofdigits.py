num = int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
    sum = sum + temp % 10
    temp = temp//10
print(f"Sum of digits of {num} is {sum}")