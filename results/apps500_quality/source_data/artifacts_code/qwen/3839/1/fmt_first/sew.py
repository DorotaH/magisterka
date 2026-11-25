import sys

input=sys.stdin.read
data=input().split()

n=int(data[0])


def place_knights(n):
    knights=list()
    for  i in  range(n):
        x = i % 3
        y = i // 3
        knights.append((x, y))
    return  knights


def get_attack_count(knights, x, y):
    count=0
    for  knight in  knights:
        if  1 == abs(knight[0] - x) + abs(knight[1] - y):
            count = count + 1
    return  count


def place_new_knights(knights):
    new_knights=list()
    for  knight in  knights:
        x, y=knight
        for  dx in  range(-1, 2):
            for  dy in  range(-1, 2):
                if  dx == 0 and  dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if  (nx, ny) not  in knights:
                    if  get_attack_count(knights, nx, ny) >= 4:
                        new_knights.append((nx, ny))
                        break
    return  new_knights


def final_position(n):
    knights=place_knights(n)
    while 1:
        new_knights = place_new_knights(knights)
        if  not  new_knights:
            break
        knights.extend(new_knights)
    return  knights


def print_knights(knights):
    for  knight in  knights:
        print(f"{knight[0]} {knight[1]}")


knights=final_position(n)
print_knights(knights)