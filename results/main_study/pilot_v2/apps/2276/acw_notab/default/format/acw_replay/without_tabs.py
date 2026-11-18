# returns answer to the subproblem with interval range [start, end],
# but with a total of "extra" additional stuff on the end
# that must be deleted last.
memo = {}


def f(dat, rewards, start, end, extra):
    curr = (start, end, extra)
    if curr in memo:
        return memo[curr]

    if start > end:
        return 0
    if start == end:
        memo[curr] = rewards[extra + dat[start]]
        return memo[curr]

    # test all possible "cut points".
    # "cut" is the earliest index to die in the same deletion as "end".
    out = 0
    for cut in range(end, start - 1, -2):
        if cut == end:
            # in this case, we're deleting the last interval right away.
            out_curr = rewards[dat[cut] + extra]
            out_curr += f(dat, rewards, start, cut - 1, 0)
        else:
            # split into 2 pieces:
            # 1) slots [start, cut] plus [end + extra]
            # 2) slots [cut+1, end-1] (with no extra, this needs to get deleted first).
            out_curr = f(dat, rewards, start, cut, dat[end] + extra)
            out_curr += f(dat, rewards, 1 + cut, end - 1, 0)

        out = max(out, out_curr)

    memo[curr] = out
    return memo[curr]


def solve(dat_str, rewards_orig):
    # break into intervals.
    dat = []
    pos = 0
    while pos < len(dat_str):
        end = pos
        while len(dat_str) > end and dat_str[pos] == dat_str[end]:
            end += 1

        dat.append(end - pos)
        pos = end

    # compute the highest-value way to remove a run of size k.
    # (google translated from C++ thinking)
    rewards = [0, rewards_orig[0]]
    rewards.extend(
        max(rewards[k - j] + rewards_orig[j - 1] for j in range(1, k + 1))
        for k in range(2, 1 + len(rewards_orig))
    )
    # print("dat: {}".format(dat))
    # print("rewards: {}".format(rewards))

    return f(dat, rewards, 0, len(dat) - 1, 0)


# get the integer
int_dummy = input()
# get the string
dat_str = input().strip()
# get the array
rewards_input = input().strip().split()
rewards_ints = [int(x) for x in rewards_input]

# print(dat_str)
# print(rewards_ints)

print(
    (
        solve(
            dat_str,
            rewards_ints,
        )
    )
)


# dat_test = "10101"
# rewards_test = [3, 10, 15, 15, 15]
# print(solve(dat_test, rewards_test))
