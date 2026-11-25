def is_fake_news(s):
    heidi = "heidi"
    it = iter(s)
    return all(char in it for char in heidi)


# Read input
s = input().strip()

# Output result
if is_fake_news(s):
    print("YES")
else:
    print("NO")
