from collections import Counter, defaultdict
from sys import stdin,stdout
import io , os , sys
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
input = stdin.readline


def mapinput():
    return  map(int, input().split())

def listinput():
    return  list( map( int, input().split()))

def intinput():
    return int(stdin.readline())

def strinput():
    return input().strip()

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    ans = []
    for p in range(n + 1):
        if prime[p]:
            ans.append(p)
    return ans

def writ(ss):
    stdout.write(str(ss) + "\n")



for test in range(int(input())):
    def solve():
        n = intinput()
        s = strinput()
        cc = Counter(s)
        #print(cc)
        if cc['2'] == 1 or cc['2'] == 2:
            print("NO")
            return
        ans = [["X"] * n  for i in range(n) ]
        for i in range(n):
            flag = 0
            for j in range(i+1 , n):
                if s[i] == '1' or s[j] == '1':
                    ans[i][j] = "="
                    ans[j][i] = '='
                else:
                    if flag == 0:
                        ans[i][j] = "+"
                        ans[j][i] = "-"
                        flag = 1 
                    else:
                        ans[i][j] = "-"
                        ans[j][i] = "+"
        print("YES")
        for i in range(n):
            print(''.join(ans[i]))
        


                
                

                

    
           
             
    solve()

