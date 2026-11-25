import sys


def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def can_be_equal(a, b):
    return gcd(a, b) == 1

def main():
    input = sys.stdin.read
    data = input().split()
    
    a1, b1 = int(data[0]), int(data[1])
    a2, b2 = int(data[2]), int(data[3])
    
    if can_be_equal(a1, b1) and can_be_equal(a2, b2):
        min_minutes = 1
        if a1 == a2 and b1 == b2:
            print(min_minutes)
            print(a1, b1)
            print(a2, b2)
            return
        elif a1 == a2:
            min_minutes = 1
            if b1 < b2:
                print(min_minutes)
                print(a1, b1 * 2)
                print(a2, b2 // 2)
            else:
                print(min_minutes)
                print(a1, b1 // 2)
                print(a2, b2 * 2)
        elif b1 == b2:
            min_minutes = 1
            if a1 < a2:
                print(min_minutes)
                print(a1 * 2, b1)
                print(a2 // 2, b2)
            else:
                print(min_minutes)
                print(a1 // 2, b1)
                print(a2 * 2, b2)
        else:
            min_minutes = 2
            if a1 < a2 and b1 < b2 or a1 < a2 and b1 > b2:
                print(min_minutes)
                print(a1 * 2, b1)
                print(a2 // 2, b2)
            elif a1 > a2 and b1 < b2:
                print(min_minutes)
                print(a1 // 2, b1)
                print(a2 * 2, b2)
            else:
                print(min_minutes)
                print(a1 // 2, b1)
                print(a2 * 2, b2)
    else:
        print(-1)

if __name__ == "__main__":
    main()
