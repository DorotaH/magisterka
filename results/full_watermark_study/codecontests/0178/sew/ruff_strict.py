n = int(input())
for i in range(n):
    a = input()
    y, o = "YES", len(a) // 2
    if o == 0 or len(a) % 2 != 0 or a.count(a[0:o]) != 2:
        y = "NO"
    print(y)
