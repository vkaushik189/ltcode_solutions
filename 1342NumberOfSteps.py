class Solution:
    def numberOfSteps(self, ans: int) -> int:

        steps = 0

        while ans != 0:
            if ans % 2 == 0:
                ans = ans / 2
                steps += 1
            else:
                ans -= 1
                steps += 1
        return steps
