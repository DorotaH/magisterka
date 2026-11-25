def max_r_number(n):
    return 8 if n == 1 else int('9' * (n - 1) + '8')


t = int(input())
for _ in range(t):
    n = int(input())
    print(max_r_number(n))
