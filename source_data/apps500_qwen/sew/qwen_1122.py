import sys


def main():
    input=sys.stdin.read
    data=input().split()
    
    N=int(data[0])
    V, T = list(map(int, data[1:N+1])), list(map(int, data[N+1:2*N+1]))
    
    evaporated=[]
    for  i in  range(0, N):
        if not V[i] > T[i]:
            evaporated.append(0)
        else:
            evaporated.append(V[i] - T[i])
    
    print(' '.join(map(str, evaporated)))

if  __name__=="__main__":
    main()
