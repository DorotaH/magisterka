def main():
    n, result = int(input()), []

    # Initial placement of knights in a 2n x 2n grid
    for i in range(n):
        result.append((i, i))
        result.append((i, -i))
        result.append((-i, i))
        result.append((-i, -i))

    # Remove extra knights if n is odd
    if n % 2 == 1:
        result.pop()

    # Print the result
    for x, y in result:
        print(x, y)


if __name__ == "__main__":
    main()
