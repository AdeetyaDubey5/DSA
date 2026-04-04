class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        stash = {}
        res = []

        for i in range(len(nums)):
            fst = nums[i]
            snd = target - fst

            if stash.get(snd,-1) != -1:
                res.append(stash.get(snd,-1))
                res.append(i)
                break
            stash[fst] = i

        return res
            
        