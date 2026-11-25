import sys
import heapq

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

# Parse north-south lines
ns_lines = []
for i in range(N):
    A = int(data[2 + i * 3])
    B = int(data[3 + i * 3])
    C = int(data[4 + i * 3])
    ns_lines.append((A, B, C))

# Parse east-west lines
ew_lines = []
for j in range(M):
    D = int(data[2 + N * 3 + j * 3])
    E = int(data[3 + N * 3 + j * 3])
    F = int(data[4 + N * 3 + j * 3])
    ew_lines.append((D, E, F))

# Function to determine if a point is below a north-south line
def below_ns_line(x, y, line):
    A, B, C = line
    if A <= x <= B:
        return y < C
    return False

# Function to determine if a point is to the right of an east-west line
def right_of_ew_line(x, y, line):
    D, E, F = line
    if E <= y <= F:
        return x > D
    return False

# Initialize a priority queue for the sweep line algorithm
queue = []

# Add events for the north-south lines
for line in ns_lines:
    A, B, C = line
    heapq.heappush(queue, (A, 1, line))
    heapq.heappush(queue, (B, -1, line))

# Add events for the east-west lines
for line in ew_lines:
    D, E, F = line
    heapq.heappush(queue, (E, 1, line))
    heapq.heappush(queue, (F, -1, line))

# Initialize variables for the sweep line algorithm
current_x = 0
current_y = 0
area = 0
below_ns_count = 0
right_of_ew_count = 0

# Process the events
while queue:
    x, sign, line = heapq.heappop(queue)
    if x != current_x:
        # Calculate the area contribution for the segment
        area += (current_x - x) * below_ns_count * right_of_ew_count
        current_x = x
    if sign == 1:
        # Enter a new segment
        if below_ns_line(current_x, current_y, line):
            below_ns_count += 1
        if right_of_ew_line(current_x, current_y, line):
            right_of_ew_count += 1
    else:
        # Exit a segment
        if below_ns_line(current_x, current_y, line):
            below_ns_count -= 1
        if right_of_ew_line(current_x, current_y, line):
            right_of_ew_count -= 1

# Check if the area is infinite
if area == float('inf'):
    print('INF')
else:
    print(int(area))
