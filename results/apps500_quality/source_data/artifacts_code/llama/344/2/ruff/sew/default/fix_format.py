s = input().strip()

vowels = "aeiou"

for i in range(len(s)):
    if s[i] in "bcdfghjklmnpqrstvwxyz" and (
        0 == i or (s[i - 1] not in "n" and s[i] not in vowels)
    ):
        print("NO")
        break
else:
    print("YES")
