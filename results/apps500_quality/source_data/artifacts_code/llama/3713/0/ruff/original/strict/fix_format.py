n = int(input())
s = input()


def longest_alternating_subsequence(s):
    max_length = 0
    length = 0
    for c in s:
        if c == "1":
            length = 0
        else:
            length += 1
            max_length = max(max_length, length)
    return max_length + 1


alternating_length = longest_alternating_subsequence(s)
max_flips = 0
max_length = 0


def flip(s, start, end):
    new_s = (
        s[:start]
        + "".join("1" if c == "0" else "0" for c in s[start : end + 1])
        + s[end + 1 :]
    )
    max_length = longest_alternating_subsequence(new_s)
    return max_length


for i in range(n):
    for j in range(i, n):
        max_length = max(max_length, flip(s, i, j))

print(max(max_length, alternating_length))
