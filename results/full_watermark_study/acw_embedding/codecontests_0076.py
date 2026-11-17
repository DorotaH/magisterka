
def naiveSolve():
    
    
    
    return



def solve():
    
    
    
    return

class SegmentTree():
    def __init__(self,arr,combinerFunction,isCommutative=True): # isCommutative means f(a,b)==f(b,a)
        self.n=len(arr)
        def cmb(a,b):
            if a==None: return b
            return a if b==None else combinerFunction(a,b)

        self.cmb=cmb
        self.sz=self.n if isCommutative else pow(2,((self.n-1).bit_length())) # commutative needs power of 2 size
        self.t=[None]*(2*self.sz) # use None as initial value
        for i in range(self.n): self.t[i+self.sz]=arr[i]
        for i in range(self.sz-1,0,-1): self.pull(i)
    def pull(self,p):
        self.t[p]=self.cmb(self.t[2*p],self.t[2*p+1])
    def update(self,idx,val): # set val at idx
        idx+=self.sz
        self.t[idx]=val
        idx//=2
        while idx>0:
            self.pull(idx)
            idx//=2
    def query(self,l,r): # aggregated value in [l,r] inclusive
        l+=self.sz; r+=self.sz+1
        a=b=None
        while l<r:
            if l%2==1: a=self.cmb(a,self.t[l]); l+=1
            if r%2==1: r-=1; b=self.cmb(self.t[r],b)
            l//=2; r//=2
        return self.cmb(a,b)
        

def add(length):
    return (length*(length+1))//2
# (leftVal,rightVal,leftLen,rightLen,cntsWithin,False)
def combiner(a,b):
    alv,arv,all,arl,ac,ab=a
    blv,brv,bll,brl,bc,bb=b
    clv,crv,cll,crl,cc,cb=alv,brv,all,brl,ac+bc,ab or bb
    if ab and bb:
        cc += add(arl+bll) if arv<=blv else add(arl)+add(bll)
    elif ab:
        if arv<=blv: crl+=arl
        else: cc+=add(arl)
    elif bb:
        if arv<=blv: cll+=bll
        else: cc+=add(bll)
    elif arv<=blv: cll=crl=all+bll
    else: cb=True
    return (clv,crv,cll,crl,cc,cb)

def main():
    
    n,q=readIntArr()
    arr2=readIntArr()
    # (leftVal,rightVal,leftLen,rightLen,cntsWithin,broken)
    arr=[(x,x,1,1,0,False) for x in arr2]
    st=SegmentTree(arr,combiner,False)

    allans=[]
    for _ in range(q):
        t,u,v=readIntArr()
        if t==1: # update
            u-=1
            st.update(u,(v,v,1,1,0,False))
        else: # query
            lv,rv,ll,rl,c,b=st.query(u-1,v-1)
            ans = c+add(ll)+add(rl) if b else add(ll)
            allans.append(ans)
    multiLineArrayPrint(allans)

    # TEST REGION

    # from random import randint as ri
    # n=7
    # # arr2=[ri(1,2) for _ in range(n)]
    # arr2=[1, 2, 1, 1, 2, 1, 2]
    # arr=[(x,x,1,1,0,False) for x in arr2]
    # st=SegmentTree(arr,combiner,False)

    # left,right=0,n-1

    # lv,rv,ll,rl,c,b=st.query(0,n-1)
    # if b: ans=c+add(ll)+add(rl)
    # else: ans=add(ll)

    # ans2=0
    # for l in range(left,right+1):
    #     prev=-inf
    #     for r in range(l,right+1):
    #         if arr2[r]>=prev:
    #             ans2+=1
    #             prev=arr2[r]
    #         else:
    #             break
    # if ans!=ans2:
    #     print('arr2:{} ans:{} ans2:{}'.format(arr2,ans,ans2))
    #     print('lv:{} rv:{} ll:{} rl:{} c:{} b:{}'.format(lv,rv,ll,rl,c,b))
    #     print(st.t[2])
    #     print(st.t[3])
    #     print(st.t[1])

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
 
def queryInteractive(x):
    print('{}'.format(x))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ans):
    print('! {}'.format(ans))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()