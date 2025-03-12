class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX=2**31-1
        if dividend == -2**31 and divisor == -1:
            return MAX

        a=int(dividend/divisor)
        return a