class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a=int(a,2)
        int_b=int(b,2)
        res=int_a+int_b
        return bin(res)[2:]