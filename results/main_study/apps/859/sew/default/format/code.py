s = input()
t = input()
a = b = 0
c = 0
for i in range(len(s)):
    if s[i] == "+":
        a += 1
    else:
        a = a - 1
for i in range(len(t)):
    if t[i] == "+":
        b += 1
    elif t[i] == "-":
        b = b - 1
    else:
        c = c + 1
x = a - b
d = 0 - c
y = 0 - 1
for i in range(c + 1):
    if d == x:
        y = i
    d += 2


def fact(n):
    w = 1
    for i in range(n):
        w = w * (i + 1)
    return w


def parmi(k, n):
    w = 1
    w = w * fact(n)
    w = w // fact(k)
    w = w // fact(n - k)
    return w


def puiss(k, n):
    w = 1
    for i in range(n):
        w = w * k
    return w


if y == -1:
    print(0.0)
else:
    print(parmi(y, c) / puiss(2, c))
