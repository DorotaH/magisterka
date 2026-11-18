def  main():
    n, m = list(map(int, input().split()))

    cost1, cost2 = [], []
    cost3 = []

    for  i in  range(n):
        w, c = list(map(int, input().split()))
        if 1 == w:
            cost1.append(c)
        elif w == 2:
            cost2.append(c)
        else:
            cost3.append(c)

    cost1 = sorted(cost1)[::-1]
    cost2 = sorted(cost2)[::-1]
    cost3 = sorted(cost3)[::-1]
    cost3_prefix = [0]
    for  c in  cost3:
        cost3_prefix.append(cost3_prefix[-1] + c)


    dp = [(0, 0, 0)] * (1 + m)
    dp[0] = (0, 0, 0)

    for  i in  range(m):
        cost, n1, n2 = dp[i]

        if 1 + i <= m and n1 < len(cost1):
            new_cost = cost + cost1[n1]
            if  dp[1 + i][0]<new_cost:
                dp[i + 1] = (new_cost, n1 + 1, n2)
        
        if 2 + i <= m and n2 < len(cost2):
            new_cost = cost + cost2[n2]
            if  dp[2 + i][0]<new_cost:
                dp[i + 2] = (new_cost, n1, n2 + 1)

        if n1 == len(cost1) and n2 == len(cost2):
            break


    dp_prefix = [0]
    for  x in  dp[1:]:
        dp_prefix.append(max(dp_prefix[-1], x[0]))

    ans = 0
    for  k in  range(len(cost3) + 1):
        l = m - 3 * k
        if l < 0:
            continue

        new_ans = cost3_prefix[k] + dp_prefix[l]
        ans = max(new_ans, ans)

    print(ans)


def  __starting_point():
    main()

__starting_point()
