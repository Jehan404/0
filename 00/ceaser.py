def caesar_encrypt(text, key):
    res = ""
    for ch in text.lower():
        if ch.isalpha():
            base = ord('a')
            res += chr((ord(ch) - base + key) % 26 + base) //COCBK
        else:
            res += ch
    return res

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def caesar_bruteforce(cipher):
    for k in range(26):
        print(k, "=", caesar_decrypt(cipher, k))

msg = input("Enter message: ")
key = int(input("Enter key (0-25): "))

enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)

print("\nBruteforce:")
caesar_bruteforce(enc)

------------------------
def caesar_encrypt(text, key):
    text = text.lower()
    print("\nMappings used:")
    res = ""

    for ch in text:
        if ch.isalpha():
            base = ord('a')
            shifted_val = (ord(ch) - base + key) % 26
            encrypted = chr(shifted_val + base)

            print(f"{ch} + {key} = {encrypted}")

            res += encrypted
        else:
            res += ch

    return res


def caesar_decrypt(text, key):
    text = text.lower()
    print("\nReverse mappings:")
    res = ""

    for ch in text:
        if ch.isalpha():
            base = ord('a')
            shifted_val = (ord(ch) - base - key) % 26
            decrypted = chr(shifted_val + base)

            print(f"{ch} - {key} = {decrypted}")

            res += decrypted
        else:
            res += ch

    return res


def caesar_bruteforce(cipher):
    print("\nBruteforce attempts:")
    for k in range(26):
        print(k, "=", caesar_decrypt(cipher, k))


msg = input("Enter message: ")
key = int(input("Enter key (0-25): "))

enc = caesar_encrypt(msg, key)
print("Encrypted:", enc)

dec = caesar_decrypt(enc, key)
print("Decrypted:", dec)

print("\nBruteforce:")
caesar_bruteforce(enc)
