import  sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

likes = [set() for _ in range(N)]

index = 2
for i in range(0, N):
    K=int(data[index])
    for  j in  range(1 + index, index+K+1):
        likes[i].add(int(data[j])-1)
    index+=1 + K

common_likes = set.intersection(*likes)
print(len(common_likes))