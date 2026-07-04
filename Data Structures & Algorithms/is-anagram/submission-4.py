class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}
        for i in s:
            if i not in smap: 
                smap[i] = 1 
            else: 
                smap[i] += 1 
        for j in t:
            if j not in tmap: 
                tmap[j] = 1 
            else: 
                tmap[j] += 1 
        return smap == tmap

                    