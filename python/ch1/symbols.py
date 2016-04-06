symbols = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split(" ")

nums = {1, 5, 6, 7, 8, 9, 15, 16, 19}

for i in range(len(symbols)):
    if i+1 in nums:
        print(symbols[i][0])
    else:
        print(symbols[i][0:2])
