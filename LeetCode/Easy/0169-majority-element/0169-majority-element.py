class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        stash = dict()

        for i in nums:
            stash[i] = stash.get(i,0) + 1

        for key, value in stash.items():
            if value > len(nums) / 2:
                return key