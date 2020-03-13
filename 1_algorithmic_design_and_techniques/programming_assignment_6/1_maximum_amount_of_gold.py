# Uses python3
import sys
from numpy import zeros

def optimal_weight(W, n, bars):
    """
    Task: Given n gold bars, find the maximum weight of gold that fits into a bag of capacity W.
    """
    # 負責紀錄在多少個金條、多少背包容量情況下，最多能裝下多少重量
    w_mat = zeros((n+1,W+1), dtype='int32')
    
    # 迭代每個金條、每個背包容量的情形
    for i in range(1, n+1):
        w_i = bars[i-1]
        for cap in range(1, W+1):
            # 判斷當前背包容量是否裝得下當前的金條
            if cap<w_i:
                # 裝不下就直接沿用「背包容量不變」、「金條數目少一條」情形下的最大負重值
                weight = w_mat[i-1, cap]
            else:
                # 裝得下就必須判斷，兩種情形的最大負重值，取其大
                weight = max(w_mat[i-1,cap], w_mat[i-1,cap-w_i]+w_i)
            # 更新
            w_mat[i, cap] = weight

    return w_mat[n,W]

if __name__ == '__main__':
    # bars: list of ints sorted in ascending order
    W, n, *bars = list(map(int, sys.stdin.read().split()))
    print(optimal_weight(W, n, bars))
