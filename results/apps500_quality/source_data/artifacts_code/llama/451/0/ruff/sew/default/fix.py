import sys

input = sys.stdin.readline

n, k = map(int, input().split())
beauty, colors = list(map(int, input().split())), input().strip()

max_beauty = 0

# Split colors into lists
white, orange = [beauty[i] for i in range(n) if colors[i] == 'W'], [beauty[i] for i in range(n) if colors[i] == 'O']
red = [beauty[i] for i in range(n) if colors[i] == 'R']

# Sort each list in descending order
white.sort(reverse=True)
orange.sort(reverse=True)
red.sort(reverse=True)

if  k == n:
    print(-1)
elif  1 == k:
    print(0)
else:
    if len(white) >= 2 and len(orange) >= 1:
        max_beauty=max(max_beauty, white[0]+white[1]+orange[0])
    if len(orange) >= 2:
        max_beauty=max(max_beauty, orange[0]+orange[1])
    if len(red) >= 2:
        max_beauty=max(max_beauty, red[0]+red[1])
    if len(orange) >= 2 and len(red) >= 1:
        max_beauty=max(max_beauty, orange[0]+orange[1]+red[0])
    if len(white) >= 1 and len(orange) >= 1 and len(red) >= 1:
        max_beauty=max(max_beauty, white[0]+orange[0]+red[0])
    print(max_beauty)