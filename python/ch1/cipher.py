lower_case = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(s):
    encrypted_s = ''
    for char in s:
        if char in lower_case:
            encrypted_s += chr(219 - ord(char))
        else:
            encrypted_s += char
    return encrypted_s

def decrypt(s):
    decrypted_s = ''
    for char in s:
        if char in chr(219 - ord(char)):
            decrypted_s += chr(219 - ord(char))
        else:
            decrypted_s += char
    return decrypted_s

if __name__ == '__main__':
    s = input()
    print(encrypt(s))
    print(decrypt(s))

