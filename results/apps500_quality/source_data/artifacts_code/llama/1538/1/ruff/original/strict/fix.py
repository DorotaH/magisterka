
n = int(input())
a = list(map(int, input().split()))

boxes = {}
for i in range(n):
    boxes[a[i]] = i

sorted_boxes = sorted(boxes.keys())

min_visible = len(sorted_boxes)

parent = [-1] * n
for i in range(n):
    for j in range(i):
        if a[sorted_boxes[j]] < a[sorted_boxes[i]]:
            parent[sorted_boxes[i]] = sorted_boxes[j]
            break

stack = [sorted_boxes[-1]]
while stack:
    box = stack.pop()
    if parent[box] != -1:
        stack.append(parent[box])

min_visible = len(set(stack))
print(min_visible)
