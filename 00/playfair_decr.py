def create_matrix(key):
    print("\n=== CREATING PLAYFAIR MATRIX ===")

    key = key.lower().replace("j", "i")
    matrix = ""

    print("Cleaned Key:", key)

    # add key characters
    for c in key:
        if c not in matrix and c.isalpha():
            matrix += c

    # add rest of alphabet
    for c in "abcdefghiklmnopqrstuvwxyz":
        if c not in matrix:
            matrix += c

    mat = [list(matrix[i:i+5]) for i in range(0, 25, 5)]

    print("\nGenerated 5x5 Matrix:")
    for row in mat:
        print(row)

    return mat


def find_pos(mat, ch):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j


def playfair_encrypt(msg, key):
    print("\n=== PLAYFAIR ENCRYPTION ===")

    mat = create_matrix(key)

    msg = msg.lower().replace(" ", "").replace("j", "i")
    print("\nCleaned message:", msg)

    if len(msg) % 2 != 0:
        msg += "x"
        print("Padded message:", msg)

    res = ""

    for i in range(0, len(msg), 2):
        a, b = msg[i], msg[i+1]
        r1, c1 = find_pos(mat, a)
        r2, c2 = find_pos(mat, b)

        print(f"\nPair: {a} {b}")
        print(f"Positions: ({r1},{c1})  ({r2},{c2})")

        if r1 == r2:
            print("Rule: Same row → take RIGHT")
            res += mat[r1][(c1+1)%5] + mat[r2][(c2+1)%5]

        elif c1 == c2:
            print("Rule: Same column → take BELOW")
            res += mat[(r1+1)%5][c1] + mat[(r2+1)%5][c2]

        else:
            print("Rule: Rectangle → SWAP COLUMNS")
            res += mat[r1][c2] + mat[r2][c1]

        print(f"{a}{b} → {res[-2]}{res[-1]}")

    return res


def playfair_decrypt(msg, key):
    print("\n=== PLAYFAIR DECRYPTION ===")

    mat = create_matrix(key)
    res = ""

    for i in range(0, len(msg), 2):
        a, b = msg[i], msg[i+1]
        r1, c1 = find_pos(mat, a)
        r2, c2 = find_pos(mat, b)

        print(f"\nPair: {a} {b}")
        print(f"Positions: ({r1},{c1})  ({r2},{c2})")

        if r1 == r2:
            print("Rule: Same row → take LEFT")
            res += mat[r1][(c1-1)%5] + mat[r2][(c2-1)%5]

        elif c1 == c2:
            print("Rule: Same column → take UP")
            res += mat[(r1-1)%5][c1] + mat[(r2-1)%5][c2]

        else:
            print("Rule: Rectangle → SWAP COLUMNS")
            res += mat[r1][c2] + mat[r2][c1]

        print(f"{a}{b} → {res[-2]}{res[-1]}")

    return res


# MAIN
key = input("Enter key: ")
msg = input("Enter message: ")

enc = playfair_encrypt(msg, key)
print("\nEncrypted:", enc)

dec = playfair_decrypt(enc, key)
print("Decrypted:", dec)
