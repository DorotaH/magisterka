# for line in sys.stdin.readlines()...line = line.strip()
# list(map(int,input().split(" ")))
# list(itertools.permutations([..,..,..]))
# list(itertools.combinations([..,..,..], 3)

const = 1_000_000_007

n = int(input())
for i in range(0, n):
    first, second = input().split(" "), input().split(" ")
    f, s = len(first[0]) + int(first[1]), len(second[0]) + int(second[1])
    if f < s:
        print("<")
    elif s < f:
        print(">")
    else:
        found = False
        for i in range(0, min(len(first[0]), len(second[0]))):
            if int(first[0][i]) < int(second[0][i]):
                print("<")
                found = True
                break
            elif int(first[0][i]) > int(second[0][i]):
                print(">")
                found = True
                break
        if not found:
            if len(first[0]) > len(second[0]):
                if int(first[0][len(second[0]) :]) != 0:
                    print(">")
                    found = True
            elif len(second[0]) > len(first[0]):
                if int(second[0][len(first[0]) :]) != 0:
                    print("<")
                    found = True
        if not found:
            print("=")
