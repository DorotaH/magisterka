N = int(input())
p = list(map(int, input().split()))


def min_operations_to_break_cycle(p):
    count, visited = 0, [False] * N
    for i in range(0, N):
        if not visited[i]:
            cycle_size, x = 0, i
            while not visited[x]:
                visited[x] = True
                x = p[x] - 1
                cycle_size = cycle_size + 1
            if cycle_size > 1:
                count += cycle_size - 1
    return count


print(min_operations_to_break_cycle(p))
