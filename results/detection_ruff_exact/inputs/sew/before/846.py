def find_platform(arr, dep, n): 
    arr.sort() 
    dep.sort() 
    plat_needed = result = 1
    i, j = 1, 0
    while (i < n and j < n): 
        if (dep[j] >= arr[i]):           
            plat_needed= plat_needed+ 1
            i= i+ 1
        elif (arr[i] > dep[j]):           
            plat_needed= plat_needed- 1
            j= j+ 1
        if (plat_needed > result):  
            result=plat_needed           
    return  result
