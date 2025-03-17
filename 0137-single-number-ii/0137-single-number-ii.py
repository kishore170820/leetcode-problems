class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t=[]
        for i in nums:
            if i in t:
                t.remove(i)
            elif nums.count(i)==1:
                return i
        