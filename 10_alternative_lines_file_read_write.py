def copy_odd_lines():
    file1 = open("file1.txt", "r")
    file2 = open("file2.txt", "w")
    line_number = 1
    for line in file1:
        if line_number % 2 != 0:
            file2.write(line)
        line_number = line_number + 1
    file1.close()
    file2.close()
copy_odd_lines()
print("Odd numbered lines copied successfully.")