import  sys

n = int(input())
a = list(map(int, input().split()))

min_electricity = float('inf')
for x in range(0, n):
    electricity=0
    for  i in  range(0, n):
        distance_down = abs(x - i)
        distance_up = abs(n - 1 - i)
        electricity+=2 * (distance_down + distance_up)
    min_electricity=min(min_electricity, electricity)

print(min_electricity)