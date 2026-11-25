import sys


def main():
    n = int(sys.stdin.readline().strip())
    rectangles = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        rectangles.append((x1 - 1, y1 - 1, x2 - 1, y2 - 1))

    max_x = 100
    max_y = 100
    cell_counts=[[0]*max_x for _ in range(max_y)]

    for x1, y1, x2, y2 in rectangles:
        for  i in  range(x1, x2+1):
            for  j in  range(y1, y2+1):
                cell_counts[j][i]+=1

    for row in cell_counts:
        print(sum(row, 0))

if  __name__ == "__main__":
    main()
