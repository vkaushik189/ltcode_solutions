def removeOuterParentheses(str="(()())(())"):
    '''
    res = ''
    count = int()
    len = 0
    for ch in str:
        if ch == '(':
            count += 1
            len += 1
        elif ch == ')':
            count -= 1
            len += 1
        if count == 0 and len > 2:
            res += '()'
            len = 0
    print(res)
    '''

    lst = list(str)
    new_lst = []
    for i in range(len(str)-1):
        if lst[i] == '(' and lst[i+1] == ')':
            lst.pop(lst[i])
            lst.pop(lst[i+1])
    return ''.join(new_lst)


removeOuterParentheses()