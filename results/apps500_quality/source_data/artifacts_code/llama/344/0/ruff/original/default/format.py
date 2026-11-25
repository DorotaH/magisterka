s = input()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

for i in range(len(s) - 1):
    if s[i] not in vowels and s[i] != "n" and s[i + 1] not in vowels:
        print("NO")
        break
else:
    print("YES")
