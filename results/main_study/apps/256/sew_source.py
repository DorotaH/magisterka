a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))


x,y = list(map(int,input().split()))
z,w = list(map(int,input().split()))


Team1=Team2=False
if(w<a and  y<a and  x<d and  z<d):
    Team1=True

if(w<c and  y<c and  x<b and  z<b):
    Team1=True

if(((b<x and  c<w) or  (b<z and  c<y)) and  ((d<x and  a<w) or  (d<z and  a<y))):
    Team2=True


if(Team1):
    print("Team 1")
elif(Team2):
    print("Team 2")
else:
    print("Draw")