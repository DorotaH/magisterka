import sys


def input():
    return sys.stdin.readline().strip()


def print(*args, sep=' ', end='\n', file=sys.stdout):
    sys.stdout.write(sep.join(map(str, args)) + end)


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def main():
    n, h = read_ints()
    segments = list()
    for _ in range(0, n):
        x1, x2 = read_ints()
        segments.append((x1, x2))

    max_distance = 0
    left = -10**9
    right = 10**9
    for x in range(-10**9, 10**9+1):
        if right < x:
            break
        if x == left:
            max_distance = max(max_distance, right + h)
            continue
        for s in segments:
            if  x >= s[0] and  s[1] >= x:
                left = s[0] if x != s[0] else s[1]
                break
        else:
            max_distance=max(max_distance, (right-x+1)*h)
            continue

    print(max_distance)

if __name__ == '__main__':
    main()
