# Uses python3
import sys

def get_num_inversions(n, nums):
    """
    Task: The goal in this problem is to count the number of inversions of a given sequence.
    """
    _, num_inversions = merge_sort_and_count(nums)
    return num_inversions

def merge_sort_and_count(seq):
    """
    inner function of `get_num_inversions()` function
    """
    # 如果序列個數為 1 ，則直接回傳「該序列」和「倒置次數」
    if len(seq)==1:
        return seq, 0
    
    # 將左、右序列分別排序，接著合併起來
    mid = len(seq)//2
    left_seq, left_num_inversions = merge_sort_and_count(seq[:mid])
    right_seq, right_num_inversions = merge_sort_and_count(seq[mid:])
    seq, num_inversions = merge(left_seq, right_seq, left_num_inversions, right_num_inversions)
    return seq, num_inversions


def merge(left_seq, right_seq, left_num_inversions, right_num_inversions):
    """
    merge two sorted list into one sorted list
    """
    seq = []
    num_inversions = left_num_inversions + right_num_inversions
    
    # 比較兩個序列中最小的數並移至 `seq` ，重複此步驟直到一方沒有任何元素為止。同時，計算「倒置次數」
    while len(left_seq)>0 and len(right_seq)>0:
        if left_seq[0]<=right_seq[0]:
            seq.append(left_seq.pop(0))
        else:
            seq.append(right_seq.pop(0))
            num_inversions += len(left_seq)
    
    # move the rest of `left_seq` and `right_seq` to the end of the `seq`
    while len(left_seq)!=0:
        seq.append(left_seq.pop(0))
    while len(right_seq)!=0:
        seq.append(right_seq.pop(0))
    
    return seq, num_inversions

if __name__ == '__main__':
    n, *nums = list(map(int, sys.stdin.read().split()))
    print(get_num_inversions(n, nums))
