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

def fibonacci_partial_sum_advanced(m, n):
    """
    Task: Given two non-negative integers m and n, where m <= n, find the last digit of the sum F_m + F_{m+1} + ... + F_n
    """
    last_digit_list = get_pisano_period_list(10)
    cycle_len = len(last_digit_list)
    # update the list to the last digit of a sum of the first n Fibonacci numbers
    for i in range(2, cycle_len):
        last_digit_list[i] = (last_digit_list[i]+last_digit_list[i-1]) % 10
    
    # find the index
    idx_m = m % cycle_len
    idx_n = n % cycle_len
    
    # calculate the last digit of the partial sum from F_m to F_n
    partial_sum_last_digit = last_digit_list[idx_n]-last_digit_list[idx_m-1]
    partial_sum_last_digit = partial_sum_last_digit if partial_sum_last_digit>=0 else partial_sum_last_digit+10
    return partial_sum_last_digit

if __name__=='__main__':
    inp = sys.stdin.read()
    m, n = map(int, inp.split())
    print(fibonacci_partial_sum_advanced(m, n))