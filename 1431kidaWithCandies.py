class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_num = 0
        for i in range(len(candies)):
            if candies[i] > max_num:
                max_num = candies[i]
        bool_list = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_num:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list