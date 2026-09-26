# 1 - 2 + 3 - 4 ...... n

n = int(input("Enter no. of terms:"))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
