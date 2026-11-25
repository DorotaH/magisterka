s = input()

n = len(s)
prefix_sum = [0] * (1 + n)
prefix_sum[0] = 0

for i in range(1, 1 + n):
    if (
        s[i - 1] == "h"
        or s[i - 1] == "e"
        and prefix_sum[i - 1] > 0
        or s[i - 1] == "a"
        and prefix_sum[i - 1] > 1
        or s[i - 1] == "v"
        and 2 < prefix_sum[i - 1]
        or s[i - 1] == "y"
        and prefix_sum[i - 1] > 3
        or s[i - 1] == "m"
        and prefix_sum[i - 1] > 4
        or s[i - 1] == "e"
        and 5 < prefix_sum[i - 1]
        or s[i - 1] == "t"
        and 6 < prefix_sum[i - 1]
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
