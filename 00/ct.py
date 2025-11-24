def col_encrypt(msg, key):
    msg = msg.replace(" ", "")
    cols = len(key)
    rows = (len(msg) + cols - 1) // cols

    # Fill grid row-wise
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(msg):
                grid[r][c] = msg[idx]
                idx += 1

    # Sort key to decide read order
    order = sorted([(key[i], i) for i in range(cols)])

    # Read column-wise in sorted key order
    cipher = ""
    for _, c in order:
        for r in range(rows):
            if grid[r][c] != "":
                cipher += grid[r][c]

    return cipher


def col_decrypt(cipher, key):
    cols = len(key)
    rows = (len(cipher) + cols - 1) // cols

    # Prepare grid
    grid = [["" for _ in range(cols)] for _ in range(rows)]

    # Determine number of characters per column
    order = sorted([(key[i], i) for i in range(cols)])
    col_lengths = [rows] * cols

    extra = rows * cols - len(cipher)
    if extra > 0:
        for last in range(cols - extra, cols):
            col_lengths[last] -= 1

    # Fill grid column-wise
    idx = 0
    for pos, (char, col) in enumerate(order):
        clen = col_lengths[pos]
        for r in range(clen):
            grid[r][col] = cipher[idx]
            idx += 1

    # Read row-wise to get plaintext
    plain = ""
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "":
                plain += grid[r][c]

    return plain


msg = input("Message: ")
key = input("Key: ")

enc = col_encrypt(msg, key)
print("Encrypted:", enc)

dec = col_decrypt(enc, key)
print("Decrypted:", dec)
