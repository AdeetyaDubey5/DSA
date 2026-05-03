class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ele = 0
        for i in nums:
            ele = ele ^ i

        return ele 
        