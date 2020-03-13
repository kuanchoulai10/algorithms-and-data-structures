# Uses python3
import sys

def get_change(money):
    """
    Task: The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with 
    denominations 1, 3, and 4.
    """
    # `min_dict` 負責儲存每個額度最少能用幾個硬幣表示: (key,value)=(amount, min_coins)
    min_dict = {}
    min_dict[0] = 0
    # 迭代每個額度大小
    for m in range(1, money+1):
        min_coins = float('inf')
        # 迭代每種硬幣幣值
        for c in [1, 3, 4]:
            # 避免 IndexError
            if m-c<0: break
            # 找出最少可用幾個硬幣，表示當前額度
            min_coins = min(min_coins, min_dict[m-c]+1)
        # 更新當前額度的最少硬幣數
        min_dict[m] = min_coins

    return min_dict[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
