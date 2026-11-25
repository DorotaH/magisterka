import sys
from collections import deque

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

n = read_int()
events = []
for _ in range(2 * n):
    event = sys.stdin.readline().strip()
    if event == '+':
        events.append(0)
    else:
        price, = read_ints()
        events.append(price)

stack = deque()
current_price = 0
can_be_bought = True

for event in events:
    if event == 0:
        stack.appendleft(0)
    else:
        if stack:
            if event <= current_price:
                stack.popleft()
                current_price = event
            elif stack[0] < event:
                can_be_bought = False
                break
            else:
                current_price = event
        else:
            can_be_bought = False
            break

if can_be_bought:
    print('YES')
    print(*sorted(stack))
else:
    print('NO')
