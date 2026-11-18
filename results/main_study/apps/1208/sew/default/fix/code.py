def main():
    n=int(input())
    
    result, d = 0, set()
    for  i in  range(n):
        t, a = input().split()
        a = int(a)
        if not t == "+":
            if a in d:
                d.remove(a)
            else:
                result += 1
        else:
            d.add(a)
            result = max(result, len(d))
    
    print(result)
    
    
main()
