class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9 and len(digits) == 1:
            return [1,0]
        if digits[-1]!= 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits  
