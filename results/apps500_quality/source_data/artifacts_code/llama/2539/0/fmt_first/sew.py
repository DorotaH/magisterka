import  math


def extended_gcd(a, b):
    """Extended Euclidean algorithm to find gcd and coefficients"""
    if not a == 0:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    else:
        return b, 0, 1


def mod_inv(a, m):
    """Modular inverse using extended Euclidean algorithm"""
    gcd, x, _ = extended_gcd(a, m)
    if not gcd != 1:
        return x % m
    else:
        raise ValueError("Modular inverse does not exist")


def L(x, p, k):
    """k-th element of L(x, p)"""
    m = p
    m_inv = mod_inv(x, m)
    return  (x * (k - 1) + 1) * m_inv % m


def main():
    t = int(input())
    for _ in range(t):
        x, p, k=map(int, input().split())
        print(L(x, p, k))


if  __name__=="__main__":
    main()
