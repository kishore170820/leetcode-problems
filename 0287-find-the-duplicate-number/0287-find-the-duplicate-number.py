class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate={}
        for i in nums:
            if i not in duplicate:
                duplicate[i]=1
            else:
                return i


 