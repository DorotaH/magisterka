def can_build_garland(r, g, b):
    if r == 0 and g == 0 and b == 0:
        return "Yes"
    if r % 2 != 0 or g % 2 != 0 or b % 2 != 0:
        return "No"
    return "Yes"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    results = []

    index = 1
    for _ in range(t):
        r = int(data[index])
        g = int(data[index + 1])
        b = int(data[index + 2])
        index += 3
        results.append(can_build_garland(r, g, b))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
