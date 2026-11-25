def main():
    # Read input from standard input
    a = list(map(int, input().split()))

    # Calculate the result using the formula: max(a) % 3
    result = max(a) % 3

    # Print the result to standard output
    print(result)

if __name__ == "__main__":
    main()
