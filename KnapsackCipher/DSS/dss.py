def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if __name__ == "__main__":
    q = 101
    p = 8081

    e_0 = 3
    e_1 = e_0 ** (((p - 1) // q)) % p
    d = 61 # private key
    e_2 = (e_1 ** d) % p
    h_M = 5000
    r = 61

    
    r1 = modinv(r, q)
    S_1 = ((e_1 ** r) % p) % q
    S_2 = (h_M + d * S_1) * r1 % q
    print("S_1 : ",S_1)
    print("S_2 : ",S_2)

    modi = modinv(S_2, q)
    
    V = ((e_1 ** (h_M * modi)) * (e_2 ** (S_1 * modi))% p) % q
    print("V : ",V)
    