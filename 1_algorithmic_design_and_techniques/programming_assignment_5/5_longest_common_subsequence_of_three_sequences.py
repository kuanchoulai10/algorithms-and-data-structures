# Uses python3
import sys
from numpy import zeros

def lcs3(n, seq1, m, seq2, l, seq3):
    """
    Task: Given three sequences A = (a_1, a_2, ..., a_n), B = (b_1, b_2, ..., b_m), and C = (c_1, c_2, ..., c_l), find the length
    of their longest common subsequence, i.e., the largest non-negative integer p such that there exist indices 
    (1 <= i_1 < i_2 < ··· < i_p <= n), (1 <= j_1 < j_2 < ··· < j_p <= m), and (1 <= k_1 < k_2 < ··· < k_p <= l)
    such that a_{i1}=b_{j1}=c_{k1} , ..., a_{ip}=b_{jp}=c_{kp}.
    """
    # 維護「最長共同子序列」長度的矩陣，每個數值都代表不同序列長度交叉配對下的「最長共同子序列」長度
    len_mat = zeros((n+1,m+1,l+1), dtype='int32')

    # 迭代不同序列長度交叉配對的情形
    for i in range(1, n+1): 
        for j in range(1, m+1): 
            for k in range(1, l+1):
                # 判斷三個序列的最後一個元素是否相等
                # 相等，直接從「三個序列皆少了當前最後一個元素」的情形下的「最長共同子序列」長度 +1 而得
                # 不相等，則必須判斷「其中一個序列少了當前最後一個元素」的三種情形下的「最長共同子序列」長度取其大而得
                if seq1[i-1]==seq2[j-1]==seq3[k-1]:
                    len_mat[i,j,k] = len_mat[i-1,j-1,k-1]+1
                else:
                    len_mat[i,j,k] = max(len_mat[i-1,j,k], len_mat[i,j-1,k], len_mat[i,j,k-1])
    return len_mat[n,m,l]

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    seq1 = data[1:n+1]
    m = data[n+1]
    seq2 = data[n+2:n+m+2]
    l = data[n+m+2]
    seq3 = data[n+m+3:n+m+l+3]
    print(lcs3(n, seq1, m, seq2, l, seq3))
