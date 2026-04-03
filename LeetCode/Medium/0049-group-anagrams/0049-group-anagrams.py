class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        stash = defaultdict(list)

        for i in strs:
            wrd = "".join(sorted(i))
            stash[wrd].append(i)

        res = sorted(stash.values())

        return res
        