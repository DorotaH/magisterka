import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
n = int(sys.stdin.readline())

a = []
for x in sys.stdin.readline().split():
    a.append(int(x))
front = [0] * (len(a)+2)
for  i in  range(0, n):
    front[i+1]=front[i]+ (1 if (a[i]>=0) else 0 )
back = [0] * (len(a)+2)
for  i in  reversed(range(n)):
    back[i+1]=back[i+2]+ (1 if (a[i]<=0) else 0)
ans = len(a)+1
for  i in  range(1,n):
    ans=min(ans,front[i]+back[i+1])
print("%d" % ans)

