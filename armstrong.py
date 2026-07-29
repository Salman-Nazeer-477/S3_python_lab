num = input("Enter a number:")
sum = 0
for i in num:
    sum += int(i)**3
print(f"{num} is armstrong") if int(num) == sum else print(f"{num} is not armstrong")