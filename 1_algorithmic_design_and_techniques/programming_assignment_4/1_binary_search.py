# Uses python3
import sys
from math import floor

def binary_search(numbers, key):
    """
    Task: The goal in this code problem is to implement the binary search algorithm.
    """
    left_idx, right_idx = 0, len(numbers)-1
    # binary search alg.
    while left_idx<=right_idx:
        mid_idx = floor(left_idx + (right_idx-left_idx)/2)
        # 判斷 key 位在 mid_idx 的左側還是右側，若已經找到則回傳 index
        if key==numbers[mid_idx]:
            return mid_idx
        elif key>numbers[mid_idx]:
            left_idx = mid_idx+1
        else:
            right_idx = mid_idx-1
    return -1

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    m = data[n+1]
    numbers = data[1:n+1]
    for key in data[n+2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(numbers, key), end = ' ')
