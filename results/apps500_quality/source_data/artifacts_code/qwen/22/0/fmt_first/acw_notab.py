def is_s_palindrome(s):
    n = len(s)
    mid = n // 2
    return (
        s[:mid] == s[mid:][::-1]
        if n % 2 == 0
        else s[:mid] == s[mid + 1 :][::-1]
    )


s = input().strip()
print("TAK" if is_s_palindrome(s) else "NIE")
