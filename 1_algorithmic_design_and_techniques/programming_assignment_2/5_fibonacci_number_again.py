# Uses python3
import sys

def get_fibonacci_huge_advanced(n, m):
    """
    Task: Given two integers n and m, output F_n mod m (that is, the remainder of F_n when divided by m)
    """
    # create a list for storing the remainders
    remainder_list = []
    # append the remainder of first and second Fibonacci number manually
    remainder_list.append(0)
    remainder_list.append(1)
    # find and store the Pisano period
    for i in range(2, n+1):
        remainder = (remainder_list[i-1]+remainder_list[i-2]) % m
        remainder_list.append(remainder)
        # check if the Pisano period has been repeated
        if (remainder_list[i]==1) and (remainder_list[i-1]==0):
            remainder_list = remainder_list[:-2]
            break
    # find the length of Pisano period and return F_n mod m
    cycle_len = len(remainder_list)
    idx = n % cycle_len
    return remainder_list[idx]
    
if __name__=='__main__':
    inp = sys.stdin.read();
    n, m = map(int, inp.split())
    print(get_fibonacci_huge_advanced(n, m))