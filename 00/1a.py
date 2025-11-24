def basic_euclid_gcd(a, b):
    print("\nq    r1    r2    r")
    print("---------------------")

    r1, r2 = a, b
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2

        print(f"{q:<4} {r1:<5} {r2:<5} {r:<5}")

        r1, r2 = r2, r

    print("\nGCD =", r1)


def extended_euclid(a, b):
    print("\nq    r1    r2    r      s1    s2    s      t1    t2    t")
    print("--------------------------------------------------------------")

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        s = s1 - q * s2
        t = t1 - q * t2

        print(f"{q:<4} {r1:<6} {r2:<6} {r:<6}  {s1:<6} {s2:<6} {s:<6}  {t1:<6} {t2:<6} {t:<6}")

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    print("\nGCD =", r1)
    print("s =", s1)
    print("t =", t1)


def multiplicative_inverse(a, m):
    print("\nq    r1    r2    r      t1    t2    t")
    print("-------------------------------------------")

    r1, r2 = m, a
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2

        print(f"{q:<4} {r1:<6} {r2:<6} {r:<6}  {t1:<6} {t2:<6} {t:<6}")

        r1, r2 = r2, r
        t1, t2 = t2, t

    if r1 != 1:
        print("\nMultiplicative inverse does not exist (GCD != 1)")
    else:
        inv = t1 % m
        print("\nGCD =", r1)
        print("Multiplicative Inverse =", inv)

while True:
    print("\n----- MENU -----")
    print("1. Basic Euclidean Algorithm (GCD)")
    print("2. Extended Euclid Algorithm (GCD, s, t)")
    print("3. Multiplicative Inverse using Euclid")
    print("4. Quit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        basic_euclid_gcd(a, b)
    elif choice == 2:
        extended_euclid(a, b)
    elif choice == 3:
        multiplicative_inverse(a, b)
    else:
        print("Invalid choice")
