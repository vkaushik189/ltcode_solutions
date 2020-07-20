class Solution:
    def shuffle(nums=[2, 5, 1, 3, 4, 7], n=3):

        numsX = nums[:n]
        numsY = nums[n:]

        numsNew = []

        a = 0
        b = 0

        for i in range(0, len(nums)):
            if i % 2 == 0:
                numsNew.append(numsX[a])
                a = a + 1
                print(a)
            else:
                numsNew.append(numsY[b])
                b = b + 1
        return numsNew