class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stash = {}

        for i in nums1:
            stash[i] = stash.get(i,0) + 1
        
        res = []
        for i in nums2:
            if stash.get(i,0) > 0:
                res.append(i)
                stash[i] = stash.get(i,0) - 1 

        return res 
        