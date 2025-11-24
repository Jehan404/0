
def col_encrypt(msg, key):
    print("\n================ COLUMNAR ENCRYPTION ================")
    msg = msg.replace(" ", "")
    print("Cleaned message:", msg)
    print("Key:", key)

    sorted_key = sorted(list(key))
    print("Sorted key:", sorted_key)

    cols = len(key)
    rows = (len(msg) + cols - 1) // cols

    print(f"\nGrid size: {rows} rows × {cols} columns")

    grid = [["" for _ in range(cols)] for _ in range(rows)]

    print("\nFilling grid row-wise:")
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(msg):
                grid[r][c] = msg[idx]
                print(f"Placed '{msg[idx]}' at ({r},{c})")
                idx += 1

    print("\nFinal grid:")
    for row in grid:
        print(row)

    print("\nReading columns in sorted key order:")
    result = ""

    for ch in sorted_key:
        col = key.index(ch)
        print(f"\nColumn for '{ch}' is original index {col}")
        for r in range(rows):
            if grid[r][col] != "":
                print(f"Taking '{grid[r][col]}' from ({r},{col})")
                result += grid[r][col]

    print("\nCipher from this round:", result)
    return result

def col_decrypt(cipher, key):
    print("\n================ COLUMNAR DECRYPTION ================")
    print("Cipher:", cipher)
    print("Key:", key)

    sorted_key = sorted(list(key))
    print("Sorted key:", sorted_key)

    cols = len(key)
    rows = (len(cipher) + cols - 1) // cols

    print(f"\nGrid size: {rows} rows × {cols} columns")

    # Step 1: Mark cells
    marks = [["" for _ in range(cols)] for _ in range(rows)]
    print("\nStep 1: Marking positions with '*'")

    idx = 0
    for ch in sorted_key:
        col = key.index(ch)
        for r in range(rows):
            if idx < len(cipher):
                marks[r][col] = "*"
                print(f"Marking ({r},{col}) as fill slot")
                idx += 1

    print("\nMarked grid:")
    for row in marks:
        print(row)

    # Step 2: Fill in ciphertext
    print("\nStep 2: Filling ciphertext:")
    idx = 0
    for ch in sorted_key:
        col = key.index(ch)
        for r in range(rows):
            if marks[r][col] == "*":
                print(f"Placing '{cipher[idx]}' at ({r},{col})")
                marks[r][col] = cipher[idx]
                idx += 1

    print("\nGrid after filling:")
    for row in marks:
        print(row)

    # Step 3: Read row-wise
    print("\nStep 3: Reading row-wise:")
    result = ""
    for r in range(rows):
        for c in range(cols):
            if marks[r][c] != "":
                print(f"Reading '{marks[r][c]}' at ({r},{c})")
                result += marks[r][c]

    print("Plaintext from this round:", result)
    return result

def double_encrypt(msg, key1, key2):
    print("\n=========== DOUBLE COLUMNAR ENCRYPTION ===========")

    print("\n----- ROUND 1 ENCRYPTION using Key1 -----")
    first = col_encrypt(msg, key1)

    print("\n----- ROUND 2 ENCRYPTION using Key2 -----")
    second = col_encrypt(first, key2)

    print("\nFINAL DOUBLE ENCRYPTED TEXT:", second)
    return second


def double_decrypt(cipher, key1, key2):
    print("\n=========== DOUBLE COLUMNAR DECRYPTION ===========")

    print("\n----- ROUND 1 DECRYPTION using Key2 -----")
    first = col_decrypt(cipher, key2)

    print("\n----- ROUND 2 DECRYPTION using Key1 -----")
    second = col_decrypt(first, key1)

    print("\nFINAL DECRYPTED TEXT:", second)
    return second

msg = input("Enter message: ")
key1 = input("Enter Key 1: ")
key2 = input("Enter Key 2: ")

enc = double_encrypt(msg, key1, key2)
print("\nEncrypted:", enc)

dec = double_decrypt(enc, key1, key2)
print("Decrypted:", dec)
