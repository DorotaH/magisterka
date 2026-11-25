from collections import deque

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

queue = deque()
alarm_clocks = 0
start = 0
min_alarm_clocks = n

for i in range(n):
    if a[i] <= m:
        queue.append(a[i])
        alarm_clocks += 1
        if len(queue) > m:
            if queue[0] <= m:
                queue.popleft()
                alarm_clocks -= 1
    else:
        queue.clear()
        alarm_clocks = 1
        queue.append(a[i])
    
    if alarm_clocks < min_alarm_clocks and alarm_clocks >= k:
        min_alarm_clocks = alarm_clocks

print(n - min_alarm_clocks)
