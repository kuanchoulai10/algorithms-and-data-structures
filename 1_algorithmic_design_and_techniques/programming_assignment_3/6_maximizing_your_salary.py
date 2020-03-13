# Uses python3
import sys

def is_greater_or_equal(num1, num2):
    """
    Check which combination makes larger number
    """
    combination_1 = int(f"{num1}{num2}")
    combination_2 = int(f"{num2}{num1}")
    return True if (combination_1>=combination_2) else False

def largest_number(numbers):
    """
    Task: Compose the largest number out of a set of integers.
    """
    answer = ""
    # greedy alg.
    while len(numbers):
        max_num = 0
        # find the best integer to maximize salary
        for num in numbers:
            max_num = num if is_greater_or_equal(num, max_num) else max_num
        answer += f"{max_num}"
        numbers.remove(max_num)
    return int(answer)

if __name__ == '__main__':
    data = sys.stdin.read().split()
    numbers = [int(x) for x in data[1:]]
    print(largest_number(numbers))