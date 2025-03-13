class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                subset = res[j] + [nums[i]]
                if subset not in res:
                    res.append(subset)
        return res

    