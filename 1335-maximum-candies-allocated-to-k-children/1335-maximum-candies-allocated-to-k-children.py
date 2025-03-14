class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        low, high = 1, max(candies)
        while low < high:
            mid = (low + high + 1) // 2
            if sum(c // mid for c in candies) >= k:
                low = mid
            else:
                high = mid - 1
        return low