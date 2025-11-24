import numpy as np

def hill_encrypt(msg, K):
    print("\n=== HILL ENCRYPTION ===")

    msg = msg.replace(" ", "").lower()
    print("Cleaned message:", msg)

    if len(msg) % 2 != 0:
        msg += "x"
        print("Padded message:", msg)

    print("\nUsing Key Matrix K:")
    print(K)

    res = ""

    for i in range(0, len(msg), 2):
        p1 = ord(msg[i]) - 97
        p2 = ord(msg[i+1]) - 97

        print(f"\nPair: {msg[i]} {msg[i+1]}")
        print(f"Vector: [{p1}, {p2}]")

        v = np.array([[p1], [p2]])
        r = np.dot(K, v) % 26

        c1 = chr(r[0][0] + 97)
        c2 = chr(r[1][0] + 97)

        print("Matrix multiplication result:", r.flatten())
        print(f"{msg[i]} {msg[i+1]} → {c1} {c2}")

        res += c1 + c2

    return res


def matrix_inverse_mod26(K):
    print("\n=== COMPUTING INVERSE MATRIX ===")

    det = int(round(np.linalg.det(K)))
    print("Determinant:", det)

    det_mod = det % 26
    print("Det mod 26:", det_mod)

    det_inv = None
    for i in range(26):
        if (det_mod * i) % 26 == 1:
            det_inv = i
            break

    if det_inv is None:
        print("Matrix NOT invertible mod 26")
        return None

    print("Determinant inverse mod 26:", det_inv)

    adj = np.array([[ K[1][1], -K[0][1]],
                    [-K[1][0],  K[0][0]]])

    print("Adjoint matrix:")
    print(adj)

    K_inv = (det_inv * adj) % 26

    print("Inverse matrix mod 26:")
    print(K_inv)

    return K_inv


def hill_decrypt(cipher, K):
    print("\n=== HILL DECRYPTION ===")
    print("Ciphertext:", cipher)

    K_inv = matrix_inverse_mod26(K)
    if K_inv is None:
        return None

    res = ""

    for i in range(0, len(cipher), 2):
        c1 = ord(cipher[i]) - 97
        c2 = ord(cipher[i+1]) - 97

        print(f"\nPair: {cipher[i]} {cipher[i+1]}")
        print(f"Vector: [{c1}, {c2}]")

        v = np.array([[c1], [c2]])
        r = np.dot(K_inv, v) % 26

        p1 = chr(r[0][0] + 97)
        p2 = chr(r[1][0] + 97)

        print("After inverse multiplication:", r.flatten())
        print(f"{cipher[i]} {cipher[i+1]} → {p1} {p2}")

        res += p1 + p2

    return res


msg = input("Message: ")
a, b, c, d = map(int, input("Enter 4 key values: ").split())
K = np.array([[a, b], [c, d]])

cipher = hill_encrypt(msg, K)
print("\nEncrypted:", cipher)

plain = hill_decrypt(cipher, K)
print("Decrypted:", plain)
