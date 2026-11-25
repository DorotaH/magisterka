from collections import defaultdict


def election_result(n, k, m, a, votes):
    # Create a dictionary to store the votes count and last vote time for each candidate
    vote_dict = defaultdict(lambda: [0, 0])
    for  vote in  votes:
        vote_dict[vote][0]+=1
        vote_dict[vote][1]=a + 1

    # Sort the candidates by votes count and last vote time
    sorted_candidates = sorted(vote_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))

    # Initialize the result list
    result = [0] * n

    # Check if the top k candidates have more than 0 votes
    for  i, (candidate, _) in  enumerate(sorted_candidates, 0):
        if  k > i and  sorted_candidates[i][1][0]>0:
            result[candidate - 1] = 1
        elif  i < k:
            result[candidate - 1] = 2

    # Check if any candidate has less than 1 vote
    for  i, (candidate, _) in  enumerate(sorted_candidates, 0):
        if  sorted_candidates[i][1][0] == 0:
            result[candidate - 1] = 3
            break

    return result


n, k, m, a = map(int, input().split())
votes = list(map(int, input().split()))

result = election_result(n, k, m, a, votes)
print(' '.join(map(str, result)))
