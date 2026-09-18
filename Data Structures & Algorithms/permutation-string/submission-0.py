class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        le = len(s1)

        mainmap = {}

        for ch in s1:
            mainmap[ch] = mainmap.get(ch, 0) + 1

        hm = {}

        for i in range(le):
            hm[s2[i]] = hm.get(s2[i], 0) + 1

        l = 0
        r = le - 1

        while True:

            if hm == mainmap:
                return True

            r += 1

            if r >= len(s2):
                break

            hm[s2[r]] = hm.get(s2[r], 0) + 1

            hm[s2[l]] -= 1

            if hm[s2[l]] == 0:
                del hm[s2[l]]

            l += 1

        return False