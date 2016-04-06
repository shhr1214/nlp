symbols = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split(" ")

nums = {1, 5, 6, 7, 8, 9, 15, 16, 19}
dict = {}

for i in range(len(symbols)):
    if i+1 in nums:
        dict[symbols[i][0]] = i + 1
    else:
        dict[symbols[i][0:2]] = i + 1

print(dict)
