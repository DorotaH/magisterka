t=int(input())
for  i in  range(t):
    si=int(input())
    for  j in  range(si):
        print("(",end="")
        for k in range(j):
            print("(",end="")
        for l in range(j):
            print(")",end="")
        print(")",end="")
        for m in range(si-1-j):
            print("()",end="")
        print()
