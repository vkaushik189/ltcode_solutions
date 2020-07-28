class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = [None] * len(s)
        for x in range(len(indices)):
            new_s[indices[x]] = s[x]
        return ''.join(new_s)