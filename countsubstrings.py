def find_substring(main, sub):
    indices = []
    start = 0
    while True:
        index = main.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    if indices:
        return indices
    else:
        return -1

main = input("Enter main string:")
sub = input("Enter substring:")
result = find_substring(main, sub)
print(result)