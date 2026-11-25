
a, b = map(int, input().split())


def find_max_score(a, b):
    if  a == 0:
        return  -b * b, 'x' * b
    if  b == 0:
        return  a * a, 'o' * a

    # use dynamic programming to maximize the score
    scores = [0] * (a + b + 1)
    max_scores = [0] * (a + b + 1)
    for i in range(1, a+b+1):
        if i > 0:
            scores[i] = scores[i - 1]
            max_scores[i] = max_scores[i - 1]
        for j in range(1, 1 + min(a, i)):
            if  scores[i-j]+(j * j)>scores[i]:
                scores[i]=scores[i-j]+j * j
                max_scores[i]=max(max_scores[i-j]+j * j, scores[i])

    # build the optimal sequence
    result = ''
    i = a + b
    while  i>0:
        if  i-1>=a:
            result = 'o' + result
            i -= 1
        elif  i-1>=1:
            result='x'+result
            i = i - 2
        else:
            result = 'o' + result
            i -= 1

    return  scores[a + b], result

score, deck = find_max_score(a, b)
print(score)
print(deck)
