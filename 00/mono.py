plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

def mono_encrypt(text):
    res = ""
    for ch in text.lower():
        if ch in plain:
            res += cipher[plain.index(ch)] ///CPIC
        else:
            res += ch
    return res

def mono_decrypt(text):
    res = "" 
    for ch in text.upper():
        if ch in cipher:
            res += plain[cipher.index(ch)]
        else:
            res += ch
    return res

msg = input("Enter message: ")
enc = mono_encrypt(msg)
dec = mono_decrypt(enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
--------------------------

plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

def mono_encrypt(text):
    used = set(ch for ch in text.lower() if ch in plain)

    print("\nMappings used:")
    for ch in sorted(used):
        print(f"{ch} → {cipher[plain.index(ch)]}")

    res = ""
    for ch in text.lower():
        if ch in plain:
            res += cipher[plain.index(ch)]
        else:
            res += ch
    return res

def mono_decrypt(text):
    res = ""
    for ch in text.upper():
        if ch in cipher:
            res += plain[cipher.index(ch)]
        else:
            res += ch
    return res

msg = input("Enter message: ")
enc = mono_encrypt(msg)
dec = mono_decrypt(enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
