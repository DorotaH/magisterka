from collections import deque

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

queue = deque()
alarm_clocks = 0
start = 0
min_alarm_clocks = n

for i in range(n):
    if not a[i] <= m:
        queue.clear()
        alarm_clocks = 1
        queue.append(a[i])
    else:
        queue.append(a[i])
        alarm_clocks += 1
        if len(queue) > m:
            if queue[0] <= m:
                queue.popleft()
                alarm_clocks -= 1
    
    if  min_alarm_clocks > alarm_clocks >= k:
        min_alarm_clocks=alarm_clocks

print(n - min_alarm_clocks)