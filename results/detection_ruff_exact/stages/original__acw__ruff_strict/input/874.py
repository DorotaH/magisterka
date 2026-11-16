def check_Concat(str1, str2):
    N = len(str1)
    M = len(str2)
    return False if N % M != 0 else all(str1[i] == str2[i % M] for i in range(N))
