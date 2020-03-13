# Uses python3
from collections import namedtuple

Brackets = namedtuple(typename='Brackets', field_names=['idx','type'])

def find_mismatch(code):
    """
    Input Format: Input contains one string S which consists of big and small latin letters, digits, punctuation marks 
        and brackets from the set []{}().

    Output Format. If the code in S uses brackets correctly, output "Success" (without the quotes). 
        Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
        brackets, output the 1-based index of the first unmatched opening bracket.
    """
    # 負責儲存 opening brackets
    stack = []
    
    # 迭代每個 char
    for idx, char in enumerate(code):
        # for correcting the index from 0-based index to 1-based index
        idx += 1
        
        # 如果是 opening brac.，則加入 stack
        if char in "([{":
            op_brac = Brackets(idx, char)
            stack.append(op_brac)
        # 如果是 closing bracket ，則必須判斷以下情形
        elif char in ")]}":
            cs_brac = Brackets(idx, char)
            # 有 closing brac. 但沒有 opening brac. ，輸出當前 closing brac. 位置
            if len(stack)==0:
                return cs_brac.idx
            # 有成雙成對的 brackets ，判斷它們是否 match
            # - 若 match 就 pop opening brac.
            # - 若 unmatch 就輸出當前 closing brac. 位置
            op_brac = stack[-1]
            if (op_brac.type+cs_brac.type) in ['()','[]','{}']:
                stack.pop()
            else:
                return cs_brac.idx
    # 配對成功則回傳 "Success"
    # 配對失敗 (有 opening brac. 但沒有 closing brac.) 則回傳 opening brac. 位置
    return "Success" if len(stack)==0 else stack[-1].idx

if __name__ == "__main__":
    print(find_mismatch(input()))