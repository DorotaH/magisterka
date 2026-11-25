n = int(input())

def is_triangle(a, b, c):
    return  a+b>c and  a+c>b and  b+c>a

count = 0
for  a in  range(1, n + 1):
    for  b in  range(a, n + 1):
        for c in range(b, n + 1):
            if  is_triangle(a, b, c) and  0 == a ^ b ^ c:
                count = count + 1

print(count)