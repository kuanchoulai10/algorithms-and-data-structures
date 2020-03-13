# Uses python3
from numpy import empty
        
def min_and_max(i, j, minima, maxima, ops):
    """
    給定一個 sub arithm. expr.，計算可能的最小、最大值
    """
    # 初始化負責記錄最小、最大值的變數
    mmin = float("inf")
    mmax = -float("inf")
    # 迭代當前 sub arithm. expr. 每種可能的兩個 sub sub arithm. exprs.
    # 舉例來說: 8+7*4-8
    # (8)+(7*4-8)
    # (8+7)*(4-8)
    # (8+7*4)-(8)
    for k in range(i, j):
        v1 = eval(f"{maxima[i,k]} {ops[k]} {maxima[k+1,j]}")
        v2 = eval(f"{minima[i,k]} {ops[k]} {minima[k+1,j]}")
        v3 = eval(f"{minima[i,k]} {ops[k]} {maxima[k+1,j]}")
        v4 = eval(f"{maxima[i,k]} {ops[k]} {minima[k+1,j]}")
        # 更新最大、最小值
        mmin = min(mmin, v1, v2, v3, v4)
        mmax = max(mmax, v1, v2, v3, v4)
    return mmin, mmax

def get_maximum_value(n, nums, ops):    
    """
    Task: Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic operations 
    using additional parentheses.
    """
    # 初始化兩個維度為 (n, n) 的上三角矩陣，負責儲存不同 sub arithm. expr. 之下的最小、最大值。
    # 舉例來說 n=6:
    # [X X X X X X
    #  0 X X X X X
    #  0 0 X X X X
    #  0 0 0 X X X
    #  0 0 0 0 X X
    #  0 0 0 0 0 X]
    # 第 0 軸代表 sub arithm. expr. 的起始數字 idx
    # 第 1 軸代表 sub arithm. expr. 的終止數字 idx
    minima = empty((n,n), dtype='int64')
    maxima = empty((n,n), dtype='int64')

    # 從左上到右下，依序迭代每個 sub arithm. expr. 情況。
    # 舉例來說 n=6 :
    # (i,j) 遍歷順序如下
    # (0,0) -> (1,1) -> (2,2) -> (3,3) -> (4,4) -> (5,5) # m=0
    # (0,1) -> (1,2) -> (2,3) -> (3,4) -> (4,5) ->       # m=1
    # (0,2) -> (1,3) -> (2,4) -> (3,5) ->                # m=2
    # (0,3) -> (1,4) -> (2,5) ->                         # m=3
    # (0,4) -> (1,5) ->                                  # m=4
    # (0,5)                                              # m=5
    for m in range(0, n):
        # sliding window
        for i in range(n-m):
            j = i+m
            # 更新當前 sub arithm. expr. 的最大、最小值
            minima[i,j], maxima[i,j] = min_and_max(i, j, minima, maxima, ops) if i!=j else (nums[i],nums[j])

    # 回傳整個算術表達式的最大值，對應到 `maxima` 矩陣右上角的值
    return maxima[0,-1]

if __name__ == "__main__":
    data = input()
    nums = data[0::2]
    ops = data[1::2]
    n = len(nums)
    print(get_maximum_value(n, nums, ops))

# for debugging
# nums = [5,8,7,4,8,9]
# ops = ['-','+','*','-','+']
# n = len(nums)
# print(get_maximum_value(n, nums, ops))