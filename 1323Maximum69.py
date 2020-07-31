class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ''
        count = 0
        for ch in str(num):
            if ch == '9':
                res += ch
            elif ch == '6' and count == 0:
                res += '9'
                count += 1
            elif ch == '6':
                res += '6'
        return ''.join(res)