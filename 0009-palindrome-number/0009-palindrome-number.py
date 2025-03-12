class Solution:
    def isPalindrome(self, x):
        n=str(x)
        rev=n[::-1]
        return n==rev
        