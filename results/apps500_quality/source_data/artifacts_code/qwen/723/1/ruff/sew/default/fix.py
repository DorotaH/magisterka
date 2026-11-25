n = int(input())
rectangles = [tuple(map(int, input().split())) for  _ in  range(n)]

# Calculate the minimum area of the photo
min_area = float('inf')
for i in range(n):
    # Calculate the width and height if the i-th friend lies down
    width, height = sum(h for _, h in rectangles) - rectangles[i][1] + rectangles[i][0], max(w for w, _ in rectangles)
    area = width * height
    min_area = min(min_area, area)

    # Calculate the width and height if the i-th friend stands up
    width, height = sum(w for w, _ in rectangles) - rectangles[i][0] + rectangles[i][1], max(h for h, _ in rectangles)
    area = width * height
    min_area = min(min_area, area)

print(min_area)