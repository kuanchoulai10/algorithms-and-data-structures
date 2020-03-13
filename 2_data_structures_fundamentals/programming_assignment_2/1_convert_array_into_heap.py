# Uses python3

def sift_down(data, current):
    """
    判斷當前節點是否滿足 heap　，若不滿足則必須將當前節點往下移一層，直到滿足 min-heap 為止
    若「子節點」小於「當前節點」時，必須互換　(若兩個子節點同時滿足，則挑較小的子節點)
    """
    # `swaps` 負責記錄 swap 的操作
    # `target` 負責記錄當前節點要與哪個子節點互換
    # `end` 負責記錄最後一個節點在哪，避免超出範圍
    swaps = []
    target = current
    end = len(data)-1
    # 如果左節點索引位置沒有超出範圍，且左節點小於當前節點，則將`target`游標指向左節點
    left = 2*current+1
    if (left<=end) and (data[left]<data[target]):
        target = left
    # 如果右節點索引位置沒有超出範圍，且右節點小於`target`游標指向的節點(可能是當前節點，也可能是左節點)，則將`target`游標指向右節點
    right = 2*current+2
    if (right<=end) and (data[right]<data[target]):
        target = right
    # 若需要互換，則進行相關操作，並往下一層
    if current!=target:
        swaps.append((current,target))
        data[current], data[target] = data[target], data[current]
        swaps += sift_down(data, target)
    #####################################################
    return swaps

def build_heap(n, data):
    """
    Task: The first step of the `HeapSort` algorithm is to create a heap from the array you want to sort. 
        By the way, did you know that algorithms based on Heaps are widely used for external sort, when you need
        to sort huge files that don’t fit into memory of a computer? Your task is to implement this first step 
        and convert a given array of integers into a heap. You will do that by applying a certain number of swaps to the array.
        Swap is an operation which exchanges elements a_i and a_j of the array a for some i and j. You will need to convert the array
        into a heap using only O(n) swaps, as was described in the lectures. Note that you will need to use a min-heap instead 
        of a max-heap in this problem.
    """
    swaps = []
    # 迭代前半段的 list (由後往前)
    # 以 heap 結構理解的話則是從倒數第二層的節點開始，依序往回(往前一個，接著上一層節點)調整當前節點的資料結構，直到根節點為止
    for current in range((n//2)-1, -1, -1):
        swaps += sift_down(data, current)
    return len(swaps), swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    m, swaps = build_heap(n, data)
    print(m)
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
