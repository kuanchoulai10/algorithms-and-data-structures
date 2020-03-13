# Uses python3
import sys
from math import sqrt
from itertools import combinations
from collections import namedtuple
Point = namedtuple(typename='Point', field_names=['x', 'y'])

def revised_sort(pts, by):
    """
    根據 x 或 y 軸排序二維平面上的點 (遞升排序)
    """
    if by=='x':
        pts = sorted(pts, key=lambda pt: pt.x)
    elif by=='y':
        pts = sorted(pts, key=lambda pt: pt.y)
    return pts

def distance(pt1, pt2):
    """
    給定兩點，計算它們在二維平面上的距離(尚未開平方根)
    """
    d = (pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2
    return d

def search_region(pts, mid, lower_bound, upper_bound):
    """
    Input:
        mid: int
        lower_bound: float
        upper_bound: float
    Output:
        回傳落在 x 軸上 (lower_bound, upper_bound) 區間的點，它們的索引範圍
    """
    # 篩選落在 (lower_bound, median_line) 的點，直到超出索引範圍
    lower_idx = mid-1
    while lower_idx>=0:
        # 判斷當前 point 是否超出下界
        if pts[lower_idx].x>=lower_bound:
            lower_idx -= 1
        else:
            break
    # 迴圈結束後， lower_idx 會停留在 -1 或是第一個超出下界的點，因此要 +1 以恢復成正常的索引值
    lower_idx += 1

    # 篩選落在 (median_line, upper_bound) 的點，直到超出索引範圍
    upper_idx = mid
    while upper_idx<len(pts):
        # 判斷當前 point 是否超出上界
        if pts[upper_idx].x<=upper_bound:
            upper_idx += 1
        else:
            break

    return lower_idx, upper_idx

def brute_minimum_distance(pts):
    """
    當 len(pts)<=3 時，直接使用暴力解，回傳最短距離
    """
    min_d = float("inf")
    combs = combinations(pts, 2)
    for comb in combs:
        min_d = min(min_d, distance(comb[0], comb[1]))
    return min_d

def minimum_distance(pts):
    """
    Task: Given n points on a plane, find the smallest distance between a pair of two (different) points. Recall
    that the distance between points (x_1, y_1) and (x_2, y_2) is equal to \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}
    """
    ### STEP 1: 當平面上小於三個點的時候，直接使用暴力解，計算並回傳最短距離 ###
    if len(pts)<=3:
        min_d = brute_minimum_distance(pts)
        return min_d

    ### STEP 2: 找出左、右區間的最小距離 ###
    mid = len(pts)//2
    left_min_d = minimum_distance(pts[:mid])
    right_min_d = minimum_distance(pts[mid:])
    min_d = min(left_min_d, right_min_d)

    ### STEP 3: 篩選出 x 軸落在 median_line 左右各 min_d 距離的點，並依 y 軸排序###
    median_line = (pts[mid-1].x+pts[mid].x)/2
    lower_bound = median_line-min_d
    upper_bound = median_line+min_d
    lower_idx, upper_idx = search_region(pts, mid, lower_bound, upper_bound)
    filtered_pts = pts[lower_idx:upper_idx]
    filtered_pts = revised_sort(filtered_pts, by='y')

    ### STEP 4: 找出 x 軸落在 (lower_bound, upper_bound) 之間的點，它們的最小距離
    for i in range(len(filtered_pts)):
        pt1 = filtered_pts[i]
        for j in range(i+1, i+1+4):
            # 避免 IndexError
            if j>=len(filtered_pts):
                break
            pt2 = filtered_pts[j]
            # 如果垂直距離已經大於等於最短距離，則沒有再繼續下去的必要
            if (pt2.y-pt1.y)>=min_d:
                break
            min_d = min(min_d, distance(pt1, pt2))

    return min_d

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    pts = [Point(x_val, y_val) for x_val, y_val in zip(x,y)]
    pts = revised_sort(pts, by='x')
    print(f"{sqrt(minimum_distance(pts)):.4f}")

# for debugging
# x = [4,-2,-3,-1,2,-4,1,-1,3,-4,-2]
# y = [4,-2,-4,3,3,0,1,-1,-1,2,4]
# pts = [Point(x_val, y_val) for x_val, y_val in zip(x,y)]
# pts = revised_sort(pts, by='x')
# print(f"{sqrt(minimum_distance(pts)):.4f}")