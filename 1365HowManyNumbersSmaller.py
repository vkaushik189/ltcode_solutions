class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        min_list = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count = count + 1
            min_list.append(count)
        return min_list
        '''

        min_list = sorted(nums)
        # index method returns the first match of i
        return [min_list.index(i) for i in nums]

