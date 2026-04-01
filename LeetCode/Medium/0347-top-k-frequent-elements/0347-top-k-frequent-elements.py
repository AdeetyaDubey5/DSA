class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = dict()

        for i in nums:
            hsh[i] = hsh.get(i,0) + 1

        sorted_hsh = dict(sorted(hsh.items(),key=lambda item:item[1],reverse=True))

        cnt = 0
        res = []
        for keys in sorted_hsh.keys():
            if cnt == k:
                break
            res.append(keys)
            cnt += 1 

        return res
        