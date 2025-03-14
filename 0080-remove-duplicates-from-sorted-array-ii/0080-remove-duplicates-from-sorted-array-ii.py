class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count=0
        for num in nums:
            if count < 2 or num != nums[count-2]:
                nums[count]=num
                count+=1
        return count