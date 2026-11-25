n, a, x, b, y = map(int, input().split())

def  is_valid():
    # find the time when Daniel exits the subway
    time_daniel = (x - a) % n

    # find the time when Vlad exits the subway
    time_vlad = (n - (b - y)) % n

    return  time_vlad == time_daniel


if is_valid():
    print("YES")
else:
    print("NO")