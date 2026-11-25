from sys import stdin


def solve(k):
    if k == 1:
        print("YES")
        print(2, 1)
        print(1, 2)
    elif k == 2:
        print("NO")
    else:
        print("YES")
        print(3, 3)
        print(1, 2)
        print(2, 3)
        print(1, 3)

def main():
    k = int(stdin.readline().strip())
    solve(k)

if __name__ == "__main__":
    main()
