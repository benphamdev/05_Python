def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def encrypt(message, n):
    ciphertext = [(message ** 2) % n]
    return ciphertext

def decrypt(ciphertext, p, q):
    n = p * q
    m1 = pow(ciphertext[0], (p + 1) // 4, p)
    m2 = pow(ciphertext[0], (q + 1) // 4, q)
    y1 = (m1 * q * mod_inverse(q, p)) % n
    y2 = (m2 * p * mod_inverse(p, q)) % n
    r1 = (y1 + y2) % n
    r2 = (y1 - y2 + n) % n
    r3 = (-y1 + y2 + n) % n
    r4 = (-y1 - y2 + 2 * n) % n

    decrypted_message = max(r1, r2, r3, r4)
    return decrypted_message

if __name__ == "__main__":
    p = int(input("p = "))
    q = int(input("q = "))
    x = int(input("x = "))

    n = p * q
    ciphertext = encrypt(x, n)
    print("Encrypted Rabin message:", ciphertext[0])
    decrypted_message = decrypt(ciphertext, p, q)
    print("Decrypted Rabin message:", decrypted_message)

# 19 23 329