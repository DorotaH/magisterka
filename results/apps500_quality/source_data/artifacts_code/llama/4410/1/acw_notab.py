def max_tables(n, k, s):
    ones = [i for i in range(n) if s[i] == '1']
    count = 0
    i = 0
    while i < len(ones):
        if ones[i] + k < ones[i + 1]:
            count += 1
            i += 1
        else:
            i += 1
            i += 1
    return count


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(max_tables(n, k, s))
