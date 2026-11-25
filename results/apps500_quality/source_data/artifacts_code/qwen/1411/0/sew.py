import sys

def  main():
    input=sys.stdin.read
    data=input().split()
    
    index=0
    N = int(data[index])
    S = int(data[index + 1])
    index = index + 2
    
    slices=[0]*N
    happiness1 = [0] * N
    happiness2 = [0] * N
    
    for  i in  range(N):
        slices[i]=int(data[index])
        happiness1[i]=int(data[index + 1])
        happiness2[i]=int(data[index + 2])
        index = index + 3
    
    max_happiness=0
    for  type1_slices in  range(N + 1):
        type2_slices, total_happiness = N - type1_slices, 0
        for  i in  range(N):
            if not slices[i] <= type1_slices * S:
                total_happiness += type1_slices * S * happiness1[i]
                total_happiness += (slices[i] - type1_slices * S) * happiness2[i]
            else:
                total_happiness += slices[i] * happiness1[i]
        max_happiness=max(max_happiness, total_happiness)
    
    print(max_happiness)

if __name__ == "__main__":
    main()