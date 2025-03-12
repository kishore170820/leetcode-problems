class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        curr_sum=nums[0]
        for num in nums[1:]:
            curr_sum=max(num,curr_sum+num)
            sum=max(sum,curr_sum)
        return sum