class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        i = 0
        for x in range(len(index)):
            target.insert(index[x], nums[i])
            i = i + 1

        return target