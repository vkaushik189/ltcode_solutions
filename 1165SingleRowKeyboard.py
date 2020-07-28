'''
row1 = 'qwertyuiop'
row2 = 'asdfghjkl'
row3 = 'zxcvbnm'

query = 'kaudfsdvsdcsd'
query_row1 = 0
query_row2 = 0
query_row3 = 0
for c in query:
    if c not in row1:
        break
    else:
        query_row1 += 1

for c in query:
    if c not in row2:
        break
    else:
        query_row2 += 1

for c in query:
    if c not in row3:
        break
    else:
        query_row3 += 1

if query_row1 == len(query) or query_row2 == len(query) or query_row3 == len(query):
    print('True')
else:
    print('False')
'''

def singleRowKB(row1 = 'qwertyuiop', row2 = 'asdfghjkl', row3 = 'zxcvbnm', query = 'kasak'):
    query_row1 = 0
    query_row2 = 0
    query_row3 = 0
    for c in query:
        if c not in row1:
            break
        else:
            query_row1 += 1

    for c in query:
        if c not in row2:
            break
        else:
            query_row2 += 1

    for c in query:
        if c not in row3:
            break
        else:
            query_row3 += 1

    if query_row1 == len(query) or query_row2 == len(query) or query_row3 == len(query):
        print('True')
    else:
        print('False')

singleRowKB()