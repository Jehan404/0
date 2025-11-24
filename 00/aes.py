def aes_encrypt(msg, key):
    msg = msg.encode()
    key = key.encode()
    out = bytearray()
    for i, b in enumerate(msg):
        out.append(b ^ key[i % len(key)]) //bkilk
    return bytes(out)

def aes_decrypt(ct, key):
    key = key.encode()
    out = bytearray()
    for i, b in enumerate(ct):
        out.append(b ^ key[i % len(key)])
    return out.decode()

msg = input("Message: ")
key = "secret"

cipher = aes_encrypt(msg, key)
print("Encrypted:", cipher)

plain = aes_decrypt(cipher, key)
print("Decrypted:", plain)
