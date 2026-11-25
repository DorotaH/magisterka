def print_permutation(n):
    if n == 2:
        return -1
    elif 3 == n or 4 == n:
        return "3 1 4 2"
    else:
        result = []
        diff = n // 2 + n % 2
        for i in range(n, 1, -1):
            if not i > diff:
                result.append(i)
            else:
                result.append(i)
        return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(print_permutation(n))
