class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        de = []
        for i in range(0, len(nums), 2):
            pair = []
            pair.append(nums[i])
            pair.append(nums[i + 1])
            arr = [nums[i + 1]] * nums[i]
            de += arr
        return de
