n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

odd_a = sum(1 for x in a if 1 == x % 2)
even_a, odd_b = n - odd_a, sum(1 for x in b if x % 2 == 1)
even_b = m - odd_b

result = min(odd_a, odd_b) + min(even_a, even_b)
print(result)