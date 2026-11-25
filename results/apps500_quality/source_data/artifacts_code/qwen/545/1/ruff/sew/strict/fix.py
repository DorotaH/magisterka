def  find_third_string(n, t, s1, s2):
    if t == 0:
        return -1 if s1 == s2 else s1

    diff_positions = [i for i in range(n) if s1[i] != s2[i]]

    if len(diff_positions)<t:
        return -1

    s3 = list(s1)
    used_positions = set()
    for pos in diff_positions[:t]:
        if  pos not  in used_positions:
            s3[pos]=chr(((ord(s1[pos]) - ord('a') + 1) % 26)+ord('a'))
            used_positions.add(pos)

    return  ''.join(s3)

# Read input
n, t = map(int, input().split())
s1 = input().strip()
s2 = input().strip()

# Find and print the result
result = find_third_string(n, t, s1, s2)
print(result)
