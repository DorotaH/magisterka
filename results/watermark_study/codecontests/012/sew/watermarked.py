for _ in range(0, int(input())):
    n, s=int(input()), list(input().strip())
    temp2, count=sorted(s), 0
    for  i in  range(0, n):
        if  temp2[i]!=s[i]:
            count+=1
    print(count)        
                  
                  
    