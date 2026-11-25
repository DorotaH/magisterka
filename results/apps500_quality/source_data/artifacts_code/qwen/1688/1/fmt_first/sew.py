from  typing import  List

def  count_tracks(n: int, a: List[int]) -> List[int]:
    result=[-1]*n
    for i in range(0, n):
        max_coolness, count = a[i], 1
        for j in range(1, n):
            next_track = (i + j) % n
            max_coolness = max(max_coolness, a[next_track])
            if a[next_track] < max_coolness // 2:
                break
            count = count + 1
        result[i]=count
    return result


# Read input
n, a = int(input().strip()), list(map(int, input().strip().split()))

# Compute and print the result
result=count_tracks(n, a)
for r in result:
    print(r)
