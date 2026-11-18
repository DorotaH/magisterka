'''input
aabc
'''


def list_input():
    return  list(map(int,input().split()))
def map_input():
    return  map(int,input().split())
def map_string():
    return  input().split()

s=input()
a, b = s.count('a'), s.count('b')
c, ans = s.count('c'), "YES"
if(a == 0 or b == 0): ans = "NO"
if(c != a and c != b): ans = "NO"
for i in range(len(s)-1):
	if(s[i] > s[1+i]): ans="NO"
print(ans)
