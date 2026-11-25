from collections import Counter

n = 24


def check_cube(cube):
    # Count the frequency of each color
    color_counts = Counter(cube[i] for i in range(n))

    # If all colors appear 4 times, it's possible to solve the cube
    return len(color_counts) == 4 and all(count == 4 for count in color_counts.values())


def main():
    cube = list(map(int, input().split()))
    if check_cube(cube):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
