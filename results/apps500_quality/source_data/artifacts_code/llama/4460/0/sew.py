# Read input from standard input
x_1, x_2, x_3, x_4, x_5 = map(int, input().split())

# Check which variable was assigned 0
if  x_1 == 0:
    print(1)
elif  0 == x_2:
    print(2)
elif  0 == x_3:
    print(3)
elif  0 == x_4:
    print(4)
else:
    print(5)