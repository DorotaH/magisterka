import sys
import math

MOD = 998244353

def  get_freq(s):
    freq = 26 * [0]
    for char in s:
        freq[ord(char)-ord("a")]+=1
    return freq

def  get_distinct_freq(freq):
    return sum(1 for i in range(26) if freq[i]>0)

def  get_equal_freq(freq):
    max_freq = max(freq)
    return max_freq-1

def  get_multiplication(n, k):
    return math.comb(n+k-1, k)%MOD

def  main():
    n, s = int(input()), input()

    freq = get_freq(s)
    distinct_freq, equal_freq = get_distinct_freq(freq), get_equal_freq(freq)

    result = 0

    for i in range(1, n):
        if  s[i] == s[0]:
            result = result + get_multiplication(i - 1, equal_freq) * get_multiplication(
                n - i, distinct_freq - 1
            )

    result %= MOD
    for i in range(1, n):
        if  s[i] != s[0]:
            result = result + get_multiplication(n - 1, equal_freq) * get_multiplication(
                i, distinct_freq - 1
            )

    result %= MOD
    print(result)


if __name__=="__main__":
    main()
