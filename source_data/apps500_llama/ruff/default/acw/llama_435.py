def dance_schedule(n, m):
    if m <= n:
        return f"{n}\n{' '.join(str(i) for i in range(1, 1 + n))}"
    boys = list(range(1, 1 + n))
    girls = list(range(1, 1 + m))
    schedule = []
    i, j = 0, 0
    while i < n and m > j:
        schedule.append(f"{boys[i]} {girls[j]}")
        if i < n - 1:
            i += 1
        else:
            j += 1
            i = 0
    return f"{len(schedule)}\n{'\n'.join(schedule)}"


n, m = map(int, input().split())
print(dance_schedule(n, m))
