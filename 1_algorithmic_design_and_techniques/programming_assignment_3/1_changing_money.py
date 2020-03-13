# Uses python3
import sys

def get_change(m):
    """
    Task: The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with 
    denominations 1, 5, and 10.
    """
    num_coins = 0
    # greedy alg.
    for value in [10, 5, 1]:
        num_coins += (m//value)
        m %= value
    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
