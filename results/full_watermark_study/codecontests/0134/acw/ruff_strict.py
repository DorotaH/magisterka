n, target = map(float, input().split())
n = int(n)


def getprob(study):

    tot = (n - 1) * n * (n - 2) // 6
    case1 = (study - 1) * study * (study - 2) // 6
    case2 = (study - 1) * study * (n - study) // 2
    case3 = (n - study) * study * (n - study - 1) // 2

    return (case1 + case2 + 0.5 * case3) * 1.0 / tot


front = 0
rear = n


while rear > front:
    mid = (rear + front) // 2
    p = getprob(mid)

    #    print(mid,p)

    if target > p:
        front = mid + 1
    else:
        rear = mid


print(front)
