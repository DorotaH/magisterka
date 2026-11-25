def find_subset():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1 or n % 2 != 0:
        print(1)
        print(a[0] + 1)
    else:
        print(n)
        print(" ".join(map(lambda x: str(1 + x), range(n))))


t = int(input())
for _ in range(t):
    find_subset()
