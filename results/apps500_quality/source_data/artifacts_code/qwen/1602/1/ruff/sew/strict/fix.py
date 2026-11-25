import sys


def f(x, y):
    return (x | y) - y

def max_array_value(arr):
    n = len(arr)
    arr.sort(reverse=True)
    return arr

def main():
    input = sys.stdin.read
    data = input().split()
    n, arr = int(data[0]), list(map(int, data[1:]))
    result = max_array_value(arr)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
