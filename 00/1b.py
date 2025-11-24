def egcd(a, b):
    r1, r2 = a, b
    t1, t2 = 0, 1
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        r1, r2 = r2, r
        t1, t2 = t2, t
    return r1, t1

def inv(a, m):
    g, t = egcd(a, m)
    if g != 1:
        return None
    return t % m

moduli = [3, 5, 7]
M = 3 * 5 * 7
Mi = [M // m for m in moduli]

def print_mod_values(x):
    print(f"{x} mod 3 = {x % 3}")
    print(f"{x} mod 5 = {x % 5}")
    print(f"{x} mod 7 = {x % 7}")

def to_tuple(x):
    return [x % m for m in moduli]

def crt_combine(c):
    total = 0
    for i in range(3):
        invMi = inv(Mi[i], moduli[i])
        total += c[i] * Mi[i] * invMi
    return total % M

def add(a, b):
    return [(a[i] + b[i]) % moduli[i] for i in range(3)]

def sub(a, b):
    return [(a[i] - b[i]) % moduli[i] for i in range(3)]

def mul(a, b):
    return [(a[i] * b[i]) % moduli[i] for i in range(3)]

def div(a, b):
    out = []
    for i in range(3):
        inv_b = inv(b[i], moduli[i])
        if inv_b is None:
            return None
        out.append((a[i] * inv_b) % moduli[i])
    return out

while True:
    print("\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Quit")
    ch = int(input("Choice: "))
    if ch == 5:
        break

    A = int(input("Enter A: "))
    B = int(input("Enter B: "))

    print("\n---- MOD VALUES ----")
    print_mod_values(A)
    print()
    print_mod_values(B)
    print("--------------------")

    a = to_tuple(A)
    b = to_tuple(B)

    if ch == 1:
        c = add(a, b)
    elif ch == 2:
        c = sub(a, b)
    elif ch == 3:
        c = mul(a, b)
    elif ch == 4:
        c = div(a, b)
        if c is None:
            print("Division not possible")
            continue
    else:
        continue

    print("A tuple:", a)
    print("B tuple:", b)
    print("Result tuple:", c)
    print("Final number:", crt_combine(c))
