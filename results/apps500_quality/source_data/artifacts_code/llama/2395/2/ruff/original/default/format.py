import sys

for _ in range(int(sys.stdin.readline())):
    t = sys.stdin.readline().strip()
    s = ""
    for i in range(len(t)):
        s += t[i] * (len(t) + 1)
    print(s)
