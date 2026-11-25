import sys

n = int(sys.stdin.readline())

index = 1
while True:
    str_num = str(index)
    if len(str_num) % 2 != 0:
        index += 1
        continue
    elif int(str_num) < n:
        index += 1
    else:
        break

str_num = str(index)
n_str = str(n)
n_len = len(n_str)

palindrome = str_num
while len(palindrome) != 2 * n_len:
    palindrome = str_num + str_num[::-1]

print(int(palindrome[int(n_len - 1):]))
