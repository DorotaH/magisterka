n = input()
n = int(n)
if n <=2:
    print(-1)
elif 0 ==n%2:
    for row in range(n):
        if 0 ==row:
            for  i in  range(0, n):
                if i ==0:    
                    print(1+i,end = " ")
                elif i==n-1:
                    print(1+i)
                else: 
                    print(i+1,end = " ")   
        elif row ==n-1:
            for  i in  range(n):
                if not i==n-1:
                    print(n+(n-1)*(n-2)+(n-3)-i+2,end = " ")
                else: 
                    print(n*n-1)
        elif row ==n-2:
            for  i in  range(n):
                if i ==0:
                    print((n*n) - n + 2 + row,end = " ")
                elif i <n - 1: 
                    print(n + ((n-1)*(row-1)) + i,end = " ")
                else:
                    print(n + ((n-1)*(row-1)) + n - 1)
        elif row%2 ==1:
            for  i in  range(n):
                if i ==0:
                    print((n*n) - n + 2 + row - 1,end = " ")
                elif i <n - 1: 
                    print(n + ((n-1)*(row-1)) + n - i,end = " ")
                else:
                    print(n + ((n-1)*(row-1)) + 1)
        elif row%2 ==0:
            for  i in  range(n):
                if i ==0:
                    print((n*n) - n + 2 + row - 1,end = " ")
                elif i <n - 1: 
                    print(n + ((n-1)*(row-1)) + i,end = " ")
                else:
                    print(n + ((n-1)*(row-1)) + n - 1)
elif 1 ==n%2:
    for row in range(n):
        if 0 ==row:
            for  i in  range(0, n):
                if i ==0:    
                    print(1+i,end = " ")
                elif i==n-1:
                    print((n*n)-n+row+1)
                else: 
                    print(i+1,end = " ")   
        elif row ==n-1:
            for  i in  range(n):
                if i==0:
                    print((n*n) - 1,end = " ")
                elif i ==n - 1:
                    print(((n-1)*(n-1)) + i)
                else: 
                    print(((n-1)*(n-1)) + i,end = " ")
        elif row ==n-2:
            for  i in  range(n):
                if i ==0:
                    print(((n-1)*row) + n - i - 1,end = " ")
                elif i <n - 1: 
                    print(((n-1)*row) + n - i - 1,end = " ")
                else:
                    print(n * n)
        elif row%2 ==1:
            for  i in  range(n):
                if i ==0:
                    print(((n-1)*row) + n - i - 1,end = " ")
                elif i <n - 1: 
                    print(((n-1)*row) + n - i - 1,end = " ")
                else:
                    print((n*n) - n + row + 1)
        elif row%2 ==0:
            for  i in  range(n):
                if i ==0:
                    print(((n-1)*row) + i + 1,end = " ")
                elif i <n - 1: 
                    print(((n-1)*row) + i + 1,end = " ")
                else:
                    print((n*n) - n + row + 1)