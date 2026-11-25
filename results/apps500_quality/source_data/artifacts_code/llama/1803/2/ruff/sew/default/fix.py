import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    shots = []
    for  _ in  range(m):
        shot = list(map(int, sys.stdin.readline().strip().split()))
        shots.append((shot[0], shot[1] - 1))

    wires=[list() for _ in range(n)]

    for  i in  range(n):
        wires[i].extend([0] * a[i])

    for  shot in  shots:
        wire_num, pos = shot
        wire_num = wire_num - 1
        pos = pos - 1
        birds = wires[wire_num].pop(pos)
        if  wire_num>0:
            wires[wire_num - 1].append(birds)
        if  wire_num<n-1:
            wires[1 + wire_num].append(birds)

    for  i in  range(n):
        print(len(wires[i]))

if __name__=="__main__":
    main()
