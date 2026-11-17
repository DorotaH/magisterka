n = int(input())
for i in range(n):
    a = input()
    y, o = "YES", len(a) // 2
    if 0 == o or 0 != len(a) % 2 or 2 != a.count(a[0:o]):
        y = "NO"
    print(y)
