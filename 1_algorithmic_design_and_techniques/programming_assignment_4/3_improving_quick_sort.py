# Uses python3
import sys
import random

def partition3(nums, left, right):
    """
    inner function for `randomized_quick_sort()` function
    """
    # 造成此種原因就是因為隨機挑選到基準值為最大值或最小值的時候
    # 因此其實只有一個子序列需要進行排序，另個子序列的將會left==right
    if left==right:
        return 

    # 隨機挑選個基準值，並置換到序列的第一個位置
    p_idx = random.randrange(left, right)
    pivot = nums[p_idx]
    nums[left], nums[p_idx] = nums[p_idx], nums[left]
    
    # 定義「小於基準值」和「等於基準值」的游標，定位在各該部分最後一個元素上
    lt_cs = left
    eq_cs = left

    # 遍歷整個序列(除了基準值本身)
    for i in range(left+1, right):
        # 如果當前元素小於基準值，則
        # 將「小於基準值」與「等於基準值」的游標，移動至下一個位置並進行相對應的置換
        if nums[i]<pivot:
            lt_cs += 1
            nums[lt_cs], nums[i] = nums[i], nums[lt_cs]
            eq_cs += 1
            # 如果「小於基準值」與「等於基準值」的游標在不同位置，則需進行置換動作
            # 反之，則不需要進行置換動作 (因為目前沒有「等於基準值的部分」)
            if lt_cs!=eq_cs:
                nums[eq_cs], nums[i] = nums[i], nums[eq_cs]
        # 如果當前元素等於基準值，則
        # 將「等於基準值」的游標移動至下一個位置，並將當前元素置換過去
        elif nums[i]==pivot:
            eq_cs += 1
            nums[i], nums[eq_cs] = nums[eq_cs], nums[i]
        # 如果當前元素大於基準值，則不做任何行動
    
    # 再來，將位在第一個位置的基準值，置換到「小於基準值」的游標所在位置
    # 值得注意的是，置換過後的 lt_cs 其實是停留在「等於基準值」的第一個位置
    nums[left], nums[lt_cs] = nums[lt_cs], nums[left]
	
    # 接著，更新 eq_cs ，使得 eq_cs 是停留在「大於基準值」的第一個位置
    eq_cs += 1
    
    # 最後，再針對「大於」和「小於」基準值的子序列，進行排序。
    partition3(nums, left, lt_cs)
    partition3(nums, eq_cs, right)

def randomized_quick_sort(n, nums):
    """
    Task: To force the given implementation of the quick sort algorithm to efficiently process sequences with
    few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
    partition procedure should partition the array into three parts: '<pivot' part, '=pivot' part, '>pivot' part.
    """
    left = 0
    right = n
    partition3(nums, left, right)

if __name__ == '__main__':
    n, *nums = list(map(int, sys.stdin.read().split()))
    randomized_quick_sort(n, nums)
    for num in nums:
        print(num, end=' ')
