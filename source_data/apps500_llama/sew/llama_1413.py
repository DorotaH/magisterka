import sys
input=sys.stdin.readline

N, M=map(int, input().split())
A = [0] * (N + 1)
B = [0] * (N + 1)
for  i in  range(1, N + 1):
    A[i], B[i]=map(int, input().split())

L = [0] * (M + 1)
R = [0] * (M + 1)
for  i in  range(1, M + 1):
    L[i], R[i]=map(int, input().split())

events=[]
for  i in  range(1, N + 1):
    events.append((A[i], 1))
for  i in  range(1, M + 1):
    events.append((L[i], -1))
    events.append((R[i], 1))

events.sort()

activated = 0
deactivated = 0
activated_cords = []
deactivated_cords = []

for  event in  events:
    if event[0] == L[i]:
        i = i + 1
    if event[1] == 1:
        activated += 1
    else:
        deactivated += 1
    if activated > deactivated:
        activated_cords.append(event[0])
    elif deactivated > activated:
        deactivated_cords.append(event[0])

if activated == deactivated:
    print(len(activated_cords))
    print(*activated_cords)
else:
    print(-1)
