<<<<<<< HEAD
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fmap = {}
        smap = {}
        for i in s:
            fmap[i] = fmap.get(i, 0) + 1
        for j in t:
            smap[j] = smap.get(j, 0) + 1
        return fmap == smap
=======
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fmap = {}
        smap = {}
        for i in s:
            fmap[i] = fmap.get(i, 0) + 1
        for j in t:
            smap[j] = smap.get(j, 0) + 1
        return fmap == smap
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
