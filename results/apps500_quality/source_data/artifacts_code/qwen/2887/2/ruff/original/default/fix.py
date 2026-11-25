import sys


def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    V = list(map(int, data[1:N+1]))
    T = list(map(int, data[N+1:2*N+1]))
    
    evaporated = []
    for i in range(N):
        if V[i] > T[i]:
            evaporated.append(V[i] - T[i])
        else:
            evaporated.append(0)
    
    print(' '.join(map(str, evaporated)))

if __name__ == "__main__":
    main()
