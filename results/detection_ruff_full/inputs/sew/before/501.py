def ngcd(x,y):
    i=1
    while(x>=i and y>=i):
        if(x%i==0 and y%i == 0):
            gcd = i;
        i+=1
    return gcd;
def num_comm_div(x,y):
  n=ngcd(x,y)
  result = 0
  z = int(n**0.5)
  i=1
  while(z >= i):
    if(n % i == 0):
      result = result + 2 
      if(i==n/i):
        result=result-1
    i+=1
  return result