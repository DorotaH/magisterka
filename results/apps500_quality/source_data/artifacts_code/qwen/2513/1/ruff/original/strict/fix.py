def solve(N, s):
    if N % 2 == 0 and s.count('o') != N:
        return -1
    if N % 2 == 1 and s.count('o') != N - 1:
        return -1

    t = [''] * N
    if N % 2 == 0:
        t[0] = 'S'
    else:
        t[0] = 'S' if s[0] == 'o' else 'W'

    for i in range(1, N):
        if t[i-1] == 'S':
            if s[i] == 'o':
                t[i] = 'S'
            else:
                t[i] = 'W'
        else:
            if s[i] == 'o':
                t[i] = 'W'
            else:
                t[i] = 'S'

    return ''.join(t)

# Read input
N = int(input().strip())
s = input().strip()

# Solve and print the result
result = solve(N, s)
print(result)
