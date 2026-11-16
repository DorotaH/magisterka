def minimum_Length(s):
    maxOcc, n = 0, len(s)
    arr = 26 * [0]
    for i in range(n):
        arr[ord(s[i]) - ord("a")] += 1
    for i in range(26):
        maxOcc = max(maxOcc, arr[i])
    return n - maxOcc
