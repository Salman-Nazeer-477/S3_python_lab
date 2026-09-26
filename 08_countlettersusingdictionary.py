string = input("Enter string:")
dict_ch = {}
for ch in string:
    dict_ch[ch] = dict_ch.get(ch, 0) + 1
print(dict_ch)
    