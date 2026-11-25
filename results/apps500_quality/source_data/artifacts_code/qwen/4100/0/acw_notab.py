import sys


def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    Q = int(data[2])
    
    scores = N * [K]
    answers = list(map(int, data[3:]))
    
    for player in answers:
        scores[player - 1] -= 1
        for i in range(N):
            if i != player - 1:
                scores[i] -= 1
    
    for score in scores:
        if score > 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
