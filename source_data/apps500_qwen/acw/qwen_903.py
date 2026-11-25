s = input().strip()
n = len(s)
is_s_palindrome = all(s[i] == s[n - i - 1] for i in range(n // 2))
print("TAK" if is_s_palindrome else "NIE")
