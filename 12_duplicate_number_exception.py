numbers = list(map(int, input("Enter the numbers: ").split()))
try:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                raise Exception("Duplicate number found: " + str(numbers[i]))
    print("No duplicate numbers found.")
except Exception as e:
    print(e)