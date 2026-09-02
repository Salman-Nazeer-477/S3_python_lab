def is_even(num: int):
    if num % 2 == 0:
        return True
    return False

num = int(input("Enter a number:"))
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")