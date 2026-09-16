import numpy as np
while True:
    print(
"""
Menu
1. Create an array
2. Find max and min
3. Find dot product
4. Reshape a 1D array to 2D array
5. Exit
"""
)
    choice = int(input("Enter your choice:"))
    match choice:
        case 1:
            r = int(input("Enter number of rows:"))
            c = int(input("Enter number of columns:"))
            arr = np.ones((r * c), dtype = int)
            print("Array filled with 1s = \n", arr)
        case 2:
            n = int(input("Enter number of elements:"))
            arr = np.array([int(input(f"Enter element {i + 1} = ")) for i in range(n)])
            print("Max. value", np.max(arr))
            print("Min. value", np.min(arr))
        case 3:
            n = int(input("Enter number of elements in arrays:"))
            arr1 = np.array([int(input(f"Enter element {i + 1} for first array:")) for i in range(n)])
            arr2 = np.array([int(input(f"Enter element {i + 1} for second array:")) for i in range(n)])
            print("Dot product:", np.dot(arr1, arr2))
        case 4:
            n = int(input("Enter total number of elements:"))
            arr = np.array([int(input(f"Enter element {i + 1}:")) for i in range(n)])
            r = int(input("Enter number of rows:"))
            c = int(input("Enter number of columns:"))
            if r * c == n:
                new_arr = arr.reshape(r, c)
                print("Reshaped 2-D array:\n", new_arr)
            else:
                print("Reshape not possible")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice!")