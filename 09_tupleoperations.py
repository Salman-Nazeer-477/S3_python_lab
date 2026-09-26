t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print("Original tuple:")
print(t1)
half = len(t1) // 2
print("Printing halves in two lines:")
print(t1[:half])
print(t1[half:])

t2 = tuple([i for i in t1 if i % 2 == 0])
print("Tuple of even values:")
print(t2)

t3 = (11, 13, 15)
print(f"Concatenate {t3} with {t1}:")
t4 = t1 + t3
print(t4)

print("Maximum and minimum values:")
print(max(t1))
print(min(t1))