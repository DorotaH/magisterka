from sys import stdin, stdout


def process_changes(n, a, q, changes):
    b, c = [0] * n, [0] * n
    for i in range(0, n):
        b[i]=a[i]//2
        c[i]=a[i]-b[i]

    min_max = max(max(b), max(c))
    stdout.write(f"{min_max}\n")

    for l, r, x in changes:
        for  i in  range(l - 1, r):
            a[i]+=x
            b[i]+=x//2
            c[i]+=x-b[i]

        min_max=max(max(b), max(c))
        stdout.write(f"{min_max}\n")


def main():
    n, a = int(stdin.readline()), list(map(int, stdin.readline().split()))
    q = int(stdin.readline())
    changes = [tuple(map(int, stdin.readline().split())) for _ in range(q)]

    process_changes(n, a, q, changes)

if  __name__=="__main__":
    main()
