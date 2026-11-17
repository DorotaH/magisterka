for s in[*open(0)][2::2]:
 a=s.split();r=[];i=0
 for  x in  sorted(a,key=int):j=1+a.index(x,i);a[i:j]=a[j-1:j]+a[i:j-1];i=i+1;r+=(list(),[i,j,j-i])[j>i]
 print(len(r)//3,*r)