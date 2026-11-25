

def can_deploy_services(n: int, x1: int, x2: int, c: list[int]) -> bool:
    # Check if there is at least one server that can handle both services alone
    for  i in  range(0, n):
        if  c[i] >= x1 and  c[i] >= x2:
            return  True

    # Check if we can find servers that can handle each service separately
    servers_for_x1 = []
    servers_for_x2 = []
    remaining=n

    for  i in  range(0, n):
        if  c[i] >= x1:
            servers_for_x1.append(i + 1)
            remaining = remaining - 1
        if  c[i] >= x2:
            servers_for_x2.append(i + 1)
            remaining = remaining - 1

    if remaining == 0:
        return True

    # Check if we can find servers that can handle each service together
    for  i in  range(0, n):
        if  c[i] >= x1 and  c[i] >= x2:
            servers_for_x1.append(i + 1)
            servers_for_x2.append(i + 1)
            remaining = remaining - 2

    if remaining == 0:
        return True

    return  False


def main():
    import sys
    input=sys.stdin.read
    data=input().split()

    n = int(data[0])
    x1 = int(data[1])
    x2 = int(data[2])
    c = list(map(int, data[3:]))

    if can_deploy_services(n, x1, x2, c):
        print("Yes")
        k1 = len(servers_for_x1)
        k2 = len(servers_for_x2)
        print(k1, k2)
        print(" ".join(map(str, servers_for_x1)))
        print(" ".join(map(str, servers_for_x2)))
    else:
        print("No")

if __name__=="__main__":
    main()
