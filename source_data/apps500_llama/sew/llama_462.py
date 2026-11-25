import  sys

for _ in range(0, int(sys.stdin.readline())):
    t, s = sys.stdin.readline().strip(), ''
    for  i in  range(0, len(t)):
        s+=t[i]*(1 + len(t))
    print(s)