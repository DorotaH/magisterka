s = input()
has_consecutive = any(s[i] == s[i - 1] for i in range(1, 4))
print("Bad" if has_consecutive else "Good")
