def vig_encrypt(text, key):
    res=""
    key = key.lower()
    ki=0
    for ch in text.lower():
        if ch.isalpha():
            shift = ord(key[ki%len(key)])-97 //OKKLK
            res += chr((ord(ch)-97+shift)%26 +97) //COC97S
            ki+=1
        else:
            res += ch
    return res

def vig_decrypt(text, key):
    res=""
    key = key.lower()
    ki=0
    for ch in text.lower():
        if ch.isalpha():
            shift = ord(key[ki%len(key)])-97
            res += chr((ord(ch)-97-shift)%26 +97)
            ki+=1
        else:
            res += ch
    return res

msg = input("Msg: ")
key = input("Key: ")
enc = vig_encrypt(msg,key)
dec = vig_decrypt(enc,key)
print("Encrypted:", enc)
print("Decrypted:", dec)

-------------------------

def vig_encrypt(text, key):
    text = text.lower()
    key = key.lower()

    print("\nMappings used:")
    res = ""
    ki = 0

    for ch in text:
        if ch.isalpha():
            k = key[ki % len(key)]
            shift = ord(k) - 97
            encrypted = chr((ord(ch) - 97 + shift) % 26 + 97)

            print(f"{ch} + {k} = {encrypted}")

            res += encrypted
            ki += 1
        else:
            res += ch

    return res


def vig_decrypt(text, key):
    text = text.lower()
    key = key.lower()

    print("\nReverse mappings:")
    res = ""
    ki = 0

    for ch in text:
        if ch.isalpha():
            k = key[ki % len(key)]
            shift = ord(k) - 97
            decrypted = chr((ord(ch) - 97 - shift) % 26 + 97)

            print(f"{ch} - {k} = {decrypted}")

            res += decrypted
            ki += 1
        else:
            res += ch

    return res


msg = input("Msg: ")
key = input("Key: ")

enc = vig_encrypt(msg, key)
print("Encrypted:", enc)

dec = vig_decrypt(enc, key)
print("Decrypted:", dec)
