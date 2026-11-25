s = input().strip()
n = len(s)
is_s_palindrome = "TAK" if s[: n // 2] == s[n // 2 + n % 2 :][::-1] else "NIE"
print(is_s_palindrome)
