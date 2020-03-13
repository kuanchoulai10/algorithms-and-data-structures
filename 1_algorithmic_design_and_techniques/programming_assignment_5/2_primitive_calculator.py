# Uses python3
import sys

def optimal_sequence(num):
    """
    Task. Given an integer n, compute the minimum number of operations needed to obtain the number n starting from the number 1.
    """
    # 負責儲存每個數字的最小操作數目: (key,value)=(number, min_ops)
    num_ops_dict = {}
    num_ops_dict[1] = 0
    # 負責儲存每個數字的歷史運算過程: (key,value)=(number, sequence: list)
    seqs_dict = {}
    seqs_dict[1] = [1]

    # 迭代每個數字
    for n in range(2, num+1):
        # 計算三種數學操作下的最小操作數目: (key,value)=(prev_state,num_ops)
        cands = {}
        cands[n/3] = num_ops_dict[n/3]+1 if n%3==0 else float('inf')
        cands[n/2] = num_ops_dict[n/2]+1 if n%2==0 else float('inf')
        cands[n-1] = num_ops_dict[n-1]+1
        # 找出三種數學操作下，最小的操作數目
        prev_state, min_ops = sorted(cands.items(), key=lambda x: x[1])[0]
        # 更新當前數字的 `num_ops_dict` 和 `seqs_dict`
        num_ops_dict[n] = min_ops
        seqs_dict[n] = list(seqs_dict[prev_state]) + [n]

    return num_ops_dict[num], seqs_dict[num]


if __name__ == '__main__':
    num = int(sys.stdin.read())
    min_ops, seq = optimal_sequence(num)
    print(min_ops)
    for x in seq:
        print(x, end=' ')

# for debugging
# min_ops, seq = optimal_sequence(5)
# print(min_ops)
# for x in seq:
#     print(x, end=' ')