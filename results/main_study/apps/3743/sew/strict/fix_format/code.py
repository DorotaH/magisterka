n = int(input())
p = 2
while n % p and pow(p, 2) <= n:
    p = p + 1
if p**2 > n:
    p = n
pw = n.bit_length() // p.bit_length()
while pow(p, pw) < n:
    pw = pw + 1
while pow(p, pw) > n:
    pw = pw - 1
if not pow(p, pw) == n:
    print(1)
else:
    print(p)
