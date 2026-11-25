import sys

def  find_xy(r):
    for  x in  range(1, 1 + int(r**0.5)):
        if (r - x**2 - x) % (2 * x + 1) == 0:
            y=(r-pow(x, 2)-x)//(1 + 2 * x)
            if y > 0:
                return (x, y)
    return  "NO"


if  __name__ == "__main__":
    r = int(sys.stdin.read().strip())
    print(find_xy(r))