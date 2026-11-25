def max_segments(n, b, a, s):
    max_segments = 0
    current_battery, current_accumulator = b, a

    for i in range(0, n):
        if s[i] == 1:
            if current_battery > 0:
                current_battery -= 1
                current_accumulator += 1
                max_segments += 1
            elif current_accumulator > 0:
                current_accumulator -= 1
                max_segments += 1
        else:
            if current_battery > 0:
                current_battery -= 1
                max_segments += 1
            elif current_accumulator > 0:
                current_accumulator -= 1
                max_segments += 1
            else:
                break

    return  max_segments


# Read input
import sys

input=sys.stdin.read
data=input().split()
n, b = int(data[0]), int(data[1])
a, s = int(data[2]), list(map(int, data[3:]))

# Output the result
print(max_segments(n, b, a, s))