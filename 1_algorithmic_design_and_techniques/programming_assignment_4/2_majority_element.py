# Uses python3
import sys

def get_majority(n, numbers):
    """
    Task: The goal in this code problem is to check whether an input sequence contains a majority element.
    """
    left = 0
    right = n
    majority_element, _ = get_majority_element(numbers, left, right)
    return 1 if (majority_element!=-1) else 0

def get_majority_element(numbers, left, right):
    """
    inner function for `get_majority()` function
    """
    # 計算目前序列個數，如果只剩 1 個，則回傳該元素和 1 計次
    n = right-left
    if n==1:
        return numbers[left], 1
    
    # 取得左右兩側的 majority
    mid = left + n//2
    left_majority, left_count = get_majority_element(numbers, left, mid)
    right_majority, right_count = get_majority_element(numbers, mid, right)
    
    # 如果左右兩側都沒有 majority ，則回傳 -1 和 0 計次
    if left_majority==right_majority==-1:
        return -1, 0
    # 如果左右兩側的 majority 都一致，則回傳該 majority 和加總過後的計次
    elif left_majority==right_majority:
        return left_majority, left_count+right_count
    # 如果左右兩側的 majority 不一致，則判斷哪個才是真正的 majority
    else:
        # 如果其中一側有 majority ，則更新該 majority 的總計次 (加上該 majority 於另一側的出現次數)
        left_count += numbers[mid:right].count(left_majority) if (left_majority!=-1) else 0
        right_count += numbers[left:mid].count(right_majority) if (right_majority!=-1) else 0
        # 判斷是否為絕對半數
        if left_count>(n/2):
            return left_majority, left_count
        elif right_count>(n/2):
            return right_majority, right_count
        else:
            return -1, 0


if __name__ == '__main__':
    n, *numbers = list(map(int, sys.stdin.read().split()))
    print(get_majority(n, numbers))