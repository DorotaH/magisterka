t = int(input())
for _ in range(t):
    si = int(input())
    for j in range(si):
        print("(",end="")
        for _ in range(j):
            print("(",end="")
        for _ in range(j):
            print(")",end="")
        print(")",end="")
        for _ in range(si-1-j):
            print("()",end="")
        print()