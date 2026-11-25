import math


def get_winner(n, k):
    # Calculate the minimum number of diplomas
    diploma_min = math.ceil(n / (1 + k))

    # Calculate the maximum number of winners
    winner_max = min(math.ceil(n / 2), n - diploma_min)

    # Calculate the number of certificates
    certificate_max = winner_max * k

    # Calculate the number of non-winners
    non_winner = n - winner_max

    return  diploma_min, certificate_max, non_winner

def main():
    n, k = map(int, input().split())
    diploma, certificate, non_winner = get_winner(n, k)
    print(diploma, certificate, non_winner)


if  __name__ == "__main__":
    main()
