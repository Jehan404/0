def rail_encrypt(msg, rails):
    msg = msg.replace(" ", "")
    print("\n=== RAIL FENCE ENCRYPTION ===")
    print("Cleaned Message:", msg)
    print("Rails:", rails)

    fence = [""] * rails
    row = 0
    direction = 1

    print("\nPlacing characters in Zigzag:\n")

    for ch in msg:
        # visual print
        print(" " * row + ch)

        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    encrypted = "".join(fence)
    print("\nEncrypted =", encrypted)
    return encrypted


def rail_decrypt(cipher, rails):
    print("\n=== RAIL FENCE DECRYPTION ===")
    print("Ciphertext:", cipher)

    # Step 1: Create empty pattern
    pattern = [["" for _ in range(len(cipher))] for _ in range(rails)]
    row = 0
    direction = 1

    # Mark pattern
    for i in range(len(cipher)):
        pattern[row][i] = "*"

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    # Step 2: Fill characters
    idx = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if pattern[r][c] == "*":
                pattern[r][c] = cipher[idx]
                idx += 1

    # Step 3: Read zigzag
    row = 0
    direction = 1
    result = ""

    for i in range(len(cipher)):
        result += pattern[row][i]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    print("Decrypted =", result)
    return result


# MAIN
msg = input("Message: ")
rails = int(input("Rails: "))

encrypted = rail_encrypt(msg, rails)
decrypted = rail_decrypt(encrypted, rails)
