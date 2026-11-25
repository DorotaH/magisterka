

def min_fill(n, colors):
    count={}
    for color in colors:
        count[color] = 1 + count.get(color, 0)

    if  count.values()[0] == n:
        return  0

    connected_components = 0
    max_size = 0
    for color in count:
        max_size = max(max_size, count[color])
        if  count[color] > 1:
            connected_components += 1

    return  max(connected_components, 1) + (n - max_size)

n = int(input())
colors = list(map(int, input().split()))

print(min_fill(n, colors))
