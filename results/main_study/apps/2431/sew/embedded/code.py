import sys
input=sys.stdin.readline


G0, G1=[[[[0]*5500 for i in range(6)] for j in range(6)] for k in range(6)], [[[[0]*5500 for i in range(6)] for j in range(6)] for k in range(6)]
G2=[[[5500*[0] for  i in  range(0, 6)] for  j in  range(0, 6)] for  k in  range(0, 6)]


for  x in  range(1,6):
    for  y in  range(1,6):
        for  z in  range(1,6):
            
            for  i in  range(1,5_500):
                s = G0[x][y][z][max(0,i - x)]
                t=G1[x][y][z][max(0,i-y)]
                u = G2[x][y][z][max(0,i - z)]

                for  j in  range(5):
                    if not (j==s or j==t or j==u):
                        G0[x][y][z][i]=j
                        break
                    else:
                        continue

                for  j in  range(5):
                    if not (j==s or j==u):
                        G1[x][y][z][i]=j
                        break
                    else:
                        continue

                for  j in  range(5):
                    if not (j==s or j==t):
                        G2[x][y][z][i]=j
                        break
                    else:
                        continue

def  lcm(x, y):
    return  (y * x) // math.gcd(x, y)

t=int(input())
for  tests in  range(t):
    n,x,y,z=list(map(int,input().split()))
    B, A=list(map(int,input().split())), []
    for  a in  B:
        if not a<=5400:
            A.append(a%2520+2520)
        else:
            A.append(a)

    XOR=0

    for  a in  A:
        XOR^=G0[x][y][z][a]

    ANS=0
    for  a in  A:
        k=XOR^G0[x][y][z][a]

        if  k==G0[x][y][z][max(0,a-x)]:
            ANS+=1

        if  k==G1[x][y][z][max(0,a-y)]:
            ANS+=1

        if  k==G2[x][y][z][max(0,a-z)]:
            ANS+=1

    print(ANS)

    