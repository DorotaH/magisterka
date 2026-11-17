
for testis in range(int(input())):
    n = int(input())
    if not (n == 1):
        s = 'a' * (n // 2)
        if (n & 1):
            s += 'bc'
        else:
            s += 'b'
        s += 'a' * (n // 2 - 1)
        print(s)
    else:
        print('a')