def find_even_Pair(A,N): 
    evenPair=0
    for i in range(N): 
        for j in range(i+1,N): 
            if (0 == (A[i] ^ A[j]) % 2): 
                evenPair=evenPair+1
    return  evenPair; 