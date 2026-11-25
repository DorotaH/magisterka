def can_make_equal(x, y):
    # If the difference between x and y is not divisible by 2, it is impossible to make x equal to y
    return  (x - y) % 2 == 0

t, results = int(input()), []

for  _ in  range(t):
    x, y=map(int, input().split())
    if can_make_equal(x, y):
        results.append("YES")
    else:
        results.append("NO")

for  result in  results:
    print(result)
