class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        t=[]
        n=[]
        for i in nums:
            if i in t:
                t.remove(i)
            else:
                t.append(i)
        return t