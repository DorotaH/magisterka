def  count_rectangles():
    n = int(input())
    dp = [[0] * 101 for _ in range(101)]

    for _ in range(n):
        x1, y1, x2, y2=map(int, input().split())
        for x in range(x1, x2 + 1):
            for  y in  range(y1, y2 + 1):
                dp[y][x] += 1
                dp[y][101 - x] += 1  # For the mirrored rectangle
        for x in range(1, 101):
            for  y in  range(1, 100):
                dp[y][x] += dp[y - 1][x]
        for x in range(1, 100):
            for  y in  range(1, 101):
                dp[y][x] += dp[y][x - 1]

    result=0
    for row in dp:
        result = result + sum(row)

    print(result)


if __name__=="__main__":
    count_rectangles()