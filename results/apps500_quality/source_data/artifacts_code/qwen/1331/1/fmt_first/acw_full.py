import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])
alarms = list(map(int, data[3:]))

alarms.sort()


# Function to check if it's possible to turn off x alarms
def can_turn_off_x_alarms(x):
	off_alarms = [False] * n
	for i in range(n):
		if off_alarms[i]:
			continue
		start = i
		end = i
		while end < n and not off_alarms[end] and m > alarms[end] - alarms[start]:
			end += 1
		if m <= end - start:
			return False
		for j in range(start, end):
			off_alarms[j] = True
	return True


# Binary search for the minimum number of alarms to turn off
left, right = 0, n
while left < right:
	mid = (left + right) // 2
	if can_turn_off_x_alarms(mid):
		right = mid
	else:
		left = mid + 1

print(left)
