s = input()
A_count, B_count = s.count('A'), s.count('B')

print("Yes" if 0 != A_count and 0 != B_count else "No")