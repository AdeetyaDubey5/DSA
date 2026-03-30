class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = dict()

        for i in arr:
            hash_map[i] = hash_map.get(i,0) + 1

        cnts = hash_map.values()

        return len(cnts) == len(set(cnts))
        