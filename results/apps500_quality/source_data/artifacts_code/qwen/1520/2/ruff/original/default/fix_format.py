def calculate_beauty(n, strings):
    result = ""
    for s in strings:
        result += s

    max_beauty = 1
    current_beauty = 1

    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            current_beauty += 1
        else:
            max_beauty = max(max_beauty, current_beauty)
            current_beauty = 1

    max_beauty = max(max_beauty, current_beauty)
    return max_beauty


# Read input
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Calculate and print the beauty of the product
print(calculate_beauty(n, strings))
