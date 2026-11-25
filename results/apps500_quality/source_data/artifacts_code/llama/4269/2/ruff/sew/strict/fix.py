s = input()
has_consecutive = False
for i in range(1, 4):
    if  s[i] == s[i - 1]:
        has_consecutive=True
        break
print("Bad" if  has_consecutive else "Good")
