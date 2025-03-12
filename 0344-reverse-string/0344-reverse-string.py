class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l1=0
        l2=len(s)-1
        while l1<l2:
            s[l1],s[l2]=s[l2],s[l1]
            l1+=1
            l2-=1