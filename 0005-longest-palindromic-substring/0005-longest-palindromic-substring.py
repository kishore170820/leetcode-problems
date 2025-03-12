class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        result_len=0
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1) > result_len:
                    result_len=right-left+1
                    result=s[left:right+1]
                left-=1
                right+=1
            left,right=i,i+1
            while left>=0 and right<(len(s)) and s[left]==s[right]:
                if (right-left+1)>result_len:
                    result_len=right-left+1
                    result=s[left:right+1]
                left-=1
                right+=1
        return result
            
        