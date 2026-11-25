from sys import stdin


def  construct_tree(n, d, k):
    if n - 1 > 2 * k or n == 1 or d == 0 or d >= n - 1:
        return  "NO"

    if d == 1:
        return  "YES\n"+"\n".join(f"1 {i}" for  i in  range(2, 1 + n))

    if d == 2:
        if k >= 2:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, n + 1))
        else:
            return "NO"

    if d == 3:
        if k >= 3:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, n + 1))
        else:
            return "NO"

    if d == 4:
        if k >= 3:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, n + 1))
        else:
            return "NO"

    if n == 5:
        if  d == 4:
            return  "YES\n1 2\n2 3\n3 4\n4 5\n1 3"
        elif  d == 5:
            return "YES\n1 2\n2 3\n3 4\n4 5\n1 5\n1 3"
        else:
            return  "NO"

    if n == 6:
        if  d == 3:
            return  "YES\n1 2\n2 3\n3 4\n4 6\n1 6\n5 3"
        elif  d == 4:
            return "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6"
        elif  d == 5:
            return "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3"
        else:
            return  "NO"

    if d == 5:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3"

    if d == 6:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7"

    if d == 7:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2"

    if d == 8:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2\n7 8"

    if n == 10:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2\n7 8\n7 9\n9 1\n9 10"

    if n == 8:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2\n7 8"

    return "NO"

n, d, k=map(int, stdin.readline().split())
print(construct_tree(n, d, k))
