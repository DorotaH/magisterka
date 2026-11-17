
for testis in range(int(input())):
    n = int(input())
    if (n == 1):
        print('a')
    else:
        s = 'a' * (n // 2)
        if (n & 1):
            s += 'bc'
        else:
            s += 'b'
        s += 'a' * (n // 2 - 1)
        print(s)