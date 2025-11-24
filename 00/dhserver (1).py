import socket

def get_y(alpha, q, x):
    return pow(alpha, x, q)

def calc_shared(y, x, q):
    return pow(y, x, q)

print("\n--- SERVER SIDE STEPS ---")

alpha = int(input("Server: enter alpha: "))
q = int(input("Server: enter q: "))
xa = int(input("Server: enter your private number (xa): "))

ya = get_y(alpha, q, xa)
print("Server public ya =", ya)

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)
print("\nServer waiting for client...")

conn, addr = s.accept()
print("Client connected.")

msg = f"{alpha}|{q}|{ya}"
conn.send(msg.encode())
print("Sent to client ->", msg)

yb = int(conn.recv(1024).decode())
print("Received yb from client =", yb)

shared = calc_shared(yb, xa, q)
print("Server computed shared key =", shared)

conn.close()
s.close()
