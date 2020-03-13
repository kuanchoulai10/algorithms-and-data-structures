#Uses python3
import sys

def max_dot_product(n, seq_a, seq_b):
    """
    Task: Given two sequences a_1, a_2, ..., a_n (a_i is the profit per click of the i-th ad) and b_1, b_2, ..., b_n (b_i is the average 
    number of clicks per day of the i-th slot), we need to partition them into n pairs (ai, bj) such that the sum of their product is 
    maximized.
    """
    # sort seq_a and seq_b in descending order
    seq_a = sorted(seq_a, reverse=True)
    seq_b = sorted(seq_b, reverse=True)
    # greedy alg.
    total_revenue = 0
    for i in range(n):
        total_revenue += seq_a[i] * seq_b[i]
    return total_revenue

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    seq_a = data[1:(n+1)]
    seq_b = data[(n+1):]
    print(max_dot_product(n, seq_a, seq_b))