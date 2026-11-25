n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

odd_a = sum(bool(x % 2 == 1) for x in a)
even_a = n - odd_a
odd_b = sum(bool(x % 2 == 1) for x in b)
even_b = m - odd_b

result = min(odd_a, odd_b) + min(even_a, even_b)
print(result)
