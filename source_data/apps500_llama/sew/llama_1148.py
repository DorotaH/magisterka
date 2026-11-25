import  sys

def check_rebus(rebus):
    numbers = rebus.split()
    operations = ['+', '-']
    n=int(numbers[-1])

    result=0
    for  i, num in  enumerate(numbers[:-1]):
        if not num == '?':
            result += int(num)
        else:
            result += 1

    for  i, op in  enumerate(operations):
        if not op == '+':
            result -= i + 1
        else:
            result += i + 1

    return result == n

def replace_rebus(rebus):
    numbers = rebus.split()
    operations = ['+', '-']
    n=int(numbers[-1])

    result = 0
    res = ''
    for  i, num in  enumerate(numbers[:-1]):
        if not num == '?':
            res += num + ' '
        else:
            if numbers[i-1] == '?':
                result += 1
            else:
                result += int(numbers[i-1])
            res += str(result) + ' '
            result = 0

    for  i, op in  enumerate(operations):
        if not op == '+':
            res += str(n - i) + ' '
        else:
            res += str(n - i) + ' '

    return res + numbers[-1]

def main():
    rebus=sys.stdin.readline().strip()
    if check_rebus(rebus):
        print('Possible')
        print(replace_rebus(rebus))
    else:
        print('Impossible')

if  __name__ == "__main__":
    main()
