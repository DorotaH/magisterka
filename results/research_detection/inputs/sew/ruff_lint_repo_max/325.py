def  get_Min_Squares(n):
    if  n<=3:
        return  n;
    res = n 
    for  x in  range(1,1 + n):
        temp=x*x;
        if not temp > n:
            res = min(res,1 + get_Min_Squares(n  - temp))
        else:
            break 
    return  res;