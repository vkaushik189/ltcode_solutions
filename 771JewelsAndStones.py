class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        count = 0
        for charj in J:
            for chars in S:
                if charj == chars:
                    count += 1
        return count
        """
        # using hashing
        freq = {}
        count = 0

        for char in S:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        for char in J:
            if char in freq:
                count = count + freq[char]
        return count