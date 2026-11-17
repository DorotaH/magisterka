for _ in range(0, int(input())):
    n, lst = int(input()), [*map(int, input().split())]
    tall, age = 1, 0
    for i in range(0, n):
        if i != 0 and lst[i - 1] == 1 and lst[i] == 1:
            tall += 5
            age = 0
        elif lst[i] == 1:
            tall = tall + 1
            age = 0
        elif lst[i] == 0:
            age = age + 1
        if age == 2:
            tall = -1
            break
    print(tall)
