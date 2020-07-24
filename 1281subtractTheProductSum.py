class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        str_n = str(n)
        product = 1
        sumn = 0
        for num in str_n:
            product = product * int(num)

        for num in str_n:
            sumn = sumn + int(num)

        return (product - sumn)