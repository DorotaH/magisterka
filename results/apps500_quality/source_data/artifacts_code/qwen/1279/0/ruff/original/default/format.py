n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

odd_a = sum(1 for x in a if x % 2 == 1)
even_a = n - odd_a
odd_b = sum(1 for x in b if x % 2 == 1)
even_b = m - odd_b

result = min(odd_a, odd_b) + min(even_a, even_b)
print(result)
