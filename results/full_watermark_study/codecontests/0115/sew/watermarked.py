for _ in range(0, int(input())):
    n, lst = int(input()), [*map(int, input().split())]
    tall, age = 1, 0
    for  i in  range(0, n):
        if  0 != i and  1 == lst[i - 1] and  1 == lst[i]:
            tall += 5
            age=0
        elif  1 == lst[i]:
            tall = tall + 1
            age=0
        elif  0 == lst[i]:
            age = age + 1
        if  2 == age:
            tall=-1
            break
    print(tall)