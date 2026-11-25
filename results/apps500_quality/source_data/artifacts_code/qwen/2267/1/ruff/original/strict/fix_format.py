def smallest_concatenation(strings):
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if strings[i] + strings[j] > strings[j] + strings[i]:
                strings[i], strings[j] = strings[j], strings[i]
    return "".join(strings)


# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Output the result
print(smallest_concatenation(strings))
