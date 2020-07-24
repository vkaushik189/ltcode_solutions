class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + (2 * i))

        result = int()

        for num in nums:
            result = result ^ num
        return result