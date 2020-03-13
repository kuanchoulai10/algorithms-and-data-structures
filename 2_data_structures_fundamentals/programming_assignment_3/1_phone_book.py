# Uses python3

class Query:
    def __init__(self, query):
        # either add, del or find
        self.type = query[0]
        # phone number
        self.number = int(query[1])
        # contact person
        if self.type=='add':
            self.name = query[2]

def read_queries():
    n = int(input())
    # there are n elements in the list and type of each element is Query which contains three attributes
    return [Query(input().split()) for i in range(n)]

def process_queries(queries):
    # 儲存 find query 的結果
    results = []
    # 使用 direct addressing 方法
    # contacts 儲存當前聯絡人姓名，索引位置的意義是電話號碼
    contacts = ['']*(10**7)
    # 迭代每個 query
    for cur_query in queries:
        number = cur_query.number
        # 加入新聯絡人，如果已在聯絡人清單當中，則修改其姓名
        if cur_query.type=='add':
            contacts[number] = cur_query.name
        # 刪除聯絡人
        elif cur_query.type=='del':
            contacts[number] = ''
        # 尋找聯絡人
        else:
            name = contacts[number]
            results.append(name if name!='' else 'not found')
    return results

def write_responses(results):
    print('\n'.join(results))


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
