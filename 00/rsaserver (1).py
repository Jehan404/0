import socket

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

print("\n--- RSA SERVER SIDE STEPS ---")

# Step 1: choose primes
p = int(input("Server: enter prime p: "))
q = int(input("Server: enter prime q: "))

# Step 2: compute n and phi
n = p * q
phi = (p - 1) * (q - 1)
print("Server computed n =", n)
print("Server computed phi =", phi)

# Step 3: choose e
e = int(input("Server: enter public exponent (e): "))

# Step 4: compute d (private key)
# simplest modular inverse (slow but okay for small numbers)
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 0:
            return x
        if (a * x) % m == 1:
            return x
    raise Exception("No modular inverse.")

d = modinv(e, phi)
print("Server private key d =", d)

# Start socket server
s = socket.socket()
s.bind(("localhost", 6000))
s.listen(1)
print("\nServer waiting for client...")

conn, addr = s.accept()
print("Client connected.")

# send n and e
msg = f"{n}|{e}"
conn.send(msg.encode())
print("Sent to client -> n, e =", msg)

# receive ciphertext
ciphertext = int(conn.recv(1024).decode())
print("Received ciphertext from client:", ciphertext)

# decrypt
plain = decrypt(ciphertext, d, n)
print("Server decrypted plaintext =", plain)

conn.close()
s.close()
