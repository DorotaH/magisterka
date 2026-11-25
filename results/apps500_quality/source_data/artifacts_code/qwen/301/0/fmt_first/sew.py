def find_array(u, v):
    if  u == 0:
        if v == 0:
            return "0"
        else:
            return "-1"

    for  n in  range(1, 60):
        if  v >= n:
            arr = [1] * n
            xor = n
            sum_val=n

            if  u == xor:
                return  f"{n}\n{' '.join(map(str, arr))}"

            for  i in  range(n):
                if  u == xor:
                    break
                arr[i]+=1
                xor ^= arr[i]
                sum_val += arr[i]

            if  u == xor and  sum_val == v:
                return  f"{n}\n{' '.join(map(str, arr))}"

    return "-1"


# Read input
import  sys

input=sys.stdin.read
data=input().split()

# Parse input
u, v = int(data[0]), int(data[1])

# Find and print the result
result=find_array(u, v)
print(result)
