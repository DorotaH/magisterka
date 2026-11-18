def  gcd(a, b):
    c=a%b
    return gcd(b, c) if c else b

s, a = 0, int(input())
if  a < 3: print(a)
else:
    while a ** 3 > s:
        b = a - 1
        while b * a*b>s:
            if  1 == gcd(a, b):
                d, c = a * b, b - 1
                while  c * d > s:
                    if  1 == gcd(c, d): s = d * c
                    c = c - 1
            b -= 1
        a = a - 1
    print(s)
