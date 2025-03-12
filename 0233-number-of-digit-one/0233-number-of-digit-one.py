class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        base = 1
        numLower = 0
        
        while n > 0:
            curr = n % 10
            if curr > 1:
                cnt += base
            elif curr == 1:
                cnt += numLower + 1
            n //= 10
            cnt += n * base
            numLower += curr * base
            base *= 10
        
        return cnt