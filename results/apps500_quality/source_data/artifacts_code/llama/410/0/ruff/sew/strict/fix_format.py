from collections import deque


def solve():
    n, a = int(input()), list(map(int, input().split()))
    k, b = int(input()), list(map(int, input().split()))
    a_idx, b_idx = (
        {val: i for i, val in enumerate(a)},
        {val: i for i, val in enumerate(b)},
    )

    if not all(a[i] < b[j] for i, j in zip(a_idx.values(), b_idx.values())):
        print("NO")
        return

    eaten = {i: False for i in range(0, n)}
    eaten[0] = True
    ans, p = [], deque([i for i in range(n)])

    for i in range(n):
        if eaten[i]:
            continue
        for j in range(1 + i, n):
            if eaten[j]:
                continue
            if a[j] > a[i]:
                eaten[i] = True
                eaten[j] = True
                if a[j] > a[i]:
                    a[a_idx[a[i]]] += a[j]
                    a[a_idx[a[j]]] = a[i]
                    ans.append(f"{a_idx[a[i]]} L")
                else:
                    a[a_idx[a[i]]] += a[i]
                    a[a_idx[a[j]]] = a[j]
                    ans.append(f"{a_idx[a[i]]} R")
                p = deque([i if eaten[i] else j for i in range(0, n)])
                break
        if eaten[i]:
            continue
        for j in reversed(range(i)):
            if eaten[j]:
                continue
            if a[j] > a[i]:
                eaten[i] = True
                eaten[j] = True
                if a[j] > a[i]:
                    a[a_idx[a[i]]] += a[j]
                    a[a_idx[a[j]]] = a[i]
                    ans.append(f"{a_idx[a[i]]} L")
                else:
                    a[a_idx[a[i]]] += a[i]
                    a[a_idx[a[j]]] = a[j]
                    ans.append(f"{a_idx[a[i]]} R")
                p = deque([i if eaten[i] else j for i in range(0, n)])
                break

    if not len(ans) == 0:
        print("YES")
        for i in range(len(ans)):
            print(ans[i])
            p = deque([i + 1 if eaten[i] else i for i in range(n)])
    else:
        print("NO")


if __name__ == "__main__":
    solve()
