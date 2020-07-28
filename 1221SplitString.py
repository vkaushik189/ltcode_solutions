class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = int()
        max_str = 0
        for c in s:
            if c == 'R':
                count += 1
            if c == 'L':
                count -= 1
            if count == 0:
                max_str += 1
        return max_str