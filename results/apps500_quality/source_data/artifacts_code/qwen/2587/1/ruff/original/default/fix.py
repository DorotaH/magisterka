def max_r_number(n):
    if n == 1:
        return 8
    else:
        return int('9' * (n - 1) + '8')

t = int(input())
for _ in range(t):
    n = int(input())
    print(max_r_number(n))
