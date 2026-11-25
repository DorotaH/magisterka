a = input()
num = 0
for i, c in enumerate(a):
    if c.isdigit():
        num += int(c) * 16 ** (6 - i)
    elif c == "A":
        num += (16 ** (6 - i)) * 10
ans = int(num % 47 == 0)
print(ans)
