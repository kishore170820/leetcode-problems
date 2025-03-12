class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result=[]
        for i in range(0,len(s),2*k):
            rev1=s[i:i + k]
            rev2=s[i + k:i + 2*k]
            result.append(rev1[::-1]+rev2)
        return ''.join(result)
            