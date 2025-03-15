class Solution:
    def containsDuplicate(self, lst: List[int]) -> bool:
        return len(lst) != len(set(lst))