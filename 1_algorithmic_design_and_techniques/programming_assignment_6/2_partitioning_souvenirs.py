# Uses python3
import sys

def allocation3(nums, lookup, idx, cap1, cap2, cap3):
    # return true if subset is found
    if cap1==cap2==cap3==0:
        return True

    # base case: no items left
    if idx<0:
        return False

    # construct an unique key from dynamic programming elements of the input
    key = f"{idx}|{cap1}|{cap2}|{cap3}"

    # if sub-problem is seen for the first time, solve it and store its result in a dict
    if key not in lookup:
        # 取出數列最後一項元素，作為當前元素
        num = nums[idx]

        # case 1: current item becomes part of first subset
        has_sol1 = False
        if (cap1>=num):
            has_sol1 = allocation3(nums, lookup, idx-1, cap1-num, cap2, cap3)

        # case 2: current item becomes part of second subset
        has_sol2 = False
        if (not has_sol1) and (cap2>=num):
            has_sol2 = allocation3(nums, lookup, idx-1, cap1, cap2-num, cap3)

        # case 3: current item becomes part of third subset
        has_sol3 = False
        if (not has_sol1) and (not has_sol2) and (cap3>=num):
            has_sol3 = allocation3(nums, lookup, idx-1, cap1, cap2, cap3-num)

        # return true if we get solution
        lookup[key] = has_sol1 or has_sol2 or has_sol3

    # if sub-problem has been solved before, just return the solution from the dict
    return lookup[key]

def partition3(n, nums):
    """
    Input Format: The first line contains an integer n. The second line contains integers v_1, v_2, ..., v_n separated by spaces.
    Output Format: Output 1, if it's possible to partition v_1, v_2, ..., v_n into three subsets with equal sums, and 0 otherwise.
    """
    total_sum = sum(nums)
    qt, rmd = divmod(total_sum, 3)
    # 如果有以下三種情形，則絕對無法分成三個擁有相同加總值的子數列
    # - 數列個數小於 3
    # - 數列加總值不整除於 3
    # - 「數列最大值」大於「子數列加總值」
    if n<3 or rmd or max(nums)>qt:
        return False
    
    lookup = {}
    nums.sort()
    return allocation3(nums, lookup, n-1, qt, qt, qt)

if __name__ == '__main__':
    n, *nums = list(map(int, sys.stdin.read().split()))
    print(1 if partition3(n, nums) else 0)

# for debugging
# n = 13
# nums = [1,2,3,4,5,5,7,7,8,10,12,19,25]
# assert partition3(n, nums)==True

# reference
# https://www.techiedelight.com/3-partition-problem/