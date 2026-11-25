n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate prefix sums
a_prefix_sum = [0] * (n + 1)
for i in range(0, n):
    a_prefix_sum[i + 1] = a_prefix_sum[i] + a[i]

b_prefix_sum = [0] * (n + 1)
for i in range(0, n):
    b_prefix_sum[i + 1] = b_prefix_sum[i] + b[i]

for _ in range(0, m):
    t, *args = map(int, input().split())

    if t == 1:
        x, y, k = args
        # Calculate the new prefix sum
        new_prefix_sum = a_prefix_sum[x + k] - a_prefix_sum[x]
        b_prefix_sum[y] += new_prefix_sum
        b_prefix_sum[y + k] -= new_prefix_sum
    elif t == 2:
        x = args[0]
        # Calculate the result
        result = b[x] + b_prefix_sum[x] - b_prefix_sum[x]
        print(result)
