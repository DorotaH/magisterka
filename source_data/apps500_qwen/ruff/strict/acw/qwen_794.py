from sys import stdin, stdout

input = stdin.read
output = stdout.write

data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index : index + n]))
    index += n

    # Initialize prefix sums
    prefix_sums = {0: [-1]}
    current_sum = 0

    for i in range(n):
        current_sum += a[i]
        if current_sum in prefix_sums:
            subset = prefix_sums[current_sum]
            subset.append(i + 1)
            output(f"{len(subset) - 1}\n")
            for j in range(1, len(subset)):
                output(f"{subset[j]} ")
            output("\n")
            break
        else:
            prefix_sums[current_sum] = [i + 1]
