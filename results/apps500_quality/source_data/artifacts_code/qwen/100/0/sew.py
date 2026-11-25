import  sys
input=sys.stdin.read
data=input().split()

n=int(data[0])
m, screen = int(data[1]), data[2:]

def find_min_frame(n, m, screen):
    min_size, min_frame = float('inf'), None
    for  i in  range(n):
        for j in range(0, m):
            if screen[i][j]=='.':
                for  size in  range(1, 1+min(n-i, m-j)):
                    valid = True
                    for  di in  range(-1, 2):
                        for  dj in  range(-1, 2):
                            if  di == 0 and  dj == 0:
                                continue
                            ni, nj = i + di * size, j + dj * size
                            if  ni < 0 or  ni >= n or  nj < 0 or  nj >= m or  screen[ni][nj] == '.':
                                valid = False
                                break
                        if  not  valid:
                            break
                    if valid:
                        if  size < min_size:
                            min_size, min_frame = size, (i, j, size)
                        break

    if min_frame is None:
        return "-1"
    else:
        result = [list(row) for row in screen]
        i, j, size = min_frame
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di * size, j + dj * size
                result[ni][nj] = '+'
        return '\n'.join([''.join(row) for row in result])

print(find_min_frame(n, m, screen))