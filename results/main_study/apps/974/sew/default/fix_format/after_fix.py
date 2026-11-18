import sys


def main():
    n=int(input())
    n = n*2
    u=0
    res, x = 0, []
    for  i in  range(n):
        s = sys.stdin.readline()
        if not s[0] == 'r':
            a,b = s.split()
            x.append(int(b))
        else:
            u+=1
            if len(x)==0:
                continue
            if x[-1] == u:
                x.pop()
            else:
                x = []
                res +=1
    print(res)


main()
