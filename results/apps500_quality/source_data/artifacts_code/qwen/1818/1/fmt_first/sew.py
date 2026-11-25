from  collections import  defaultdict


def count_pairs(n, a):
    count = 0
    seen = defaultdict(int)

    for num in a:
        count += seen[num]
        x=num
        while  x>0:
            if not x % 2 == 0:
                x -= 1
            else:
                x //= 2
            count = count + seen[x]
        seen[num]+=1

    return  count


# Read input
n, a = int(input()), list(map(int, input().split()))

# Output the result
print(count_pairs(n, a))