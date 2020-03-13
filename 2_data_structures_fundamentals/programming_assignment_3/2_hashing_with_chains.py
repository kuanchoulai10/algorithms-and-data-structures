# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.bkt_idx = int(query[1])
        else:
            self.name = query[1]


class QueryProcessor:
    # 用來計算雜湊值的參數
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, num_bkts):
        self.num_bkts = num_bkts
        # 負責儲存每個 bucket 裡的所有 names
        self.bkts = [[] for _ in range(num_bkts)]

    def _hash_func(self, S):
        """S: str"""
        hashed_val = 0
        for c in reversed(S):
            hashed_val = (hashed_val*self._multiplier + ord(c)) % self._prime
        hashed_val %= self.num_bkts
        return hashed_val

    def process_query(self, qry):
        """
        分兩種情況處理
        1. 'check'
        2. 'find', 'add', 'del'
        """
        # 如果當前操作是'check'，則印出指定 bucket 裡的所有 name
        if qry.type == "check":
            bkt = self.bkts[qry.bkt_idx]
            print(' '.join(bkt))
            return

        # 試著找出 qry.name 位在哪個 bucket 裡的哪個位置 (name_idx)
        bkt_idx = self._hash_func(qry.name)
        bkt = self.bkts[bkt_idx]
        try:
            # 1-based index
            name_idx = bkt.index(qry.name)+1
        except ValueError:
            name_idx = None

        # 根據當前操作('find', 'add', 'del') 進行相對應的操作
        if qry.type == 'find':
            print('yes' if name_idx else 'no')
        elif qry.type == 'add':
            bkt.insert(0, qry.name) if not name_idx else None
        else:
            # (name_idx-1) for recovering 0-based index
            bkt.pop(name_idx-1) if name_idx else None

    def read_query(self):
        """
        讀取 query 並轉換成 Query 物件
        input().split() 之後的格式會是這樣: ['add','Hello'], ['del','Nancy'], ['find','Kevin'], ['check',15], ...
        """
        return Query(input().split())

    def process_queries(self):
        """wrapper method"""
        num_qrys = int(input())
        for _ in range(num_qrys):
            self.process_query(self.read_query())


if __name__ == '__main__':
    num_bkts = int(input())
    proc = QueryProcessor(num_bkts)
    proc.process_queries()
