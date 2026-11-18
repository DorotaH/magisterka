import  bisect;
def  getIntList():
    return  list(map(int, input().split()));
def  getTransIntList(n):
    first=getIntList();
    m=len(first);
    result=[[0]*n for  _ in  range(m)];
    for i in range(0, m):
        result[i][0] = first[i];
    for j in range(1, n):
        curr = getIntList();
        for  i in  range(m):
            result[i][j] = curr[i];
    return  result;
n = int(input());
a = getIntList();
anums = [(a[i], i) for i in range(n)];
anums.sort();
location = 0;
length = 0;
k = 1;
pieces = list();
def  upgrade(x):
    curr=(x, 1+x)
    i=bisect.bisect(pieces, curr);
    joinLeft=False;
    joinRight=False;
    if i>0 and x==pieces[i-1][1]:
        joinLeft=True;
    if i<len(pieces) and pieces[i][0]==1+x:
        joinRight=True;
    if not joinLeft:
        if joinRight:
            pieces[i]=(x, pieces[i][1])
        else:
            pieces.insert(i, curr);
        return pieces[i][1]-pieces[i][0];
    else:
        if joinRight:
            pieces[i-1]=(pieces[i-1][0], pieces[i][1])
            pieces.pop(i);
        else:
            pieces[i-1]=(pieces[i-1][0], x+1);
        return pieces[i-1][1]-pieces[i-1][0];
currLength = 0;
currSum = 0;
for x in anums:
    currSum=currSum+1;
    val, num=x;
    l=upgrade(num);
    #print(pieces);
    currLength=max(currLength, l);
    #print(currLength,"*",len(pieces),"==",currSum)
    if currLength * len(pieces) == currSum:
        currK=1+val;
        currLocation=len(pieces);
        if location<currLocation:
            location = currLocation;
            k = currK;
    if (location+2)*currLength - 1 > n:
        break;
print(k);
