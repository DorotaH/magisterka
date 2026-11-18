import  sys
n = 0;
inp = [];
tree = [];#stores the index of min in range(i,j)

def  build(node,i,j):
    if(i>j):
        return None;
    if(i==j):
        tree[node]=int(i);
        return None;
    mid = int( (i + j) / 2 );

    build(2*node,i,mid)
    build(1+2*node,1+mid,j)
    if( inp[ tree[2*node] ] < inp[ tree[2*node+1] ] ):
        tree[node]= tree[2*node];
    else:
        tree[node]=tree[2*node+1]

def  RMQ(node,i,j,l,r):#return  index of minimum in range i,j #r,l is current range
    if( (l>=i) and  (j>=r) ):
        return tree[node];

    if( (i>r) or  (l>j) ):
        return n;

    mid = int((l + r) / 2);

    a = RMQ(2*node,   i, j, l ,    mid);#     j,l,mid);
    b = RMQ(1+2*node, i, j, 1+mid, r);

    if( inp[a] < inp[b]):
        return a;
    else:
        return b;

def  inputArray():
    A = str(input()).split();
    return list(map(int,A));

def  solve(a,b,ht):
    if(a>b):
        return 0;
    mn = RMQ(1,a,b,0,n - 1);
    op1=b-a+1
    op2=solve(a,mn-1 , inp[mn] ) + solve(mn+1,b, inp[mn] ) + inp[mn]-ht ;
    return min(op1,op2);


if( __name__=="__main__"):
    n = int( input() );
    inp = inputArray();
    inp.append(1000*1000*1000+10);
    
    sys.setrecursionlimit(10_000)
    #build RMQ array
    tree = [ int(n) for x in range(0, 4*n+10) ];
    build(1,0,n - 1);

    print(( solve(0,n - 1,0) ));
