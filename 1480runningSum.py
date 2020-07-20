class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumN = 0
        res = list(range(len(nums)))
        for i in range(len(nums)):
            sumN = sumN + nums[i]
            res[i] = sumN
        return res