class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        hm = {}
        l = sum(wall[0])
        n = len(wall)

        for w in wall:
            b = 0
            for i in range(len(w) - 1):
                b += w[i]
                hm[b] = hm.get(b, 0) + 1

        if not hm:
            return n

        max_gap = max(hm.values())

        return n - max_gap