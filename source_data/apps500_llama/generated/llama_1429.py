import math

def extended_gcd(a, b):
    """Extended Euclidean algorithm to find gcd and coefficients"""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inv(a, m):
    """Modular inverse using extended Euclidean algorithm"""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m

def L(x, p, k):
    """k-th element of L(x, p)"""
    m = p
    m_inv = mod_inv(x, m)
    return (x * (k - 1) + 1) * m_inv % m

def main():
    t = int(input())
    for _ in range(t):
        x, p, k = map(int, input().split())
        print(L(x, p, k))

if __name__ == "__main__":
    main()
