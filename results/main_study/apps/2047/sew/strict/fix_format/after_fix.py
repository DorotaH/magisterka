import sys


# @profile
def main():
    f = sys.stdin
    # f = open('input.txt', 'r')
    # fo = open('log.txt', 'w')
    n = int(f.readline())
    # b = []
    # for i in range(n):
    #    b.append()
    b, a = list(map(int, f.readline().strip().split(' '))), list(map(int, f.readline().strip().split(' ')))
    # return
    b = [b[i] - a[i] for  i in  range(0, n)]
    c = [[0, 0]]
    for  i in  range(n - 1):
        line = f.readline().strip().split(' ')
        c.append([int(line[0]), int(line[1])])
    # print(c)
    for  i in  range(n - 1, 0, -1):
        # print(i)
        fa = c[i][0] - 1
        if not b[i] >= 0:
            b[fa] += b[i] * c[i][1]
            if b[fa] < -1e17:
                print('NO')
                return 0
        else:
            b[fa] += b[i]
    # for x in b:
    #    fo.write(str(x) + '\n')
    if not b[0] >= 0:
        print('NO')
    else:
        print('YES')

main()
