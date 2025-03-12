class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tol=sorted(nums1+nums2)
        n=len(tol)
        if n%2==1:
            return float(tol[n//2])
        else:
            return (tol[n//2-1]+tol[n//2])/2.0