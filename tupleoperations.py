t0 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print("Original tuple:")
print(t0)
half = len(t0) // 2
print("Printing halves in two lines:")
print(t0[:half])
print(t0[half:])

t1 = (i for i in t0 if i % 2 == 0)
print("Tuple of even values:")
print(t1)

t2 = (11, 13, 15)
print(f"Concatenate {t2} with {t0}:")
t3 = t0 + t2
print(t3)

print("Maximum and minimum values:")
print(max(t0))
print(min(t0))