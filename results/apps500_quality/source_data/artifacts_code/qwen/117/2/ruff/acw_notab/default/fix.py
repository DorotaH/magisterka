import sys

input = sys.stdin.read
data = input().split()

N, M = int(data[0]), int(data[1])
north_south_lines = []
east_west_lines = []

for i in range(N):
    A, B, C = int(data[2 + i * 3]), int(data[3 + i * 3]), int(data[4 + i * 3])
    north_south_lines.append((A, B, C))

for j in range(M):
    D, E, F = int(data[2 + N * 3 + 2 * j]), int(data[3 + N * 3 + 2 * j]), int(data[4 + N * 3 + 2 * j])
    east_west_lines.append((D, E, F))

# Check if the area is infinite


def is_infinite_area():
    for i in range(N):
        for j in range(M):
            if north_south_lines[i][2] < east_west_lines[j][1] < north_south_lines[i][2] or north_south_lines[i][2] < east_west_lines[j][3] < north_south_lines[i][2]:
                return True
            if east_west_lines[j][2] < north_south_lines[i][1] < east_west_lines[j][2] or east_west_lines[j][2] < north_south_lines[i][3] < east_west_lines[j][2]:
                return True
    return False


if is_infinite_area():
    print("INF")
else:
    # Calculate the area of the region the cow can reach
    area = 0
    for i in range(N):
        for j in range(M):
            if north_south_lines[i][1] < east_west_lines[j][3] < north_south_lines[i][2] and north_south_lines[i][3] < east_west_lines[j][1] < north_south_lines[i][2]:
                area += (east_west_lines[j][3] - east_west_lines[j][1]) * (north_south_lines[i][2] - north_south_lines[i][1])
    print(area)
