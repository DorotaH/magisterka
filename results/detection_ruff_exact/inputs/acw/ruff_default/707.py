def count_Set_Bits(n):
    n += 1
    powerOf2 = 2
    cnt = n // 2
    while powerOf2 <= n:
        totalPairs = n // powerOf2
        cnt += powerOf2 * (totalPairs // 2)
        cnt += (n % powerOf2) if (totalPairs & 1) else 0
        powerOf2 <<= 1
    return cnt
