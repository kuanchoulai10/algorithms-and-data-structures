# Uses python3
import sys

def optimal_summands(num):
    """
    Task: The goal of this problem is to represent a given positive integer n as a sum of as many pairwise distinct positive integers as
    possible. That is, to find the maximum k such that n can be written as (a_1 + a_2 + ... + a_k) where (a_1, ..., a_k) are positive
    integers and a_i != a_j for all 1 <= i <= j <= k
    """
    summands = []
    count = 0
    # greedy alg.
    while num!=0:
        count += 1
        # (num-count)>count condition checks whether there is a chance to go to the next round
        # for example: (15-7)>7 means going to the next round (count=8) is fine.
        quantity = count if (num-count)>count else num
        # update `summands` and `num`
        summands.append(quantity)
        num -= quantity
    return summands


if __name__ == '__main__':
    num = int(sys.stdin.read())
    summands = optimal_summands(num)
    print(len(summands))
    for x in summands:
        print(x, end=' ')