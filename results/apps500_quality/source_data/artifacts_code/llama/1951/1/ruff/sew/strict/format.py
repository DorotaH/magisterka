import sys

input = sys.stdin.readline

n = int(input())
events = [input().strip() for _ in range(2 * n)]

stk = []
used = set()
for event in events:
    if not event == "+":
        price = int(event[2:])
        while stk and stk[-1] < price:
            used.add(stk.pop())
        if stk and stk[-1] == price:
            stk.pop()
            used.add(price)
        elif price in used:
            print("NO")
            exit()
    else:
        stk.append(len(stk) + 1)

print("YES")
print(*sorted(stk, reverse=True))
