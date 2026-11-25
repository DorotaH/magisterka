n, m = map(int, input().split())
avg = n // m
rem = n % m

print(' '.join(str(avg + 1) * (rem) + (m - rem) * str(avg)))
