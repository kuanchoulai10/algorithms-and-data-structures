# Uses python3
import sys
from collections import namedtuple
Point = namedtuple(typename='Point', field_names=['value', 'type'])

def merge_sort(seq):
    # 如果序列個數為 1 ，則直接回傳「該序列」
    if len(seq)==1:
        return seq
    # 將左、右序列分別排序，接著合併起來
    mid = len(seq)//2
    left_seq = merge_sort(seq[:mid])
    right_seq = merge_sort(seq[mid:])
    seq = merge(left_seq, right_seq)
    return seq

def merge(left_seq, right_seq):
    seq = []
    # 比較兩個序列中最小的數並移至 `seq` ，重複此步驟直到一方沒有任何元素為止。同時，計算「倒置次數」
    while len(left_seq)>0 and len(right_seq)>0:
        if left_seq[0].value<=right_seq[0].value:
            seq.append(left_seq.pop(0))
        else:
            seq.append(right_seq.pop(0))
    # move the rest of `left_seq` and `right_seq` to the end of the `seq`
    while len(left_seq)!=0:
        seq.append(left_seq.pop(0))
    while len(right_seq)!=0:
        seq.append(right_seq.pop(0))
    return seq

def fast_count_segments(starts, ends, points):
    """
    Task: You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
    each point, the number of segments that contain this point.
    """
    pts = [Point(s, "start") for s in starts]
    pts += [Point(p, "point") for p in points]
    pts += [Point(e, "end") for e in ends]
    pts = merge_sort(pts)
    # 計算每個 `Point(type='point')` 目前位於多少個區間內，以 dict 儲存
    rslt = {}
    count = 0
    for pt in pts:
        if pt.type=="start":
            count += 1
        elif pt.type=="end":
            count -= 1
        else:
            rslt[pt.value] = count
    # 將結果轉換成 list
    rslt = [rslt[p] for p in points]
    return rslt

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    m = data[1]
    starts = data[2:2*n+2:2]
    ends = data[3:2*n+2:2]
    points = data[2*n+2:]

    rslt = fast_count_segments(starts, ends, points)
    for cnt in rslt:
        print(cnt, end=' ')
