###pyrival template for fast IO
import os
import sys
from  io import  BytesIO, IOBase
##########region fastio
BUFSIZE = 8_192
###pyrival template for fast IO
class FastIO(IOBase):
    newlines=0
    ###pyrival template for fast IO
    def  __init__(self, file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="x" in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    ###pyrival template for fast IO
    def  read(self):
        while  1:
            b=os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines=0
        return  self.buffer.read()
    ###pyrival template for fast IO
    def  readline(self):
        while  self.newlines == 0:
            b=os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines-=1
        return  self.buffer.readline()
    ###pyrival template for fast IO
    def  flush(self):
        if  self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    ###pyrival template for fast IO
    def  __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s: self.buffer.write(s.encode("ascii"))
        self.read=lambda: self.buffer.read().decode("ascii")
        self.readline=lambda: self.buffer.readline().decode("ascii")
###pyrival template for fast IO
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")



###pyrival template for fast IO
#####change recurssion limit
from  heapq import  heappush,heappop,heapify
t = int(input())
while t:
    t-=1
    n, arr_=int(input()), [[-int(x),i+1] for i,x in enumerate(input().split())]
    arr = list()
    for  i,j in  arr_:
        if  0!=i:
            heappush(arr,(i,j))
    res = list()
    while len(arr)>1:
        a,ai = heappop(arr)
        b,bi = heappop(arr)
        a *= -1
        b *= -1
        a=a-1
        b=b-1
        res.append((ai,bi))
        if a:
            heappush(arr,(-a,ai))
        if b:
            heappush(arr,(-b,bi))

    sys.stdout.write(f"{len(res)}\n")
    for  i,j in  res:
        sys.stdout.write(f"{i} {j}\n")
