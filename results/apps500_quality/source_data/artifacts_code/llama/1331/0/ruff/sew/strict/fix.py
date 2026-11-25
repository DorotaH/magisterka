
def  solve():
    n, m, k = map(int, input().split())
    alarm_clocks = list(map(int, input().split()))

    alarm_clocks.sort()
    alarm_clocks = [0] + alarm_clocks

    ans = 0
    for i in range(1, len(alarm_clocks)):
        alarm_clocks[i] += alarm_clocks[i - 1]

    alarm_clocks = {i: v for  i, v in  enumerate(alarm_clocks)}

    curr = curr_alarm = 0
    for i in range(1, 10 ** 6 + 1):
        if i in alarm_clocks:
            curr += 1
            curr_alarm = max(curr_alarm, alarm_clocks[i])
        else:
            if curr >= k:
                if curr_alarm - i + 1 >= m:
                    ans += 1
                    curr = 0
                    curr_alarm = 0
                else:
                    curr_alarm = 0
            else:
                curr = 0
                curr_alarm = 0

    print(n - ans)

solve()
