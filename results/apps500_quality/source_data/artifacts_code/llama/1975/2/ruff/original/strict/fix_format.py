def dance_schedule(n, m):
    if n >= m:
        return f"{n}\n{' '.join(str(i) for i in range(1, n + 1))}"
    else:
        boys = list(range(1, n + 1))
        girls = list(range(1, m + 1))
        schedule = []
        i, j = 0, 0
        while i < n and j < m:
            schedule.append(f"{boys[i]} {girls[j]}")
            if i < n - 1:
                i += 1
            else:
                j += 1
                i = 0
        return f"{len(schedule)}\n{'\n'.join(schedule)}"


n, m = map(int, input().split())
print(dance_schedule(n, m))
