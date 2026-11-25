s = input()
a_count, b_count = s.count("A"), s.count("B")

print("Yes" if a_count > 0 and b_count > 0 else "No")