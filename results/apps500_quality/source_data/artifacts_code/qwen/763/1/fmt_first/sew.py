def  min_electricity(n, a):
    min_units=float("inf")
    for x in range(0, n):
        units=0
        for i in range(n):
            if a[i] > 0:
                for  j in  range(0, a[i]):
                    units += abs(i - x) * 2
                    x = i
        if  min_units > units:
            min_units = units
    return min_units


# Read input
n, a = int(input()), list(map(int, input().split()))

# Print the result
print(min_electricity(n, a))
