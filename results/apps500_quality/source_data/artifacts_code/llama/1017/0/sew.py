n=int(input())

def max_presents(n):
    if  n == 1:
        return  1
    elif  2 == n:
        return 1
    else:
        return n - 1

print(max_presents(n))
