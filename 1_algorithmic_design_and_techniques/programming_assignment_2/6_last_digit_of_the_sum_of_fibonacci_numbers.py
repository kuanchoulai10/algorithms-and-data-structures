# Uses python3
import sys

def get_pisano_period_list(m):
    """
    Task: Given an integer m, output the Pisano period list of (F mod m).
    """
    remainder_list = []
    remainder_list.append(0)
    remainder_list.append(1)
    
    # find and store the Pisano period
    i = 2
    while True:
        r = (remainder_list[i-1]+remainder_list[i-2]) % m
        remainder_list.append(r)
        # check if the Pisano period has been repeated
        if (remainder_list[i]==1) and (remainder_list[i-1]==0):
            remainder_list = remainder_list[:-2]
            break
        i += 1
    return remainder_list

def fibonacci_sum_advanced(n):
    """
    Task: Given an integer n, find the last digit of the sum (F_0 + F_1 + ... + F_n).
    """
    last_digit_list = get_pisano_period_list(10)
    cycle_len = len(last_digit_list)
    # update the list to the last digit of a sum of the first n Fibonacci numbers
    for i in range(2, cycle_len):
        last_digit_list[i] = (last_digit_list[i]+last_digit_list[i-1]) % 10
    
    idx = n % cycle_len
    return last_digit_list[idx]

if __name__=='__main__':
    inp = sys.stdin.read()
    n = int(inp)
    print(fibonacci_sum_advanced(n))