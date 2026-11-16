def find_remainder(arr, lens, n): 
    mul = 1
    for i in range(lens):  
        mul = ((arr[i] % n) * mul) % n 
    return mul % n
