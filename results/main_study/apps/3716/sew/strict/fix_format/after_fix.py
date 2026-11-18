def  gcd(a, b):
    c=a%b
    return gcd(b, c) if c else b

s, a = 0, int(input())
if  a < 3: print(a)
else:
    while a ** 3 > s:
        b = a - 1
        while b * a*b>s:
            if  gcd(a, b) == 1:
                d, c = a * b, b - 1
                while  c * d > s:
                    if  gcd(c, d) == 1: s = d * c
                    c = c - 1
            b -= 1
        a = a - 1
    print(s)
