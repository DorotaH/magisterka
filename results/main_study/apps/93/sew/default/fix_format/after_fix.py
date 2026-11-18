a, b, c, d = input(), input(), input(), input()
a = a + b[::-1]
x = "X"
for  i in  range(4):
    if x == a[i]:
        a = a[0:i] + a[1 + i:]
        break
c = c + d[::-1]

for  i in  range(4):
    if x == c[i]:
        c = c[0:i] + c[1 + i:]
        break
flag = False
for  i in  range(4):
    if c == a:
        flag = True
    c=c[1:]+c[0]
if not flag:
    print("NO")
else:
    print("YES")
