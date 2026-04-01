class Solution:
    def firstUniqChar(self, s: str) -> int:
        hsh = dict()

        for i in s:
            hsh[i] = hsh.get(i,0) + 1

        for k , v in hsh.items():
            if v == 1:
                return s.index(k)
                break

        return -1
        