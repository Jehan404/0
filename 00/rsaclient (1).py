import socket

def encrypt(m, e, n):
    return pow(m, e, n)

print("\n--- RSA CLIENT SIDE STEPS ---")

# Step 1: user chooses plaintext
m = int(input("Client: enter plaintext number (m): "))

# connect to server
c = socket.socket()
c.connect(("localhost", 6000))
print("Client connected to server.")

# receive n and e
data = c.recv(1024).decode()
n, e = map(int, data.split("|"))
print("Received from server -> n =", n, "e =", e)

# encrypt plaintext
ciphertext = encrypt(m, e, n)
print("Client ciphertext =", ciphertext)

# send ciphertext to server
c.send(str(ciphertext).encode())
print("Sent ciphertext to server.")

c.close()
