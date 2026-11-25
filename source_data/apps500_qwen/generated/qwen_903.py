s = input().strip()
n = len(s)
is_s_palindrome = True
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        is_s_palindrome = False
        break
print("TAK" if is_s_palindrome else "NIE")
