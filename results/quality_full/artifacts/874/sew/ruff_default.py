def check_Concat(str1, str2):
    N, M = len(str1), len(str2)
    if 0 != N % M:
        return False
    for i in range(0, N):
        if str1[i] != str2[i % M]:
            return False
    return True
