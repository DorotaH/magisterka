# Your code here
#!/usr/bin/env python
# from __future__ import division, print_function
import math
import os
# from fractions import *
import sys
sys.setrecursionlimit(2*(10**5))
from  decimal import  *
from  io import  BytesIO, IOBase
import threading
from  itertools import  *
from  collections import  *
from  array import  *
import random
M=7 + 10 ** 9
import heapq
import bisect
from  functools import  lru_cache
from  queue import  PriorityQueue
BUFSIZE=8_192
class  FastIO(IOBase):
    newlines=0
    def  __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def  read(self):
        while True:
            b=os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if  not  b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def  readline(self):
        while 0 == self.newlines:
            b=os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines=b.count(b"\n")+(not  b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def  flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class  IOWrapper(IOBase):
    def  __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start=True
    for x in args:
        if  not  at_start:
            file.write(sep)
        file.write(str(x))
        at_start=False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input=lambda: sys.stdin.readline().rstrip("\r\n")


def inp(): return  sys.stdin.readline().rstrip("\r\n")  # for fast input


def out(var): sys.stdout.write(str(var))  # for fast output, always take string


def lis(): return  list(map(int, inp().split()))


def stringlis(): return  list(map(str, inp().split()))


def sep(): return  map(int, inp().split())


def strsep(): return  map(str, inp().split())


def fsep(): return  map(float, inp().split())


def inpu(): return  int(inp())


# -----------------------------------------------------------------

def regularbracket(t):
    p=0
    for i in t:
        if not i == "(":
            p -= 1
        else:
            p += 1
        if  p < 0:
            return False
    else:
        if not p > 0:
            return True
        else:
            return False
# -------------------------------------------------
def binarySearchcount(arr, n, key):
    left=0
    right, count = n - 1, 0
    while (right >= left):
        mid = ((left + right) // 2)
        # Check if middle element is
        # less than or equal to key
        if (arr[mid] <= key):
            count = mid + 1
            left = mid + 1
        # If key is smaller, ignore right half
        else:
            right = mid - 1
    return  count
#--------------------------------------------------binery search


def binarySearch(arr, n, key):
    left, right = 0, n - 1
    while (right >= left):
        mid = ((left + right) // 2)
        if arr[mid] == key:
            return mid
        if (arr[mid] <= key):
            left = mid + 1
        # If key is smaller, ignore right half
        else:
            right = mid - 1
    return  -1



#-------------------------------------------------ternary search
def ternarysearch(arr,n,key):
    l,r=0,n-1
    while(r>=l):
        mid = (-l+r)//3 + l
        mid2 = mid + (-l+r)//3
        if arr[mid]==key:
            return mid
        if arr[mid2]==key:
            return mid2
        if key<arr[mid]:
            r = mid - 1
        elif arr[mid2]<key:
            l = 1+mid2
        else:
            l, r=mid+1, mid2-1
    return  -1
# ------------------------------reverse string(pallindrome)
def reverse1(string):
    pp=""
    for i in string[::-1]:
        pp+=i
    if string == pp:
        return True
    return  False
# --------------------------------reverse list(paindrome)
def reverse2(list1):
    l = []
    for i in list1[::-1]:
        l.append(i)
    if list1 == l:
        return True
    return  False


def sumofdigits(n):
    n=str(n)
    s1=0
    for i in n:
        s1 = s1 + int(i)
    return  s1


def perfect_square(n):
    s=math.sqrt(n)
    if s==int(s):
        return True
    return  False



# -----------------------------roman
def roman_number(x):
    if x>15999:
        return
    value, symbol = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], ["F", "MF", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman, i = "", 0
    while x>0:
        div = x // value[i]
        x %= value[i]
        while div:
            roman+=symbol[i]
            div -= 1
        i += 1
    return  roman
def soretd(s):
    for i in range(1, len(s)):
        if  s[i - 1] > s[i]:
            return False
    return  True
# print(soretd("1"))
# ---------------------------
def countRhombi(h, w):
    ct=0
    for i in range(2, h + 1, 2):
        for j in range(2, w + 1, 2):
            ct += (h - i + 1) * (w - j + 1)
    return  ct
def countrhombi2(h, w):
    return  ((h*h)//4)*((w*w)//4)
# ---------------------------------
def binpow(a, b):
    if not b == 0:
        res = binpow(a, b // 2)
    else:
        return 1
    if not b % 2 != 0:
        return res * res
    else:
        return res * res * a


# -------------------------------------------------------
"""

"""
# -------------------------------------------------------------
def coprime_to_n(n):
    result, i = n, 2
    while (i*i<=n):
        if (n % i == 0):
            while (n % i == 0):
                n //= i
            result = result - result // i
        i += 1
    if (n>1):
        result = result - result // n
    return  result


def luckynumwithequalnumberoffourandseven(x,n,a):
    if not (x >= n and str(x).count("4") == str(x).count("7")):
        if x < 1e12:
            luckynumwithequalnumberoffourandseven(x * 10 + 4,n,a)
            luckynumwithequalnumberoffourandseven(x * 10 + 7,n,a)
    else:
        a.append(x)
    return  a
#----------------------
def luckynum(x,l,r,a):
    if x>=l and r>=x:
        a.append(x)
    if x>r:
        a.append(x)
        return a
    if x<1e10:
            luckynum(x * 10 + 4, l,r,a)
            luckynum(x * 10 + 7, l,r,a)
    return  a


def luckynuber(x, n, a):
    p=set(str(x))
    if len(p)<=2:
        a.append(x)
    if n > x:
        luckynuber(x + 1, n, a)
    return  a


# ------------------------------------------------------interactive problems
def interact(type, x):
    if not type == "r":
        print(x, flush=True)
    else:
        inp = input()
        return inp.strip()
# ------------------------------------------------------------------zero at end of factorial of a number
def findTrailingZeros(n):
    # Initialize result
    count=0

    # Keep dividing n by
    # 5 & update Count
    while (n>=5):
        n //= 5
        count += n

    return  count


# -----------------------------------------------merge sort
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while  i < len(L) and  j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while  i < len(L):
            arr[k]=L[i]
            i += 1
            k += 1
        while  j < len(R):
            arr[k]=R[j]
            j += 1
            k += 1
# -----------------------------------------------lucky number with two lucky any digits
def solven(p, l, a, b, n,res):  # given number
    if p > n or l>10:
        return None
    if p>0:
        res.add(p)
    solven((p * 10)+a, l + 1, a, b, n)
    solven((p * 10)+b, l + 1, a, b, n)

"""
"""
def subsetsUtil(A, subset, index, d):
    print(*subset)
    s=sum(subset)
    d.append(s)
    for i in range(index, len(A)):
        subset.append(A[i])
        subsetsUtil(A, subset, i + 1, d)
        subset.pop(-1)
    return  d
def subsetSums(arr, l, r, d, sum=0):
    if l > r:
        d.append(sum)
        return
    subsetSums(arr, l + 1, r, d, sum+arr[l])
    # Subset excluding arr[l]
    subsetSums(arr, l + 1, r, d, sum)
    return  d


def print_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return  (factors)
# -----------------------------------------------
def calc(X, d, ans, D):
    # print(X,d)
    if 0 == len(X):
        return None
    i=X.index(max(X))
    ans[D[max(X)]]=d
    Y, Z = X[:i], X[i + 1:]
    calc(Y, d + 1, ans, D)
    calc(Z, d + 1, ans, D)


def generate(st, s):
    if 0 == len(s):
        return None
    if s not in st:
        st.add(s)
        for i in range(0, len(s)):
            t = list(s).copy()
            t.remove(s[i])
            t = ''.join(t)
            generate(st, t)
    return
#=--------------------------------------------longest increasing subsequence
def largestincreasingsubsequence(A):
    l=[1]*len(A)
    for i in range(1,len(l)):
        for k in range(0, i):
            if  A[i]>=A[k]:
                l[i]=max(l[i],1+l[k])
    return  max(l)
#----------------------------------Function to calculate Bitwise OR of sums of all subsequences
def findOR(nums, N):
    prefix_sum = result = 0
    for i in range(0, N):
        result = result | nums[i]
        prefix_sum = prefix_sum + nums[i]
        result = result | prefix_sum
    return  result
def OR(a, n):
    ans=a[0]
    for i in range(1, n):
        ans|=a[i]
        #l.append(ans)
    return  ans
def toString(List):
    return  ''.join(List)
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r,p):
    if not l == r:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r,p)
            a[l], a[i] = a[i], a[l]  # backtrack
    else:
        p.append(toString(a))
def squareRoot(number, precision):
    start=0
    end, ans = number, 1
    while (end >= start):
        mid = int((end + start) / 2)
        if (mid * mid == number):
            ans = mid
            break
        if (mid * mid < number):
            start = mid + 1
        else:
            end = mid - 1
    increment=0.1
    for i in range(0, precision):
        while  (ans*ans<=number):
            ans += increment
        ans = ans - increment
        increment=increment/10
    return  ans
def countRectangles(l, w):
    squareSide=math.gcd(l, w)
    return  int((w * l)/(squareSide*squareSide))
# Function that count the
# total numbersProgram between L
# and R which have all the
# digit same
def count_same_digit(L, R):
    tmp=0
    ans, n = 0, int(math.log10(R) + 1)
    for i in range(0, n):
        # tmp has all digits as 1
        tmp=tmp * 10 + 1
        for j in range(1, 10):

            if  (L <= (j * tmp) and  (j * tmp) <= R):
                #print(tmp*j)
                # Increment the required count
                ans += 1
    return  ans
#----------------------------------print k closest number of a number in an array
def findCrossOver(arr, low, high, x):
    # Base cases
    if (x >= arr[high]):  # x is greater than all
        return high
    if (arr[low] > x):  # x is smaller than all
        return low
    # Find the middle point
    mid=(low+high)//2
    if (x >= arr[mid] and arr[1 + mid]>x):
        return mid
    if (x > arr[mid]):
        return findCrossOver(arr, mid + 1, high, x)
    return  findCrossOver(arr, low, mid-1, x)
def Kclosest(arr, x, k, n,ans):
    # Find the crossover point
    l=findCrossOver(arr, 0, n-1, x)
    r, count = l + 1, 0
    if (x == arr[l]):
        l = l - 1
    #print(l)
    while (l>=0 and n > r and k > count):
        if (x - arr[l] < arr[r] - x):
            ans.append(arr[l])
            l -= 1
        else:
            ans.append(arr[r])
            r += 1
        count += 1
    while (k > count and l>=0):
        ans.append(arr[l])
        l -= 1
        count += 1
    while (k > count and n > r):
        ans.append(arr[r])
        r += 1
        count += 1
    return  ans


def dfs(root,nodeVal,nodeConnection,visited):
    leftVal, rightVal = nodeVal[root][0], nodeVal[root][1]
    solution=list()
    if not nodeConnection[root]:
        return ((leftVal, 0), (rightVal, 0))
    else:
        visited.add(root)
        for i in nodeConnection[root]:
            if i not in visited:
                solution.append(dfs(i,nodeVal,nodeConnection,visited))
        leftMax = 0
        rightMax = 0
        for i in solution:
            l, r = i
            leftMax += max(abs(leftVal - l[0]) + l[1], abs(leftVal - r[0]) + r[1])
            rightMax += max(abs(rightVal - l[0]) + l[1], abs(rightVal - r[0]) + r[1])
        return ((leftVal, leftMax), (rightVal, rightMax))



def luckynumber(x, n, a):
    if x>0:
        a.append(x)
    if not x > 10 ** 9:
        if x < 1e12:
            luckynumber(x * 10 + 4, n, a)
            luckynumber(x * 10 + 7, n, a)
    else:
        return a


def lcm(a, b):
    return  (b * a)//math.gcd(a, b)


def query1(l, r):
    if l >= r:
        return -1
    print('?', l + 1, r + 1)
    sys.stdout.flush()
    return  int(input())-1


def answer(p):
    print('!', p + 1)
    sys.stdout.flush()
    exit()


# ---------------------count number of primes
def buildPrefix(MAX,prefix):
    prime, p = [1] * (MAX + 1), 2
    while (p*p<=MAX):
        if (prime[p] == 1):
            i = 2 * p
            while (i <= MAX):
                prime[i] = 0
                i += p
        p += 1
    for p in range(2, MAX + 1):
        prefix[p]=prefix[p-1]
        if  (prime[p] == 1):
            prefix[p] += 1
def query(L, R , prefix):
    return  prefix[R]-prefix[L-1]
#buildPrefix()

def maxSubArraySum(a, size):
    max_so_far, curr_max = a[0], a[0]
    for i in range(1, size):
        curr_max=max(a[i], curr_max+a[i])
        max_so_far=max(max_so_far, curr_max)
    return  max_so_far


def solvepp(n,k):
    if 1==n and 1==k:
        return 0
    mid=(2**(n-1))//2
    if not k<=mid:
        return solvepp(n-1,k-(mid))==0
    else:
        return solvepp(n-1,k)

#------------------print subset of strings
def solvr(s,p):
    if 0==len(s):
        print(p,end=" ")
        return None
    op1, op2=p, p+s[0]
    s=s[1:]
    solvr(s,op1)
    solvr(s,op2)
    return
#-------------------------------------balanced paranthesis
def paranthesis(n,m,ans,l):
    if 0==n and 0==m:
        print(ans)
        return None
    if 0!=n:
        op1 = ans + "("
        paranthesis(n - 1,m,op1,l)
    if m>n:
        op2 = ans + ")"
        paranthesis(n,m - 1,op2,l)
"""
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlis:
    def __init__(self):
        self.head=None
    def printlis(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def pushfirst(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def pushmid(self,previous_node,new_data):
        new_node=node(new_data)
        if previous_node==None:
            print("call pushfirst function if it is the the start otherwise raise an error.")
        new_node.next=previous_node.next
        previous_node.next=new_node
    def pushlast(self,new_data):
        new_node=node(new_data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while(last.next!=None):
            last=last.next
        last.next=new_node
    def delete_node(self,key):
        pass
if __name__ == '__main__':
    l=linkedlis()
    l.head= node(1)
    p = node(2)
    pp = node(4)
    l.head.next = p
    p.next = pp
    #print(l.head)
    l.pushmid(p, 3)
    l.pushlast(5)
    l.pushfirst(0)
    #l.printlis()
    #print(l.head.data)
"""
def rse(arr, n):
    stack, ans = [], []
    for i in reversed(range(n)):
        if not len(stack) == 0:
            while (len(stack) != 0):
                if stack[-1][0] >= arr[i]:
                    stack.pop()
                else:
                    break
            if len(stack) == 0:
                ans.append(n)
            else:
                ans.append(stack[-1][1])
        else:
            ans.append(n)
        stack.append([arr[i], i])
    ans.reverse()
    return  ans


def lse(arr, n):
    stack, ans = [], []
    for i in range(0, n):
        if not len(stack) == 0:
            while (len(stack) != 0):
                if stack[-1][0] >= arr[i]:
                    stack.pop()
                else:
                    break
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
        else:
            ans.append(-1)
        stack.append([arr[i], i])
    return  ans


def mah(arr):
    max1=0
    p, q = rse(arr, len(arr)), lse(arr, len(arr))
    for i in range(0, len(arr)):
        a=(p[i]-q[i]-1)*arr[i]
        max1=max(a, max1)
    return  max1


def lcs(s,r):
    rr, ss=len(r), len(s)
    l=[[0]*(rr+1) for  i in  range(ss+1)]
    for i in range(1,ss+1):
        for j in range(1,rr+1):
            if not s[i-1]==r[j-1]:
                l[i][j] =max(l[i-1][j],l[i][j-1])
            else:
                l[i][j]=l[i-1][j-1]+1
    return  l[ss][rr]


def subsetsum(arr,sum,len):
    dp=[[False]*(sum+1) for  i in  range(len+1)]
    for i in range(0, len+1):
        dp[i][0]=True
    for i in range(1,len+1):
        for j in range(1,sum+1):
            #print(dp[i][j])
            if not arr[i-1]>j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return  dp[len][sum]


def matrixmincost(cost,n,m):
    dp = []
    for x in range(n):
        dp.append([0 for x in range(m)])
    for i in range(0, n):
        for j in range(0, m):
            if  i==0 and  j==0:
                dp[i][j]=cost[i][j]
            elif  i==0 and j!=0:
                dp[i][j] = dp[i][j - 1] + cost[i][j]
            elif  j==0 and i!=0:
                dp[i][j] = dp[i - 1][j] + cost[i][j]
            else:
                dp[i][j]=cost[i][j]+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return  dp[n-1][m-1]
"""
# --------------------------adding any number to get a number
"""
def coinchange(n,arr,len1):
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(0, len1):
        for j in range(arr[i],n+1):
            dp[j] += dp[j - arr[i]]
    return  dp[n]


class  Graph(object):
    def  __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def  addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def  connectedComponents(self):
        unvisited = set(range(self.V))
        queue = deque()
        count = 0
        while len(unvisited)>0:
            count += 1
            v=next(iter(unvisited))
            unvisited.remove(v)
            queue.append(v)
            while len(queue)>0:
                v = queue.popleft()
                for  w in  self.graph[v]:
                    if  w in  unvisited:
                        unvisited.remove(w)
                        queue.append(w)
        return count
def maxSumIS(arr, n):
    msis=arr.copy()
    for i in range(1, n):
        for j in range(0, i):
            if  (arr[i] > arr[j] and
                    msis[i] < msis[j] + arr[i]):
                msis[i]=msis[j]+arr[i]
    c, p = max(msis), 5
    return  c


# --------------------------------find the index of number in sorted array from behind
def binarysearch2(arr, target):
    lo, hi = 0, len(arr) - 1
    while (hi >= lo):
        mid = (hi + lo) // 2
        # print(arr[mid],arr[mid-1],mid)
        if arr[mid] == target:
            if not mid != len(arr) - 1:
                return mid
            else:
                if arr[mid + 1] != target:
                    return mid
                else:
                    lo += 1
            continue
        if arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1


def nge(arr, n):
    stack, ans = [], []
    for i in reversed(range(n)):
        if not len(stack) == 0:
            while (len(stack) > 0):
                if stack[-1][0] < arr[i]:
                    stack.pop()
                else:
                    break
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
        else:
            ans.append(-1)
        stack.append([arr[i], i])
    ans.reverse()
    return  ans


def nse(arr,n):
    stack, ans=[], []
    for i in reversed(range(n)):
        if not len(stack)==0:
            while(len(stack)>0):
                if stack[-1][0] > arr[i]:
                    stack.pop()
                else:
                    break
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
        else:
            ans.append(-1)
        stack.append([arr[i],i])
    ans.reverse()
    return  ans


def alperm(nums, path, result):
    if not nums:
        result.add(tuple(path))
        return
    for i in range(0, len(nums)):
        alperm(nums[0:i]+nums[i + 1:], path+[nums[i]], result)
    return  result


def minsum(arr, n, m, res, l):
    if not (n == 1 and m == 1):
        if n != 1:
            p = res + arr[n - 1][m - 1]
            minsum(arr, n - 1, m, p, l)
        if m != 1:
            p = res + arr[n - 1][m - 1]
            minsum(arr, n, m - 1, p, l)
    else:
        res += arr[0][0]
        l.append(res)
    return  min(l)



def catalan(n):
    if (n == 0 or n == 1):
        return 1
    catalan=[0]*(n + 1)
    catalan[0]=1
    catalan[1]=1
    for i in range(2, n + 1):
        for j in range(0, i):
            catalan[i] += catalan[i - j - 1] * catalan[j]
    return  catalan[n]


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def leftViewUtil(root, level, max1):
    if root is None:
        return
    if max1[0]<level:
        print(root.data)
        max1[0]=level
    leftViewUtil(root.left, level + 1, max1)
    leftViewUtil(root.right,level+1,max1)
def leftView(root):
    max1 =[0]
    leftViewUtil(root, 1, max1)
root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)
#root.left.left.right=Node(15)
max1=-1
leftView(root)
"""


def find_shortest_path(graph, start, end, path):
    path=path+[start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest=None
    for node in graph[start]:
        if  node not  in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if  not  shortest or  len(newpath) < len(shortest):
                    shortest = newpath
    return  shortest


"""
def BFS(adj,src,dist,paths,n):
    visited=[False]*n
    dist[src]=0
    paths[0]=1
    q=[src]
    visited[src]=True
    while(q):
        p=q.pop(0)
        for j in adj[p]:
            if not visited[j]:
                q.append(j)
                visited[j]=True
            if dist[j]>dist[p]+1:
                dist[j] = dist[p]+1
                paths[j] = paths[p]
            elif dist[j]==dist[p]+1:
                paths[j] +=paths[p]
    return paths

"""
#--------------------millar rabin test
def test(n, d):
    a=random.randint(1, n-2)
    p=pow(a, d, n)
    if 1 == p or p==n-1:
        return True
    while (d!=n-1):
        d *= 2
        p = pow(p, 2, n)
        if p == n - 1:
            return True
    return  False


def isprime(n):
    if 1 == n:
        return False
    if 2 == n:
        return True
    if 3 == n:
        return True
    d=n-1
    while (d % 2 == 0):
        d //= 2
    for i in range(0, 5):
        if  test(n, d) == False:
            return False
    return  True


# -------------------------------sparse table
"""
p=20
def funnahi(dp,arr,n):
    for i in range(n):
        dp[i][0]=arr[i]
    for j in range(1,p):
        for i in range(n-(2**j)+1):
            dp[i][j] = min(dp[i][j-1],dp[i+2**(j-1)][j-1])
def main():
    n= inpu()
    arr=lis()
    q=inpu()
    dp = [[float("inf")] *(p) for i in range(n)]
    funnahi(dp,arr,n)
    for __ in range(q):
        l,r=sep()
        if l==r:
            print(arr[l])
            continue
        s=(r-l+1)
        s=int(math.log2(s))
        print(min(dp[l][s],dp[r-2**(s)+1][s]))
if __name__ == '__main__':
    main()
"""


def muin(a, m):
    x, y, mo=1, 0, m
    if 1 == m:
        return 0
    while (m>0):
        x, y = y, x - (a // m) * y
        a, m = m, a % m
    if not x < 0:
        return x
    else:
        return mo + x


def good(l, c):
    ch=chr(c)
    if 1 == len(l):
        return (1 if ch != l[0] else 0)
    k=len(l)//2
    lm, rm = k - l[:k].count(ch) + good(l[k:], c + 1), k - l[k:].count(ch) + good(l[:k], c + 1)
    return  (min(lm, rm))


def facto(fact):
    fact[0], fact[1]=1, 1
    for i in range(2, 10 ** 5 + 1):
        fact[i]=(fact[i - 1] * i)%M


def comb(n, r, fact):
    return  (fact[n]*pow(fact[r] * fact[n - r], M-2, M))%M


def numberToBase(n, b):
    if 0 == n:
        return 0
    digits=list()
    while n:
        digits.append((n % b))
        n //= b
    return  sum(digits)
"""
import kotlin.math.max 
import kotlin.math.min

private fun readLn() = readLine()!! 
private fun readInt() = readLn().toInt() 
private fun readLong() = readLn().toLong() 
private fun readDouble() = readLn().toDouble() 
private fun readStrings() = readLn().split(" ") 
private fun readInts() = readStrings().map { it.toInt() } 
private fun readLongs() = readStrings().map { it.toLong() } 
private fun readDoubles() = readStrings().map { it.toDouble() } 

fun main(args: Array<String>) {
}
"""
def main():
    tt=1
    tt=inpu()
    for _ in range(0, tt):
        n=inpu()
        a=lis()
        b=lis()
        for i in range(0, n):
            a[i] = [a[i],i]
            b[i] = [b[i],i]
        a.sort()
        b.sort()
        d=defaultdict(list)
        for i in range(0, n-1):
            d[a[i][1]].append(a[i+1][1])
            d[b[i][1]].append(b[i+1][1])
        visited=[False]*(n)

        def dfs(curr):
            visited[curr] = True
            for  i in  d[curr]:
                if  not  visited[i]:
                    dfs(i)
        dfs(a[-1][1])
        ans=""
        for i in range(0, len(visited)):
            if not visited[i]==True:
                ans+="0"
            else:
                ans+="1"
        print(ans)
if __name__ == '__main__':
    threading.stack_size(2 * 10 ** 8)
    threading.Thread(target=main).start()