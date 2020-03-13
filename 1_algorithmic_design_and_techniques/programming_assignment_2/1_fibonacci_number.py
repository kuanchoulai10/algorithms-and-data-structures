# Uses python3
def calc_fib(n):
    """
    Task: Given an interger n, find the nth Fibonacci number F_n
    """
    # create a list for storing all Fibonacci numbers before nth
    fib_list = []
    # append first and second Fibonacci number manually 
    fib_list.append(0)
    fib_list.append(1)
    # append all the Fibonacci numbers before nth
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    # return nth Fibbonacci number
    return fib_list[n]

n = int(input())
print(calc_fib(n))