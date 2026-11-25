import sys

for _ in range(int(sys.stdin.readline())):
    t, s = sys.stdin.readline().strip(), ''
    for  i in  range(len(t)):
        s+=t[i]*(1 + len(t))
    print(s)