# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    """
    Task: Given an integer n, find the last digit of the nth Fibonacci number F_n (that is, F_n mod 10).
    """
    # create a list for storing last digit of all the Fibonacci numbers before nth
    last_digit_list = []
    # append last digit of first and second Fibonacci number manually
    last_digit_list.append(0)
    last_digit_list.append(1)
    # append last digit of all the Fibonacci numbers before nth
    for i in range(2, n+1):
        last_digit = (last_digit_list[i-1] + last_digit_list[i-2]) % 10
        last_digit_list.append(last_digit)
    # return last digit of nth Fibbonacci number
    return last_digit_list[n]

if __name__ == '__main__':
    n = sys.stdin.read()
    n = int(n)
    print(get_fibonacci_last_digit_naive(n))
