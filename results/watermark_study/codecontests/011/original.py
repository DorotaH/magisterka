
def naiveSolve():
    
    
    
    return



def main():
    
    allans=[]
    t=int(input())
    for _ in range(t):
        input()
        n,k=readIntArr()
        adj=[[] for __ in range(n)]
        for __ in range(n-1):
            u,v=readIntArr()
            u-=1;v-=1
            adj[u].append(v)
            adj[v].append(u)
        if k==2:
            allans.append((n*(n-1))//2)
            continue
        
        # for k>2, need a central node
        centralNodes=[]
        for node in range(n):
            if len(adj[node])>=k: # need at least k degree
                centralNodes.append(node)
        
        ans=0
        for cn in centralNodes:
            v=[False]*n
            v[cn]=True
            groups=[] # store [group] where group contains all elements from one of cn's immediate neighbour
            for nex in adj[cn]:
                v[nex]=True
                groups.append([nex])
            while len(groups)>=k:
                # print(groups)##
                
                N=len(groups)
                M=k
                dp=[[0 for __ in range(M+1)] for ___ in range(N)]
                # dp[i][j] = number of ways to choose j nodes from up to idx i
                # dp[n-1][r]
                for i in range(N):
                    dp[i][0]=1
                dp[0][1]=len(groups[0])
                for i in range(1,N):
                    for j in range(1,M+1):
                        dp[i][j]=dp[i-1][j]+dp[i-1][j-1]*len(groups[i]) # don't take i + take i
                        dp[i][j]%=MOD
                ans+=dp[N-1][M]
                ans%=MOD
                # for row in dp: ###
                #     print(row)
                # update groups
                groups2=[]
                for gp in groups:
                    temp=[]
                    for node in gp:
                        for nex in adj[node]:
                            if v[nex]: continue
                            v[nex]=True
                            temp.append(nex)
                    if len(temp)>0:
                        groups2.append(temp)
                groups=groups2
        allans.append(ans)
    multiLineArrayPrint(allans)
    
    return



import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(l,r):
    print('? {} {}'.format(l,r))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(x):
    print('! {}'.format(x))
    sys.stdout.flush()
 
inf=float('inf')
MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()