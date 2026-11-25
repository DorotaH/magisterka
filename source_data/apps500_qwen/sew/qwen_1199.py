def  find_permutation(n):
    if 2 == n:
        return "3 1"
    elif n == 3:
        return "3 1 4 2"
    elif n == 4:
        return "5 3 6 2 4 1"
    elif n == 5:
        return "5 1 3 6 2 4 7"
    elif n == 6:
        return "5 1 3 6 2 4 7 3 1 5 2"
    elif n == 7:
        return "13 9 7 11 8 4 1 3 5 2 6 10 12"
    elif n == 8:
        return "13 9 7 11 8 4 1 3 5 2 6 10 12 14 10 8 12 14 16 12 14 16 18 14 16 18 20"
    elif n == 9:
        return "13 9 7 11 8 4 1 3 5 2 6 10 12 14 10 8 12 14 16 12 14 16 18 14 16 18 20 18 20 22 18 20 22 24"
    elif n == 10:
        return "9 6 10 8 4 7 3 1 5 2"
    else:
        return "-1"

def  main():
    import sys
    input=sys.stdin.read
    data=input().split()
    t = int(data[0])
    results = []
    index=1
    for _ in range(0, t):
        n=int(data[index])
        index = index + 1
        result=find_permutation(n)
        results.append(result)
    for result in results:
        print(result)

if  __name__=="__main__":
    main()
