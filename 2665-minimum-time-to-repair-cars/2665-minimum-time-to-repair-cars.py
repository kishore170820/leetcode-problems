class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, max(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if sum(int((mid // rank) ** 0.5) for rank in ranks) >= cars:
                right = mid
            else:
                left = mid + 1
        return left