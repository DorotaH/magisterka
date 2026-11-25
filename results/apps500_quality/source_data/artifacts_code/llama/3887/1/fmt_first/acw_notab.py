import sys


def check_rebus(rebus):
    numbers = rebus.split()
    operations = ["+", "-"]
    n = int(numbers[-1])

    result = sum(
        1 if num == "?" else int(num) for i, num in enumerate(numbers[:-1])
    )
    for i, op in enumerate(operations):
        if op == "+":
            result += i + 1
        else:
            result -= i + 1

    return result == n


def replace_rebus(rebus):
    numbers = rebus.split()
    operations = ["+", "-"]
    n = int(numbers[-1])

    result = 0
    res = ""
    for i, num in enumerate(numbers[:-1]):
        if num == "?":
            result += 1 if numbers[i - 1] == "?" else int(numbers[i - 1])
            res += str(result) + " "
            result = 0
        else:
            res += " " + num

    for i, op in enumerate(operations):
        res += str(n - i) + " "
    return numbers[-1] + res


def main():
    rebus = sys.stdin.readline().strip()
    if check_rebus(rebus):
        print("Possible")
        print(replace_rebus(rebus))
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
