class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = [num for row in grid for num in row]
        return [sum(nums) - sum(set(nums)), list(set(range(1, len(nums) + 1)) - set(nums))[0]]