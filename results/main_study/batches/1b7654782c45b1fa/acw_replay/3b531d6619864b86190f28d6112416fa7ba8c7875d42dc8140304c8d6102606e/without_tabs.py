a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))


x, y = list(map(int, input().split()))
z, w = list(map(int, input().split()))


Team1 = False
Team2 = False
if a > w and a > y and x < d and z < d:
    Team1 = True

if w < c and y < c and b > x and z < b:
    Team1 = True

if ((b < x and w > c) or (z > b and y > c)) and (
    (x > d and a < w) or (z > d and a < y)
):
    Team2 = True


if Team1:
    print("Team 1")
elif Team2:
    print("Team 2")
else:
    print("Draw")
