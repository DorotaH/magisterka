import os
import sys
import math
from  io import  BytesIO, IOBase
from  collections import  deque,defaultdict,OrderedDict,Counter
from  heapq import  heappush,heappop,heapify
from  bisect import  bisect_right,insort,bisect_left
from  functools import  lru_cache
from  itertools import  permutations

sys.setrecursionlimit(10**6)


def  STRIN():return  input()
def  INTIN():return  int(input())
def  LINT():return  list(map(int,input().split()))
def  LSTR():return  list(map(str,input().split()))
def  MINT():return  map(int,input().split())
def  MSTR():return  map(str,input().split())



def  solve():
   
   
    
    n,m=map(int,input().split())

    s=[]
    d={}

    for  i in  range(0, n):
        s.append(list(input()))


    for  j in  range(0, n):
        for  k in  range(0, len(s[i])):
            if  (k+1)%2==0:
                s[j][k]=chr(90-(26+ord(s[j][k])-91))


    for  i in  range(0, len(s)):
        d[''.join(s[i])]=i+1


    s.sort()

    for  i in  s:
        print(d[''.join(i)],end=" ")



    



    



 
        
 
 
    

def  main():
    #for _ in range(INTIN()):
    solve()
        





# region fastio

BUFSIZE=8192


class  FastIO(IOBase):
    newlines=0

    def __init__(self, file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="x" in  file.mode or  "r" not  in file.mode
        self.write=self.buffer.write if  self.writable else None

    def read(self):
        while  True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()

    def readline(self):
        while  0 == self.newlines:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()

    def flush(self):
        if  self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class  IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda  s: self.buffer.write(s.encode("ascii"))
        self.read=lambda: self.buffer.read().decode("ascii")
        self.readline=lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout=IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input=lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__=="__main__":
    main()

