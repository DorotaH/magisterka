def sum_difference(n):
    sumofsquares = 0
    squareofsum = 0
    for num in range(1, 1+n):
        sumofsquares = sumofsquares + num * num
        squareofsum = squareofsum + num
    squareofsum **= 2
    return squareofsum - sumofsquares