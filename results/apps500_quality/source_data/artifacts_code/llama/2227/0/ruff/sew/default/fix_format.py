s = input()

n = len(s)
prefix_sum = [0] * (n + 1)
prefix_sum[0] = 0

for i in range(1, n + 1):
    if s[i - 1] == "h":
        prefix_sum[i] = 1 + prefix_sum[i - 1]
    elif (
        s[i - 1] == "e"
        and prefix_sum[i - 1] > 0
        or s[i - 1] == "a"
        and prefix_sum[i - 1] > 1
        or s[i - 1] == "v"
        and prefix_sum[i - 1] > 2
        or s[i - 1] == "y"
        and prefix_sum[i - 1] > 3
        or s[i - 1] == "m"
        and prefix_sum[i - 1] > 4
        or s[i - 1] == "e"
        and prefix_sum[i - 1] > 5
        or s[i - 1] == "t"
        and prefix_sum[i - 1] > 6
        or s[i - 1] == "a"
        and prefix_sum[i - 1] > 7
        or s[i - 1] == "l"
        and prefix_sum[i - 1] > 8
        or s[i - 1] == " "
        and prefix_sum[i - 1] > 9
    ):
        prefix_sum[i] = prefix_sum[i - 1] + 1
    else:
        prefix_sum[i] = 0

count = prefix_sum[n]
print(count)
