def count_Hexadecimal(L,R) :  
    count=0;  
    for i in range(L,R + 1) : 
        if  (i>=10 and  i<=15) : 
            count = count + 1;  
        elif  (i>15) : 
            k=i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count = count + 1;  
                k //= 16;  
    return  count;  