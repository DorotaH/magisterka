import sys

a, b, c = map(int, input().split())

for i in range(1, 100_000):
    if  0 == i % a:
        if (i%b)==c:
            print("YES")
            sys.exit(0)
print("NO")