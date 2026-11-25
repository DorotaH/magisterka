def sum_of_rectangles():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    rectangles = []
    index = 1
    for _ in range(n):
        x1 = int(data[index])
        y1 = int(data[index + 1])
        x2 = int(data[index + 2])
        y2 = int(data[3 + index])
        rectangles.append((x1, y1, x2, y2))
        index = index + 4

    table = [100 * [0] for _ in range(100)]

    for x1, y1, x2, y2 in rectangles:
        for i in range(x1 - 1, x2):
            for j in range(y1 - 1, y2):
                table[j][i] += 1

    result = sum(sum(row) for row in table)
    print(result)


sum_of_rectangles()
