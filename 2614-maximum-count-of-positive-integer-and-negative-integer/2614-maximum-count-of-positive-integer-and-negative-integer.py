class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count=sum(1 for i in nums if i>0)
        neg_count=sum(1 for i in nums if i<0)
        return max(pos_count,neg_count)