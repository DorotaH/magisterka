import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
D = int(data[3])
E = int(data[4])

# Sort the dishes by their serving times in ascending order
dishes = sorted([A, B, C, D, E])

# Calculate the earliest possible time for the last dish to be delivered
last_delivery_time = 0
for dish in dishes:
    last_delivery_time = (last_delivery_time + dish - 1) // 10 * 10 + dish

print(last_delivery_time)
