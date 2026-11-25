def main():
    n = int(input())
    strings = [input() for _ in range(n)]
    # Sort the list of strings
    strings.sort()

    # Concatenate the sorted strings
    result = "".join(strings)

    print(result)


if __name__ == "__main__":
    main()
