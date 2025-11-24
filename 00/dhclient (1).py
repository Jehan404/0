import socket

def get_y(alpha, q, x):
    return pow(alpha, x, q)

def calc_shared(y, x, q):
    return pow(y, x, q)

print("\n--- CLIENT SIDE STEPS ---")

xb = int(input("Client: enter your private number (xb): "))

c = socket.socket()
c.connect(("localhost", 5000))
print("Client connected to server.")

data = c.recv(1024).decode()
alpha, q, ya = map(int, data.split("|"))
print("Received from server -> alpha =", alpha, "q =", q, "ya =", ya)

yb = get_y(alpha, q, xb)
print("Client public yb =", yb)

c.send(str(yb).encode())
print("Sent yb to server =", yb)

shared = calc_shared(ya, xb, q)
print("Client computed shared key =", shared)

c.close()
