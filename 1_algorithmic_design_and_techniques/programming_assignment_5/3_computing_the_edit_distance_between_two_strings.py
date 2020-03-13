# Uses python3
from numpy import zeros

def edit_distance(s1, s2):
    """
    Task: The goal of this problem is to implement the algorithm for computing the edit distance between two strings.

    Four types of operation:
    - insertion: 第二個字串丟出個字母，第一個字串略過
    - deletion: 第一個字串丟出個字母，第二個字母略過
    - match: 兩個字串都丟出個字母，剛好字母皆相同
    - mismatch: 兩個字串都丟出個字母，字母不同
    """
    # 將兩個字串轉成 list of chars 並計算長度
    s1 = list(s1)
    n = len(s1)
    s2 = list(s2)
    m = len(s2)
    # 維護 edit distance 矩陣，每個數值都代表 不同字串長度交叉配對下的 edit distance
    ed_mat = zeros((n+1,m+1), dtype='int32')
    # 若其中一個為空字串，則 edit distance 是隨著另個字串長度逐一遞增
    ed_mat[:,0] = range(n+1)
    ed_mat[0,:] = range(m+1)
    # 迭代不同字串長度交叉配對的情形
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 計算四種不同操作情形下的 edit distance
            insertion = ed_mat[i, j-1]+1
            deletion = ed_mat[i-1, j]+1
            match = ed_mat[i-1, j-1]
            mismatch = ed_mat[i-1, j-1]+1
            # 判斷當前兩個字串的 last char 是否相同，接著
            # 找出是哪個操作能得到最小的 edit distance 並更新至 edit distance 矩陣
            if s1[i-1]==s2[j-1]:
                ed_mat[i,j] = min(insertion, deletion, match)
            else:
                ed_mat[i,j] = min(insertion, deletion, mismatch)
    return ed_mat[n,m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))