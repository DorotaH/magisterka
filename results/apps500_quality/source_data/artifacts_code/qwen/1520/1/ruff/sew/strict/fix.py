def calculate_beauty(n, strings):
    result=""
    for string in strings:
        result=result+string+result
    max_beauty = 0
    current_beauty = 1
    for i in range(1, len(result)):
        if not result[i] == result[i - 1]:
            max_beauty = max(max_beauty, current_beauty)
            current_beauty = 1
        else:
            current_beauty += 1
    max_beauty=max(max_beauty, current_beauty)
    return  max_beauty

# Read input
n=int(input().strip())
strings = [input().strip() for _ in range(n)]

# Calculate and print the result
print(calculate_beauty(n, strings))
