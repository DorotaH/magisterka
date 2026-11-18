def main(arr):
    ans = 2
    if 2 > len(arr):
        return 4 - len(arr)
    set_arr = set(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            need = 2
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            xc = (x1 + x2) / 2
            yc = (y2 + y1) / 2
            xd = (x1 - x2) / 2
            yd = (y1 - y2) / 2

            x3 = xc - yd
            y3 = yc + xd
            x4 = yd + xc
            y4 = yc - xd
            if (x3, y3) in set_arr:
                need -= 1
            if (x4, y4) in set_arr:
                need -= 1
            ans = min(ans, need)
    return ans


arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(main(arr))
