def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    odd_count = sum(1 for num in a if num % 2 != 0)
    return 'Yes' if x % 2 == 1 or (x % 2 == 0 and odd_count >= x) else 'No'

for _ in range(int(input())):
    print(solve())
