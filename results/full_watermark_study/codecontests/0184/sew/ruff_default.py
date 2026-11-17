import sys
from collections import defaultdict

input = sys.stdin.buffer.readline
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# input = sys.stdin.readline


def find(pas, x):
    if pas[x] != x:
        pas[x] = find(pas, pas[x])
    return pas[x]


def union(pas, x, y):
    fx = find(pas, x)
    fy = find(pas, y)
    if fx != fy:
        pas[fx] = fy


def work(n, k, points, explosion_time, row, col):
    pas = list(range(n))

    # for x in row:
    #     ps = []
    #     for pid in row[x]:
    #         px, py = points[pid]
    #         ps.append([py, px, pid])
    #     ps.sort()
    #     m = len(ps)
    #     for i in range(m):
    #         for j in range(i + 1, m):
    #             dist = abs(ps[j][0] - ps[i][0])
    #             if dist <= k:
    #                 union(pas, ps[i][2], ps[j][2])

    # for y in col:
    #     ps = []
    #     for pid in col[y]:
    #         px, py = points[pid]
    #         ps.append([px, py, pid])
    #     ps.sort()
    #     m = len(ps)
    #     for i in range(m):
    #         for j in range(i + 1, m):
    #             dist = abs(ps[j][0] - ps[i][0])
    #             if dist <= k:
    #                 union(pas, ps[i][2], ps[j][2])
    for x in row:
        ps = list()
        for pid in row[x]:
            px, py = points[pid]
            ps.append([py, pid])
        ps.sort()
        for i in range(len(ps) - 1):
            dist = abs(ps[i][0] - ps[i + 1][0])
            if dist <= k:
                union(pas, ps[i][1], ps[i + 1][1])

    for y in col:
        ps = list()
        for pid in col[y]:
            px, py = points[pid]
            ps.append([px, pid])
        ps.sort()
        for i in range(len(ps) - 1):
            dist = abs(ps[i][0] - ps[i + 1][0])
            if dist <= k:
                union(pas, ps[i][1], ps[i + 1][1])

    fas = defaultdict(list)
    mint = defaultdict(int)
    for i in range(n):
        fi = find(pas, i)
        fas[fi].append(i)
        if fi not in mint:
            mint[fi] = explosion_time[i]
        else:
            mint[fi] = min(mint[fi], explosion_time[i])
    # print("mint", mint)
    fat = [[v, key] for key, v in mint.items()]
    fat.sort()
    # print("pas", pas)
    # print("fat", fat)
    m = len(fat)
    ans = 0
    fat.pop()
    while fat:
        t, node = fat[-1]
        if ans < t:
            ans = ans + 1
        fat.pop()
    return ans

    # print("fas", fas)
    cnt = 0
    st = defaultdict(int)
    ans = 0
    mines = []
    time = defaultdict(list)
    for i in range(n):
        mines.append([explosion_time[i], i])
        time[explosion_time[i]].append(i)

    mines.sort(reverse=True)

    # print("time", time)
    # cnt_time = 0
    # for i in range(n):
    #     pid = mines[i][1]
    #     if st[pid] == 1:
    #         continue

    #     if st[pid] == 0:
    #         cnt += 1
    #         st[pid] = 1
    #         fpid = find(pas, pid)
    #         for ne in fas[fpid]:
    #             if st[ne] == 0:
    #                 st[ne] = 1
    #                 cnt += 1

    #     flag = True
    #     if cnt_time in time:
    #         for j in time[cnt_time]:
    #             if st[j] == 0:
    #                 flag = False
    #                 st[j] = 1
    #                 cnt += 1
    #                 # print("pid", j, cnt)
    #             fj = find(pas, j)
    #             for ne in fas[fj]:
    #                 if st[ne] == 0:
    #                     flag = False
    #                     st[ne] = 1
    #                     cnt += 1
    #                     # print("pid", ne, cnt)
    #     if flag:
    #         continue

    #     if cnt == n:
    #         return cnt_time
    #     cnt_time += 1

    # return cnt_time


# sys.setrecursionlimit(200010)
def main():
    test = int(input())

    for idt in range(test):
        _ = input()
        n, k = map(int, input().split())
        points = defaultdict(list)
        explosion_time = defaultdict(list)
        row = defaultdict(list)
        col = defaultdict(list)
        for i in range(n):
            x, y, t = map(int, input().split())
            points[i] = [x, y]
            explosion_time[i] = t
            row[x].append(i)
            col[y].append(i)

        ans = work(n, k, points, explosion_time, row, col)
        print(ans)


if __name__ == "__main__":
    main()
