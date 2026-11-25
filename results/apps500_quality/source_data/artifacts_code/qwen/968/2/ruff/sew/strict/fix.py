

def  can_sort_by_handle(n: int, handles: list[list[str]], p: list[int]) -> str:
    for  i in  range(0, n):
        handles[p[i] - 1].append(str(1 + i))

    for  i in  range(0, n):
        handles[i].sort(key=lambda x: (x[0], x[1]))

    for  i in  range(0, n):
        handles[i].sort(key=lambda x: int(x[2]))

    for  i in  range(0, n):
        for  j in  range(i + 1, n):
            if  handles[p[i] - 1][0] > handles[p[j] - 1][0]:
                return "NO"

    return  "YES"

# Read input
n = int(input())
handles, p = [input().split() for _ in range(n)], list(map(int, input().split()))

# Output result
print(can_sort_by_handle(n, handles, p))
