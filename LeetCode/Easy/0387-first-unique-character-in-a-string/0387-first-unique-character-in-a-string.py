class Solution:
    def firstUniqChar(self, s: str) -> int:
        hsh = dict()

        for i in s:
            hsh[i] = hsh.get(i,0) + 1

        # for k , v in hsh.items():
        #     if v == 1:
        #         return s.index(k)
        #         break

        for i , ch in enumerate(s):
            if hsh[ch] == 1:
                return i

        return -1
        