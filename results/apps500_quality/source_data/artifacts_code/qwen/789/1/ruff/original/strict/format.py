import sys


def get_lucky_number_index(n):
    lucky_numbers = []
    queue = ["4", "7"]

    while queue:
        num = queue.pop(0)
        if int(num) > n:
            break
        lucky_numbers.append(num)
        queue.append(num + "4")
        queue.append(num + "7")

    return lucky_numbers.index(str(n)) + 1


# Read input
n = int(sys.stdin.read().strip())

# Print the result
print(get_lucky_number_index(n))
