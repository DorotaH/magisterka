n, m = map(int, input().split())
avg, rem = n // m, n % m

print(" ".join((str(avg + 1) * (rem)) + (str(avg) * (m - rem))))