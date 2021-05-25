class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fmap = {}
        smap = {}
        for i in s:
            fmap[i] = fmap.get(i, 0) + 1
        for j in t:
            smap[j] = smap.get(j, 0) + 1
        return fmap == smap
