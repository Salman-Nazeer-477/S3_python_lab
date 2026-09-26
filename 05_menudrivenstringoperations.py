s = input("Enter a string:")
while True:
    print(f"\nstring:{s}")
    print(
"""Menu
1. Frequency
2. Replace a character
3. Remove first occurence of a character
4. Remove all occurences of a character
5. Exit
"""
    )
    choice = int(input("Enter your choice:"))
    match(choice):
        case 5:
            print("Exiting")
            quit()
        case 1:
            ch = input("Enter character:")
            f = s.count(ch)
            print(f"Frequency of {ch} is {f}")
        case 2:
            old = input("Enter character to be replaced:")
            new = input("Enter new character:")
            s = s.replace(old, new)
        case 3: 
            ch = input("Enter character:")
            s = s.replace(ch, "", 1)
        case 4:
            ch = input("Enter character:")
            s = s.replace(ch, "")
            
