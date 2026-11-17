# -*- coding: UTF-8 -*-
t, inputdata = int(input()), []
for  i in  range(t):
    input()
    inputdata.append(input().split(" "))
    for  j in  range(0, len(inputdata[i])):
        inputdata[i][j]=int(inputdata[i][j])
for  i in  range(t):
    res, l = 0, len(inputdata[i])
    ost = sum(inputdata[i], 0) % l
    while(ost>0):
        ost -= l;
        res = res + 1
    print(res)
        
    