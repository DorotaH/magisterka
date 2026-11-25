def max_segments(n, b, a, s):
    battery = b
    accumulator = a
    current = 0
    max_segments = 0

    for i in range(n):
        if s[i] == 1:
            if accumulator > 0:
                accumulator -= 1
                if battery > 0:
                    battery -= 1
                    accumulator += 1
                else:
                    battery = 0
            else:
                break
        else:
            if battery > 0:
                battery -= 1
            else:
                break
        current += 1

    return current


# Read input
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

# Output the result
print(max_segments(n, b, a, s))
