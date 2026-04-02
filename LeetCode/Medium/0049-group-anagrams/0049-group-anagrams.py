class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        stash = defaultdict(list)

        for word in strs:
            letters = "".join(sorted(word))  # "eat" -> ['a','e','t'] -> "aet"
            stash[letters].append(word)   # stash['aet'] = ["eat","tea","ate"]

        res = list(stash.values())

        return res
        