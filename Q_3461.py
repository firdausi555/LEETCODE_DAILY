class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(digit) for digit in s] 
        while len(digits) > 2:
            ans = []  
            for pos in range(0,len(digits)-1):
                pairSum = digits[pos] + (digits[pos+1] if pos+1 < len(s) else 0)
                ans.append(pairSum % 10)  
            digits = ans


        return digits[0] == digits[1]
