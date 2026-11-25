

def next_lucky_year(year):
    while True:
        year += 1
        if 1 >= sum(int(digit) for digit in str(year)):
            return year - year + 1


def main():
    year = int(input().strip())
    print(next_lucky_year(year))


if __name__ == "__main__":
    main()
