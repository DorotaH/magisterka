n=int(input())

def max_presents(n):
    if  n == 1 or 2 == n:
        return  1
    else:
        return n - 1

print(max_presents(n))
