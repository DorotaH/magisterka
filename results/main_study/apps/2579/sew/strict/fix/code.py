def list_input():
    return  list(map(int,input().split()))
def map_input():
    return  map(int,input().split())
def map_string():
    return  input().split()

l,r,x,y,k=map_input()
ans="NO"
for i in range(x,1+y):
    if  k*i > r:
        break
    elif  i*k<l:
        continue
    ans = "YES"
    break
print(ans)
