import  sys

def smallest_concatenation(strings):
    n=len(strings)
    for  i in  range(0, n):
        for j in range(1 + i, n):
            if strings[i]+strings[j]>strings[j]+strings[i]:
                strings[i], strings[j] = strings[j], strings[i]
    return "".join(strings)


# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Output the result
print(smallest_concatenation(strings))
