class Solution:
    def reverse(self, x: int) -> int:
        min,max=-2**31,2**31-1
        sign=-1 if x<0 else 1
        x*=sign
        rev=int(str(x)[::-1])
        rev*=sign
        if rev<min or rev>max:
            return 0
        return rev
        