from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        p = permutations(nums)
        for i in list(p):
            lst.append(list(i))
        return lst