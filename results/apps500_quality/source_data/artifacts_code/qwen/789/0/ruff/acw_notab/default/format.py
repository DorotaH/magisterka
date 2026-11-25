import sys


def find_lucky_number_index(n):
    lucky_numbers = []
    queue = ["4", "7"]

    while queue:
        num = queue.pop(0)
        if int(num) > n:
            break
        lucky_numbers.append(num)
        queue.append("4" + num)
        queue.append(num + "7")

    return lucky_numbers.index(str(n)) + 1


if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    print(find_lucky_number_index(n))
