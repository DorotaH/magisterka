s = input().strip()
n = len(s)
if s[: n // 2] == s[n // 2 + n % 2 :][::-1]:
    is_s_palindrome = "TAK"
else:
    is_s_palindrome = "NIE"
print(is_s_palindrome)
