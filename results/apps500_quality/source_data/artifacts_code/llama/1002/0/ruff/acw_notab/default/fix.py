

def solve():
    n, d = map(int, input().split())
    t = list(map(int, input().split()))
    total_time = sum(t)
    if total_time + 10 * (n - 1) > d:
        print(-1)
        return
    t.sort()
    time_for_jokes = 0
    num_jokes = 0
    for i in range(n):
        time_for_jokes += t[i]
        time_for_jokes += 10
        if time_for_jokes <= d:
            num_jokes += (d - time_for_jokes) // 5
            time_for_jokes += 5 * ((d - time_for_jokes) // 5)
        else:
            break
    print(num_jokes)


if __name__ == "__main__":
    solve()
